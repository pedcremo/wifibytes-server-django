# encoding:utf-8
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import detail_route, list_route
from rest_framework.views import APIView

import os
import random
import string
import smtplib
from geo.models import Provincia

from cliente.serializers import ClienteSerializer, ClienteListSerializer
from cliente.serializers import cuentasbcocliSerializer, dirclientesSerializer
from cliente.serializers import mobilsclientsSerializer, CuentaSerializer
from cliente.models import Cliente, CuentasbcoCli, DirClientes, MobilsClients
from catalogo.models import Tarifa
from icc.models import RangoICC
from .models import *
from datos_empresa.models import DatosEmpresa, TextosContrato
from .serializers import *
from wifibytes.omv_functions import getpool, getCDR, altaCliente, altaLinea, getpoolSim
from wifibytes.omv_functions import portabilidadLinea, enviarDocumento
from wifibytes.functions import calculate_checksum, get_full_image_url
from wifibytes.utils import generate_pdf
import logging
# import email
# from smtplib import SMTPException
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime
from wifibytes.authlib import *
from wifibytes.configuracion_email import *
import json
import shutil
from signaturit_sdk.signaturit_client import SignaturitClient
import signal
from contextlib import contextmanager
from schwifty import IBAN

os.environ['DJANGO_SETTINGS_MODULE'] = 'wifibytes.settings.local'

# Get an instance of a logger
logger = logging.getLogger(__name__)

class DireccionesViewSet(viewsets.ModelViewSet):

    """
    API endpoint to View,Edit,Add, list Addresses.
    """
    queryset = DirClientes.objects.all()
    serializer_class = DireccionesSerializer

    def list(self, request):
        queryset = self.queryset.filter(codcliente__consumer_user=request.user)
        serializer = DireccionesSerializer(queryset, many=True)
        return Response({'results': serializer.data,
                         'count': len(serializer.data)})

    def get_queryset(self):
        queryset = self.queryset.filter(
            codcliente__consumer_user=self.request.user)
        received = self.request.query_params
        if 'default' in list(received.keys()):
            queryset = queryset.filter(default=True, domfacturacion=True)

        return queryset


# class ClienteViewSet(viewsets.ModelViewSet):
class ClienteViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):

    """
    API endpoint to View,Edit,Add, list Clients.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_permissions(self):
        # Permitir que usuarios no registrados se puedan registrar
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny, ]

        return super(ClienteViewSet, self).get_permissions()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            # comprobamos si el dni ya existe
            if (Cliente.objects
                       .filter(cifnif=serializer.validated_data.get('cifnif', ""))
                       .exists()):
                message = 'El dni introducido ya existe en la base de datos'
                return Response(data={"message": message, "isRegistered": True},
                                status=status.HTTP_400_BAD_REQUEST)

            # comprobamos si el email ya existe
            if (Cliente.objects
                       .filter(email__iexact=serializer.validated_data.get('email', ""))
                       .exists()):
                message = 'El email introducido ya existe en la base de datos'
                return Response(data={"message": message, "isRegistered": True},
                                status=status.HTTP_400_BAD_REQUEST)
            
            user = serializer.save()
            
            # --> SEND EMAIL WITH USER NAME
            query = self.request.query_params
            lang = query.get('lang', 'es')

            if lang == 'va':
                context = {
                    'title': 'Wifibytes',
                    'title_message': 'Benvingut!',
                    'content_message': 'Wifibytes, altra forma de fer comunicació. El teu proveïdor integral de comunicacions',
                    'center_message': "El teu nom d'usuari: %s <br/>Podràs utilitzar este codi o el teu email per autenticar-te" % user.codcliente,
                }
                subject = 'Benvingut!'
            else:
                context = {
                    'title': 'Wifibytes',
                    'title_message': 'Bienvenido!',
                    'content_message': 'Wifibytes, otra forma de hacer comunicación. Tu proveedor integralde telecomunicaiones',
                    'center_message': 'Tu nombre de usuario: %s <br/>Podrás utilizar este código o tu email para autenticarte' % user.codcliente,
                }
                subject = 'Bienvenido!'

            context['logo'] = 'https://backend.wifibytes.com/media/logo/wifibytes-logo.png'
            context['urlWeb'] = 'http://wifibytes.com/'

            #message = render_to_string('email/welcome.html', context,
            #                           context_instance=RequestContext(request)).encode('utf8')
            message = render_to_string('email/welcome.html', context)
            email_instance = Email()

            try:
                email_instance.sendemail(user.email, message,
                                     subject, True)
            except:
                logger.error('Register user has failed to sent and Email to '+user.email+' Something went wrong!')
                pass
            
            ###############

            return Response(self.serializer_class(user).data, status=status.HTTP_201_CREATED)

        message = 'Falta algún paramentro requerido'
        return Response(data={"message": message, "errors": serializer.errors, "isRegistered": False},
                        status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            client = Cliente.objects.get(pk=pk, consumer_user=request.user)
            serializer = ClienteSerializer(client)
            return Response(data=serializer.data,
                            status=status.HTTP_200_OK)
        except Cliente.DoesNotExist:
            return Response(data={"message": 'Unauthorized token'},
                            status=status.HTTP_401_UNAUTHORIZED)

    def partial_update(self, request, pk=None, *args, **kwargs):
        kwargs['partial'] = True
        client = cliente_token(pk, self.request.META.get('HTTP_AUTHORIZATION',
                                                         ''))
        return self.update(request, *args, **kwargs)


class LineaViewSet(viewsets.ModelViewSet):

    """
    API endpoint to View,Edit,Add, list Lineas.
    """
    queryset = MobilsClients.objects.all()
    serializer_class = LineaSerializer

    def get_queryset(self):
        user = self.request.user
        request_params = self.request.query_params

        if 'draft' in list(request_params.keys()):
            query = self.queryset.filter(
                codcliente__consumer_user=user, draft=True)
        else:
            query = self.queryset.filter(
                codcliente__consumer_user=user, draft=False)

        return query

    def get_serializer_context(self):
        query = self.request.query_params
        if 'lang' in list(query.keys()):
            lang = query['lang']
        else:
            lang = ''
        return {'lang': lang, 'request': self.request}


class CuentaViewSet(viewsets.ModelViewSet):

    """
    API endpoint to View,Edit,Add, list Lineas.
    """
    queryset = CuentasbcoCli.objects.all()
    serializer_class = CuentaSerializer

    def get_queryset(self):
        token = self.request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        queryset = self.queryset.filter(codcliente__token=token)
        return queryset

    def create(self, request):
        # serialize data
        serializer = CuentaSerializer(data=request.data)

        # check fields
        if serializer.is_valid():
            try:
                iban = IBAN(serializer.validated_data.get('iban', None))
                cuenta = serializer.save()
                cuenta_s = self.serializer_class(cuenta)
                return Response(
                    cuenta_s.data, status=status.HTTP_201_CREATED)
            except ValueError as err:
                return Response(data={"message": str(err)},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class activarLinea(APIView):

    def post(self, request):
        query = self.request.data
        if 'id_linea' in list(query.keys()):
            linea = MobilsClients.objects.get(pk=query['id_linea'])
            activacion = enviarDocumento(linea)
            if (activacion['status_code'] == 200 and
                    (activacion['response_code'] == '0001' or
                     activacion['response_code'] == '0017')):
                linea.activa = True
                linea.save()
                return Response(data={"message": "Linea activada"},
                                status=status.HTTP_200_OK)
            else:
                return Response(data={"message": activacion['message']},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"message": "Falta el campo linea"},
                            status=status.HTTP_400_BAD_REQUEST)


class getContracts(APIView):

    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        def make_action(linea):
            cliente = linea.codcliente

            if linea.nuevoicc:
                print(('linea', linea))
                new_partial_icc = str(linea.nuevoicc)[:-1]
                try:
                    new_icc_dc = str(linea.nuevoicc)[-1:]
                except Exception:
                    new_icc_dc = 0
            else:
                '''
                    last_icc = MobilsClients.objects.all().exclude(
                        nuevoicc=None).exclude(nuevoicc='')
                    if last_icc.count() == 0:
                        new_partial_icc = 893490307130123081
                    else:
                        last_icc = last_icc.order_by('-nuevoicc')[0].nuevoicc
                        new_partial_icc = (int(last_icc) / 10) + 1

                    new_icc_dc = calculate_checksum(new_partial_icc)
                new_icc = RangoICC.objects.filter(
                    rango_icc_activo=True).first().nuevo_icc_a_registrar
                '''

                # new_icc_dc = calculate_checksum(new_partial_icc)
                # new_partial_icc = (int(new_icc) / 10) + 1
                # new_icc_dc = calculate_checksum(new_partial_icc)

                try:
                    result = getpoolSim()
                    print (result)
                    print('------')
                    print((result['response']['icc']))
                    print((result['response']['dc']))
                    new_partial_icc = result['response']['icc']
                    new_icc_dc = result['response']['dc']
                except Exception as error:
                    new_partial_icc = str(0000000000)
                    new_icc_dc = str(0)

                linea.nuevoicc = str(new_partial_icc) + str(new_icc_dc)
                linea.save()

                print(('[PARTIAL ICC] --> ', new_partial_icc))
                print(('[DC ICC] --> ', new_icc_dc))
                print ('linea save')

            if(linea.origen == 1):
                return 200
                print ('origen uno')
                alta = portabilidadLinea(
                    linea, new_partial_icc, new_icc_dc)
            else:
                # test
                #new_partial_icc = 893490307130123160
                #new_icc_dc = calculate_checksum(new_partial_icc)

                print ('origen dos')
                print(('partial_icc', new_partial_icc))
                print(('new_icc_dc', new_icc_dc))
                alta = altaLinea(
                    linea, new_partial_icc, new_icc_dc)

            message = alta['message']

            print(('message--> ', message))
            if alta['response_code'] == '0001':
                linea.alta = True
                linea.omv_solicitud = alta['n_solicitud']
                linea.mobil = alta['movil']
                linea.fechaContrato = datetime.now()
                linea.save()
            elif alta['response_code'] == '0020' or \
                    (linea.origen == 1 and alta['response_code'] == '0024'):
                icc = int(new_partial_icc) + 1
                icc_dc = calculate_checksum(icc)
                linea.nuevoicc = str(icc) + str(icc_dc)
                linea.fechaContrato = datetime.now()
                linea.save()
                action = make_action(linea)
                if action["status"] == 200:
                    linea = action['linea']
                else:
                    return action
            else:
                return {"status": 400, "response": Response(
                    data={"message": message},
                    status=status.HTTP_400_BAD_REQUEST)}

            return {"status": 200, "linea": linea}

        # VARIABLES
        global_folder_contracts_path = \
            os.path.join(settings.MEDIA_ROOT, 'contratos')

        client_folder_contract_path = \
            os.path.join(global_folder_contracts_path, str(request.user))
        query = self.request.query_params
        now = datetime.now()
        months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                  'julio', 'agosto', 'septiembre', 'octubre', 'noviembre',
                  'diciembre']
        company = {
            'name': 'Wifibytes, S.L',
            'address': 'C\ Batalla de Lepanto No 5 Bajo -46880-',
            'city': 'Bocairent (València)',
            'CIF': 'B98137078',
            'phone': '960 500 606',
            'logo': 'img/pdf/logo-wifibytes.png'
        }
        try:  # Get company Data
            data_company = DatosEmpresa.objects.filter(datos_empresa_default=True).first()
            print(data_company)
            company['name'] = data_company.name
            company['address'] = data_company.address
            company['city'] = data_company.city
            company['CIF'] = data_company.cifnif
            company['phone'] = data_company.phone
            company['logo'] = get_full_image_url(request, data_company.logo.url)
        except Exception as error:
            print ('[ERROR] --> datos_empresa DoesNotExist')
            print(error)
            return {
                "status": 400,
                "response": Response(
                    data={"message": 'Datos_Empresa DoesNotExist'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            }
        # Get Contract Textos
        try:
            textos_contrato = TextosContrato.objects.filter(
                textos_contrato_default=True
            ).first().textos
        except Exception as error:
            print (error)
            textos_contrato = []

        date = {
            'day': now.day,
            'month': months[now.month - 1],
            'monthNumber': now.month,
            'year': now.year
        }
        file_path = []
        cliente = None
        cuenta = None
        direccion = None
        linea = None
        name = None
        #######

        # check if exist global contracts folder and client folder
        if not os.path.exists(global_folder_contracts_path):
            os.makedirs(global_folder_contracts_path)
        if not os.path.exists(client_folder_contract_path):
            os.makedirs(client_folder_contract_path)
        #######

        if 'line' in list(query.keys()):
            try:
                linea = MobilsClients.objects.get(pk=query['line'])
            except MobilsClients.DoesNotExist:
                return Response(data={"message": "La linea no existe"},
                                status=status.HTTP_400_BAD_REQUEST)

            # Hack

            #action = make_action(linea)

            '''
            if action["status"] == 200:
                linea = action['linea']
                cliente = linea.codcliente
            else:
                return action["response"]'''

            cliente = linea.codcliente

            cuenta = linea.codcuenta
            direccion = linea.coddir
            # linea.fecha_contrato = linea.fechaContrato.strftime('%d/%m/%Y')
            # cliente.birthday_omv = cliente.birthday_omv.strftime('%d/%m/%Y')

            # OLD CONTRACT ##############################
            old_template = 'pdf/contract.html'
            context = {'cliente': cliente, 'direccion': direccion,
                       'linea': linea, 'cuenta': cuenta, 'company': company,
                       'date': date, 'textos': textos_contrato}
            pdf_old = generate_pdf(old_template, context=context)
            pdf_old_path = \
                os.path.join(client_folder_contract_path,
                             'contrato_servicio_movil_%s.pdf' %
                             now.strftime('%Y_%m_%d_%Hh_%Mm_%Ss'))
            with open(pdf_old_path, 'w') as fd:
                pdf_old.seek(0)
                shutil.copyfileobj(pdf_old, fd)
            file_path.append(pdf_old_path)
            # OLD CONTRACT ##############################

        if 'service' in list(query.keys()):

            try:
                service = Servicio.objects.get(pk=query['service'])
            except Servicio.DoesNotExist:
                return Response(data={"message": "El servicio no existe"},
                                status=status.HTTP_400_BAD_REQUEST)

            cliente = service.servicio_consumer if not cliente else cliente
            cuenta = service.servicio_cuenta if not cuenta else cuenta
            direccion = service.servicio_direccion

            if service.servicio_telefono_anterior:
                # PORTABILITY ##############################
                portability_template = 'pdf/wifibytes_portability.html'
                context = {'cliente': cliente, 'direccion': direccion,
                           'cuenta': cuenta, 'company': company, 'date': date,
                           'service': service}
                pdf_portability = generate_pdf(portability_template,
                                               context=context)
                pdf_portability_path = \
                    os.path.join(client_folder_contract_path,
                                 'portabilidad_contrato_%s.pdf' %
                                 now.strftime('%Y_%m_%d_%Hh_%Mm_%Ss'))
                with open(pdf_portability_path, 'w') as fd:
                    pdf_portability.seek(0)
                    shutil.copyfileobj(pdf_portability, fd)
                file_path.append(pdf_portability_path)
                # PORTABILITY ##############################

            # REQUEST SERVICE ##############################
            services_template = 'pdf/wifibytes_requestService.html'
            context = {'cliente': cliente, 'direccion': direccion,
                       'cuenta': cuenta, 'company': company, 'date': date,
                       'service': service}

            for subrate in service.servicio_tarifa.getSubtarifas:
                if (subrate.tipo_tarifa == 2):
                    context['fijo'] = subrate
                elif (subrate.tipo_tarifa == 3):
                    context['fibra'] = subrate
                elif (subrate.tipo_tarifa == 4):
                    context['wifi'] = subrate
                elif (subrate.tipo_tarifa == 5):
                    context['tv'] = subrate

            pdf_request_service = \
                generate_pdf(services_template, context=context)
            pdf_request_service_path = \
                os.path.join(client_folder_contract_path,
                             'solicitud_servicio_contrato_%s.pdf' %
                             now.strftime('%Y_%m_%d_%Hh_%Mm_%Ss'))
            with open(pdf_request_service_path, 'w') as fd:
                pdf_request_service.seek(0)
                shutil.copyfileobj(pdf_request_service, fd)
            file_path.append(pdf_request_service_path)
            # REQUEST SERVICE ##############################

        # WIFIBYTES CONTRACT ##############################

        wifibytes_template = 'pdf/wifibytes_contract_v1.html'
        context = {'company': company, 'date': date, 'textos': textos_contrato}
        pdf_wifibytes = generate_pdf(wifibytes_template, context=context)
        pdf_wifibytes_path = \
            os.path.join(client_folder_contract_path,
                         'wifibytes_contrato_%s.pdf' %
                         now.strftime('%Y_%m_%d_%Hh_%Mm_%Ss'))
        with open(pdf_wifibytes_path, 'w') as fd:
            pdf_wifibytes.seek(0)
            shutil.copyfileobj(pdf_wifibytes, fd)
        file_path.append(pdf_wifibytes_path)
        # WIFIBYTES CONTRACT ##############################

        # SEPA CONTRACT ##############################
        sepa_template = 'pdf/sepaContract.html'
        context = {'cliente': cliente, 'direccion': direccion,
                   'cuenta': cuenta, 'company': company, 'date': date}
        pdf_sepa = generate_pdf(sepa_template, context=context)
        pdf_sepa_path = \
            os.path.join(client_folder_contract_path,
                         'sepa_contrato_%s.pdf' %
                         now.strftime('%Y_%m_%d_%Hh_%Mm_%Ss'))
        with open(pdf_sepa_path, 'w') as fd:
            pdf_sepa.seek(0)
            shutil.copyfileobj(pdf_sepa, fd)
        file_path.append(pdf_sepa_path)
        # SEPA CONTRACT ##############################

        # SIGNATURIT ##############################
        urls = []
        recipients = {
            'fullname': '%s %s' % (cliente.nombre, cliente.apellido),
            'email': cliente.email,
            'limit': 5
            # 'require_signature_in_coordinates': [] # specific sign page
        }
        client = SignaturitClient(settings.SIGNATURIT_ACCESS_TOKEN)
        for path in file_path:
            signature = client.create_signature(
                [path], recipients, {
                    'delivery_type': 'url',
                })
            if 'sepa' in signature['documents'][0]['file']['name']:
                name = 'Contrato Sepa'
            elif 'solicitud_servicio' in signature['documents'][0]['file']['name']:
                name = 'Contrato Servicio'
            elif 'wifibytes' in signature['documents'][0]['file']['name']:
                name = 'Contrato Wifibytes'
            elif 'portabilidad' in signature['documents'][0]['file']['name']:
                name = 'Contrato Portabiliad'
            elif 'servicio_movil' in signature['documents'][0]['file']['name']:
                name = 'Contrato Movil'
            urls.append({'url': signature['url'],
                         'id': signature['id'],
                         'name': name,
                         'signed': False})
        # SIGNATURIT ##############################

        if linea:
            linea.signature_id = signature['id']
            linea.document_id = signature['documents'][0]['id']
            linea.save()

        return Response(data={"urls": urls},
                        status=status.HTTP_200_OK)


# VVVVVVVVVVVVVVVVVV


class ClienteAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None, *args, **kwargs):
        # print request.META['QUERY_STRING']
        query = self.request.query_params
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            codcliente = query['id_consumer_token']
        except Exception:
            message = ('Error: falta algun parametro,'
                       '[id_consumer_token][token] necesarios ')
            return Response(data={"message": message},
                            status=status.HTTP_403_FORBIDDEN)

        if not cliente_token(codcliente, token):
            return Response('the user is not compatible with the token',
                            status=status.HTTP_403_FORBIDDEN)

        if 'codcliente' in list(query.keys()):
            codcliente = query.get('codcliente')

            try:
                item = Cliente.objects.get(pk=codcliente)
                serializer = ClienteListSerializer(item)
                return Response(serializer.data)
            except Cliente.DoesNotExist:
                message = 'Error: No existe [cliente]'
                return Response(data={"message": message},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            items = Cliente.objects.all()
            paginator = PageNumberPagination()
            result_page = paginator.paginate_queryset(items, request)
            serializer = ClienteSerializerGet(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializerA = ClienteSerializer(data=request.data, partial=False)
        # comprobamos que los datos sean válidos
        if serializerA.is_valid():
            # comprobamos si el dni ya existe
            if (Cliente.objects
                       .filter(cifnif=serializerA.validated_data.get('cifnif', ""))
                       .exists()):
                message = 'EEl dni introducido ya existe en la base de datos'
                return Response(data={"message": message, "isRegistered": True},
                                status=status.HTTP_400_BAD_REQUEST)

            # comprobamos si el email ya existe
            if (Cliente.objects
                       .filter(email__iexact=serializerA.validated_data.get('email', ""))
                       .exists()):
                message = 'EEl email introducido ya existe en la base de datos'
                return Response(data={"message": message, "isRegistered": True},
                                status=status.HTTP_400_BAD_REQUEST)

            user = serializerA.save()
            user_response = ClienteSerializer(user)
            return Response(user_response.data, status=201)
        else:
            message = 'FFalta algún paramentro requerido'
            return Response(data={"message": message, "isRegistered": False},
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        dict_data = {}
        received = request.data
        query = self.request.query_params
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            id_cliente_token = request.DATA['id']
        except Exception:
            message = ('Error: falta algun parametro,'
                       '[id_cliente_token][token] necesarios ')
            return Response(data={"message": message},
                            status=status.HTTP_403_FORBIDDEN)

        if not cliente_token(id_cliente_token, token):
            return Response('the user is not compatible with the token',
                            status=status.HTTP_403_FORBIDDEN)

        try:
            item = Cliente.objects.get(codcliente=id_cliente_token)
        except Cliente.DoesNotExist:
            return Response(status=404)
        serializer = ClienteListSerializer(
            item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            message = "Actualización Exitosa"
            return Response(data={"message": message}, status=201)
        return Response(data={"message": "Data invalida en serializer"},
                        status=400)

    def delete(self, request, id, format=None):
        try:
            item = Cliente.objects.get(pk=id)
        except Cliente.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ClienteNoRegistradoView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        received = self.request.data

        if 'cifnif' in list(received.keys()):
            try:
                user = Cliente.objects.filter(cifnif=received['cifnif'])[0]
            except Exception:
                return Response({'message': 'Error: client not found'},
                                status=status.HTTP_400_BAD_REQUEST)
        elif 'email' in list(received.keys()):
            try:
                user = Cliente.objects.filter(email=received['email'])[0]
            except Exception:
                return Response({'message': 'Error: client not found'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Error: cifnif or email needed'},
                            status=status.HTTP_400_BAD_REQUEST)

        newpass = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        dict_data = {'codcliente': user.codcliente, 'password': newpass,
                     'is_active': 'True'}

        serializer = ClienteSerializer(user, data=dict_data,
                                       context={'request': request},
                                       partial=True)

        if serializer.is_valid():
            #serializer.save()
            message = "Actualización Exitosa"
            email_instance = Email()
            if email_instance.sendemail_updatepass(newpass, user.email, user.codcliente):
                serializer.save() #We send email if we have send it the email
                return Response({'message': message},
                                status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Error sending email'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Error parsing user'},
                            status=status.HTTP_400_BAD_REQUEST)


class cuentasbcocliAPIListView(APIView):

    def get(self, request, format=None):
        query = self.request.query_params

        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            q_codcliente = query.get('codcliente')
        except Exception:
            message = ('Error: falta algun parametro,'
                       '[q_codcliente][token] necesarios ')
            return Response(data={"message": message},
                            status=status.HTTP_403_FORBIDDEN)

        if not cliente_token(q_codcliente, token):
            return Response(
                'the user is not compatible with the token',
                status=status.HTTP_403_FORBIDDEN)

        try:
            item = CuentasbcoCli.objects.get(codcliente=q_codcliente)
            serializer = cuentasbcocliSerializer(item)
            return Response(serializer.data)
        except CuentasbcoCli.DoesNotExist:
            message = 'Error: No existe [codcliente]'
            return Response(
                data={"message": message},
                status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = cuentasbcocliSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, format=None):
        received = request.data
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            id_cliente_token = request.DATA['id']
        except Exception:
            message = 'Error: falta algun parametro, [id_cliente_token][token] necesarios '
            return Response(
                data={"message": message}, status=status.HTTP_403_FORBIDDEN)

        if not cliente_token(id_cliente_token, token):
            return Response(
                'the user is not compatible with the token',
                status=status.HTTP_403_FORBIDDEN)
        try:
            item = CuentasbcoCli.objects.get(codcliente=id_cliente_token)
        except CuentasbcoCli.DoesNotExist:
            return Response(status=404)
        serializer = cuentasbcocliSerializer(
            item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            message = "Actualización Exitosa"
            return Response(data={"message": message}, status=201)
        return Response(
            data={"message": "Data invalida en serializer"}, status=400)


class dirclientesAPIListView(APIView):

    def get(self, request, format=None):

        query = self.request.query_params

        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            q_codcliente = query.get('codcliente')
        except Exception:
            message = 'Error: falta algun parametro, [q_codcliente][token] necesarios '
            return Response(
                data={"message": message}, status=status.HTTP_403_FORBIDDEN)

        if not cliente_token(q_codcliente, token):
            return Response('the user is not compatible with the token',
                            status=status.HTTP_403_FORBIDDEN)

        try:
            if 'id_dir' in list(query.keys()):
                id_dir = query.get('id_dir')
                dirs = DirClientes.objects.get(pk=id_dir)
                direcciones = {
                    'id': dirs.id,
                    'codcliente': dirs.codcliente.codcliente,
                    'domenvio': dirs.domenvio,
                    'domfacturacion': dirs.domfacturacion,
                    'nombre': str(dirs.nombre),
                    'cifnif': dirs.cifnif,
                    'direccion': str(dirs.direccion),
                    'codpais': dirs.codpais,
                    'ciudad': str(dirs.ciudad),
                    'provincia': str(dirs.provincia),
                    'apartado': dirs.apartado,
                    'codpostal': dirs.codpostal,
                    'telefono': dirs.telefono,
                    'numero': dirs.numero
                }
                return Response(
                    {"result": direcciones}, status=status.HTTP_200_OK)
            else:
                item = DirClientes.objects.filter(codcliente=q_codcliente)

            serializer = dirclientesSerializer(item, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except DirClientes.DoesNotExist:
            message = 'Error: No existe [codcliente]'
            return Response(data={"message": message},
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        dict_data = {}
        query = self.request.data
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            id_cliente_token = request.DATA['codcliente']
        except Exception:
            message = 'Error: falta algun parametro, [id_cliente_token][token] necesarios '
            return Response(data={"message": message},
                            status=status.HTTP_403_FORBIDDEN)

        if not cliente_token(id_cliente_token, token):
            return Response('the user is not compatible with the token',
                            status=status.HTTP_403_FORBIDDEN)

        codcliente_q = query.get('codcliente')
        facturacion_q = query.get('domfacturacion')
        envio_q = query.get('domenvio')

        if envio_q == 'True':
            item = DirClientes.objects.filter(
                codcliente=codcliente_q).update(domenvio=0)
        if facturacion_q == 'True':
            item = DirClientes.objects.filter(
                codcliente=codcliente_q).update(domfacturacion=0)

        serializerd = dirclientesSerializer(data=request.data)
        if serializerd.is_valid():
            serializerd.save()
            return Response(serializerd.data, status=201)
        return Response(serializerd.errors, status=400)

    def put(self, request, format=None):
        dict_data = {}
        query = request.data

        dircliente_q = query.get('id')
        codcliente_q = query.get('codcliente')
        facturacion_q = query.get('domfacturacion')
        envio_q = query.get('domenvio')
        if envio_q == 'True':
            item = DirClientes.objects.filter(
                codcliente=codcliente_q).update(domenvio=0)
        if facturacion_q == 'True':
            item = DirClientes.objects.filter(
                codcliente=codcliente_q).update(domfacturacion=0)

        try:
            item = DirClientes.objects.get(
                codcliente=codcliente_q, id=dircliente_q)
            # print ":-:"*30
        except DirClientes.DoesNotExist:
            return Response(data={"message": "La direccion no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = dirclientesSerializer(
            item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            message = "Actualización Exitosa"
            return Response(data={"message": message}, status=201)
        return Response(data={"message": "Data invalida en serializer"},
                        status=400)

    def delete(self, request, format=None):
        dict_data = {}
        received = request.data
        query = self.request.query_params
        id_dir = query['id_dir']
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            id_cliente_token = query['id']
        except Exception:
            message = 'Error: falta algun parametro, [id_cliente_token][token] necesarios '
            return Response(data={"message": message},
                            status=status.HTTP_403_FORBIDDEN)

        if not cliente_token(id_cliente_token, token):
            return Response('the user is not compatible with the token',
                            status=status.HTTP_403_FORBIDDEN)

        try:
            item = DirClientes.objects.get(pk=id_dir)
        except Cliente.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class mobils_clientsAPIListView(APIView):

    def get(self, request, format=None):

        query = self.request.query_params

        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            id_cliente_token = query.get('userId')
        except Exception:
            message = 'Error: falta algun parametro, [id_cliente_token][token] necesarios '
            return Response(
                data={"message": message}, status=status.HTTP_403_FORBIDDEN)

        if not cliente_token(id_cliente_token, token):
            return Response('the user is not compatible with the token',
                            status=status.HTTP_403_FORBIDDEN)

        if 'id_mobil' in list(query.keys()):
            id_mobil = query.get('id_mobil')
            items = MobilsClients.objects.filter(pk=id_mobil)
        else:
            items = MobilsClients.objects.filter(codcliente=id_cliente_token)

        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)

        serializer = mobilsclientsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        dict_data = MobilsClients()
        query = self.request.data

        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            id_cliente_token = request.DATA['codcliente']
        except Exception:
            message = 'Error: falta algun parametro, [id_cliente_token][token] necesarios '
            return Response(
                data={"message": message}, status=status.HTTP_403_FORBIDDEN)

        if not cliente_token(id_cliente_token, token):
            return Response(
                'the user is not compatible with the token',
                status=status.HTTP_403_FORBIDDEN)

        if 'direccion' in list(query.keys()):

            mobil = MobilsClients()
            mobil.codcliente = Cliente.objects.get(pk=query['codcliente'])
            mobil.roaming = 0
            mobil.buzon_voz = 0

            if 'titular' in list(query.keys()):
                mobil.tipoCliente = query['titular']
            else:
                return Response(
                    data={"message": "Falta tipo de cliente"}, status=400)

            if 'codtarifa' in list(query.keys()):
                mobil.codtarifa = Tarifa.objects.get(pk=query['codtarifa'])
            else:
                return Response(
                    data={"message": "Falta codtarifa"}, status=400)

            if 'mobil' in list(query.keys()):
                mobil.mobil = query['mobil']

            if 'tipoTarifaAntigua' in list(query.keys()):
                mobil.tipoTarifaAntigua = query['tipoTarifaAntigua']

            if 'companiaAntigua' in list(query.keys()):
                mobil.companiaAnterior = query['companiaAntigua']

            if 'tipoSim' in list(query.keys()):
                mobil.tipoSim = query['tipoSim']

            if 'icc_anterior' in list(query.keys()):
                mobil.icc_anterior = query['icc_anterior']

            if 'dc_icc_anterior' in list(query.keys()):
                mobil.dc_icc_anterior = query['dc_icc_anterior']

            if query['direccion']['id'] > 0:
                mobil.coddir = DirClientes.objects.get(
                    pk=query['direccion']['id'])
            else:
                direccion = DirClientes()
                try:
                    direccion.codcliente = Cliente.objects.get(
                        pk=query['codcliente'])
                except Cliente.DoesNotExist:
                    return Response(
                        data={"message": "Este cliente no existe"}, status=400)

                direccion.domenvio = 0
                direccion.domfacturacion = 1
                direccion.nombre = query['direccion']['nombre']
                direccion.cifnif = query['direccion']['cifnif']
                direccion.direccion = query['direccion']['direccion']
                direccion.numero = query['direccion']['numero']
                direccion.ciudad = query['direccion']['ciudad']
                direccion.provincia = query['direccion']['provincia']
                if 'idprovincia' in list(query['direccion'].keys()):
                    direccion.idprovincia = Provincia.objects.get(
                        pk=query['direccion']['idprovincia'])
                # direccion.apartado = query['direccion'].apartado
                direccion.codpostal = query['direccion']['codpostal']
                direccion.telefono = query['direccion']['telefono']
                direccion.save()
                mobil.coddir = direccion

            mobil.save()

            dict = {
                'id_mobilsclients': mobil.id_mobilsclients
            }

            return Response(data=dict, status=201)
        else:
            return Response(data={"message": "Falta direccion"}, status=400)

    def put(self, request, format=None):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            id_cliente_token = request.DATA['id']
            id_mobilsclients_q = request.DATA['id_mobilsclients']
        except Exception:
            message = 'Error: falta algun parametro, [id_cliente_token][token] necesarios '
            return Response(
                data={"message": message}, status=status.HTTP_403_FORBIDDEN)

        if not cliente_token(id_cliente_token, token):
            return Response('the user is not compatible with the token',
                            status=status.HTTP_403_FORBIDDEN)
        try:
            item = MobilsClients.objects.get(
                codcliente=id_cliente_token,
                id_mobilsclients=id_mobilsclients_q)
        except MobilsClients.DoesNotExist:
            return Response(status=404)
        serializer = mobilsclientsSerializer(
            item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            message = "Actualización Exitosa"
            return Response(data={"message": message}, status=201)
        return Response(
            data={"message": "Data invalida en serializer"}, status=400)


class omvDisponibleNumbers(APIView):

    def get(self, request, format=None):

        query = self.request.query_params
        response = getpool()
        if response['status_code'] == 403:
            return Response(
                data={"message": "Forbidden"},
                status=status.HTTP_403_FORBIDDEN)
        else:
            number_list = ()
            for number in response['numbers']:
                number_list = number_list + ((number),)
            return Response(
                data={"results": response['numbers']},
                status=status.HTTP_200_OK)


class obtenerConsumoCliente(APIView):

    def get(self, request, format=None):
        print('obtener el consumo')

        query = self.request.query_params

        if 'id_linea' in list(query.keys()):
            id_linea = query['id_linea']
            try:
                linea = MobilsClients.objects.get(pk=id_linea)
                number = linea.mobil
                token = self.request.META['HTTP_AUTHORIZATION'].replace(
                    'JWT ', '')
                user_token = linea.codcliente.token
                if user_token != token:
                    raise Exception('invalid token')
            except MobilsClients.DoesNotExist:
                return Response(
                    data={"message": "la linea solicitada no existe"},
                    status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response(
                    data={"message": "Token inválido o cliente no existente"},
                    status=status.HTTP_401_UNAUTHORIZED)

            today = datetime.now()

            if 'mes' in list(query.keys()):
                mes = query['mes']
            else:
                mes = today.month

            if 'anyo' in list(query.keys()):
                anyo = query['anyo']
            else:
                anyo = today.year

            total_datos = 0
            try:
                for dato in response['CDR']:
                    total_datos += int(dato['segundos'])
                response = getCDR(mes, anyo, number, 'DATOS')
                if response['status_code'] == 403:
                    return Response(
                        data={"message": "Forbidden"},
                        status=status.HTTP_403_FORBIDDEN)
                else:
                    return Response(
                        data={"result": response['CDR'], "total_consumo": total_datos},
                        status=status.HTTP_200_OK)
            except Exception as error:
                results = [1]
                results[0] = {
                    'posicion': 9511,
                    'fecha': '01/07/15 00:16:29',
                    'origen': 651356298,
                    'segundos': 2072576,
                    'importe': 0.0000,
                    'patron': 'Grps_Mo_Nac'
                }

                return Response(
                    data={"result": results, "total_consumo": total_datos},
                    status=status.HTTP_200_OK)

        else:
            return Response(
                data={"message": "id de linea obligatorio"},
                status=status.HTTP_400_BAD_REQUEST)


class nuevaAlta(APIView):

    def get(self, request, format=None):

        query = self.request.query_params

        if 'id_linea' in list(query.keys()):
            response = altaCliente(query['id_linea'])
            return Response(
                data={"message": "Forbidden"},
                status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(
                data={"message": "id de linea obligatorio"},
                status=status.HTTP_400_BAD_REQUEST)


def ultimaslineasdashboard(request):

    lineas = MobilsClients.objects.all().order_by('-id_mobilsclients')[:5]
    lines = []
    for linea in lineas:

        try:
            fecha = datetime.strptime(
                str(linea.fechaContrato), '%Y-%m-%d').strftime('%d/%m/%Y')
        except:
            fecha = "None"

        try:
            numero = linea.mobil[:3] + " " + linea.mobil[3:-3] + " " + linea.mobil[6:]
        except:
            numero = "No especificado"

        info = {
            'lineaId': linea.id_mobilsclients,
            'clienteId': linea.codcliente.codcliente,
            'clienteEmail': linea.codcliente.email,
            'activa': linea.activa,
            'fecha': fecha,
            'numero': numero
        }
        lines.append(info)

    return HttpResponse(
        json.dumps({'results': lines}), content_type='application/json; utf-8')


def ultimosclientesdashboard(request):

    clientes = Cliente.objects.all().order_by('-codcliente')[:5]
    clients = []
    for cliente in clientes:

        try:
            fecha = datetime.strptime(
                str(cliente.fecha_registro), '%Y-%m-%d').strftime('%d/%m/%Y')
        except:
            fecha = "None"

        try:
            numero = cliente.telefono[:3] + " " + \
                cliente.telefono[3:-3] + " " + cliente.telefono[6:]
        except:
            numero = "No especificado"

        if len(numero) < 11:
            numero = "No especificado"

        info = {
            'codcliente': cliente.codcliente,
            'nombre': cliente.nombre + " " + cliente.apellido,
            'email': cliente.email,
            'cifnif': cliente.cifnif,
            'fecha': fecha,
            'telefono': numero
        }
        clients.append(info)

    return HttpResponse(
        json.dumps({'results': clients}),
        content_type='application/json; utf-8')


class ServicioViewSet(viewsets.ModelViewSet):
    """
    API endpoint to View,Edit,Add, list products.
    """
    queryset = Servicio.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ServicioSerializer

    def get_queryset(self):
        user = self.request.user
        request_params = self.request.query_params

        if 'draft' in list(request_params.keys()):
            query = self.queryset.filter(
                servicio_consumer__consumer_user=user, servicio_draft=True)
        else:
            query = self.queryset.filter(
                servicio_consumer__consumer_user=user, servicio_draft=False)

        return query
