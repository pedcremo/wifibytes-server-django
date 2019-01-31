# encoding:utf-8
from datetime import datetime
import random
from django.urls import reverse
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import render
from django.http import (
    HttpResponse,
    Http404,
)
from wifibytes.utils import generate_pdf

from facturacion.serializers import (
    FormaspagoSerializer,
    LineaspedidoscliSerializer,
    PedidoscliSerializer,
    ImpuestosSerializer,
    FormasEnvioSerializer,
    FacturascliSerializer,
)

from facturacion.models import (
    FormasPago,
    LineaPedidoCli,
    PedidoCli,
    Impuesto,
    FormasEnvio,
    facturasCli,
    lineasfacturascli,
)
from datos_empresa.models import DatosEmpresa, TextosContrato
from cliente.models import Cliente, DirClientes, MobilsClients
from catalogo.models import Articulo
from django.contrib.auth.models import User
from wifibytes.authlib import *
import json
import decimal

from pinax.stripe.actions import charges, customers, sources
from pinax.stripe.models import Card
from wifibytes.functions import get_full_image_url


class MakePayment(APIView):

    def get(self, request):

        received = request.data
        print(received)

        user = User.objects.get(pk=2)

        user = customers.get_customer_for_user(
            user=user
        )
        print("*" * 30)
        print(user)

        if 'pedido' in list(received.keys()):
            # pedido = PedidoCli.objects.get(pk=)
            # new_user = User.objects.get(username='pepito')

            # user = customers.create(
            #     user = new_user,
            #     card = "tok_18W83xG0oxKWmlJ25PPepmxq"
            # )

            # charge = charges.create(
            #     amount=decimal.Decimal("5.66"),
            #     customer= user.stripe_id
            # )
            return Response(status=204)


class FormasPagoAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = FormasPago.objects.get(pk=id)
            serializer = FormaspagoSerializer(item)
            return Response(serializer.data)
        except FormasPago.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = FormasPago.objects.get(pk=id)
        except FormasPago.DoesNotExist:
            return Response(status=404)
        serializer = FormaspagoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = FormasPago.objects.get(pk=id)
        except FormasPago.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


# class FormasPagoAPIListView(APIView):

#     def get(self, request, format=None):
#         items = FormasPago.objects.all()
#         paginator = PageNumberPagination()
#         result_page = paginator.paginate_queryset(items, request)
#         serializer = FormaspagoSerializer(result_page, many=True)
#         return paginator.get_paginated_response(serializer.data)

#     def post(self, request, format=None):
#         serializer = FormaspagoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


class LineaspedidoscliAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = LineaPedidoCli.objects.get(pk=id)
            serializer = LineaspedidoscliSerializer(item, context={'request': request})
            return Response(serializer.data)
        except LineaPedidoCli.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = LineaPedidoCli.objects.get(pk=id)
        except LineaPedidoCli.DoesNotExist:
            return Response(status=404)
        serializer = LineaspedidoscliSerializer(
            item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = LineaPedidoCli.objects.get(pk=id)
        except LineaPedidoCli.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class LineaspedidoscliAPIListView(APIView):

    def get(self, request, format=None):
        received = self.request.query_params

        if('idpedido' in list(received.keys())):
            pedido = PedidoCli.objects.get(pk=received['idpedido'])
            lineas = LineaPedidoCli.objects.filter(idpedido=pedido)
        else:
            return Response(data={'message': 'Pedido no recibido'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = LineaspedidoscliSerializer(lineas, many=True, context={'request': request})
        return Response(serializer.data)


class PedidoscliAPIView(APIView):

    def get(self, request, format=None):
        received = self.request.query_params
        if 'HTTP_AUTHORIZATION' in list(self.request.META.keys()):
            token = self.request.META['HTTP_AUTHORIZATION'].split(' ')[1]

            if('idpedido' in list(received.keys())):
                try:
                    item = PedidoCli.objects.get(pk=received['idpedido'], codcliente__token=token)
                    serializer = PedidoscliSerializer(item, context={'request': request})
                    return Response(serializer.data)
                except PedidoCli.DoesNotExist:
                    return Response(status=404)
        else:
            return Response(status=401)

    def put(self, request, id, format=None):
        try:
            item = PedidoCli.objects.get(pk=id)
        except PedidoCli.DoesNotExist:
            return Response(status=404)
        serializer = PedidoscliSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def post(self, request, format=None):

        received = request.data
        dict_data = PedidoCli()

        if('lineasPedido' in list(received.keys())):

            if('codcliente' in list(received.keys())):
                try:
                    codcliente = Cliente.objects.get(pk=received['codcliente'])
                    dict_data.codcliente = codcliente
                except Cliente.DoesNotExist:
                    return Response(data={'message': 'codcliente not exists'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={'message': 'codcliente not received'},
                                status=status.HTTP_400_BAD_REQUEST)

            if('formaenvio' in list(received.keys())):
                try:
                    formaenvio = FormasEnvio.objects.get(
                        pk=received['formaenvio'])
                    dict_data.formaEnvio = formaenvio
                except FormasEnvio.DoesNotExist:
                    return Response(data={'message': 'formaenvio not exists'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={'message': 'formaenvio not received'},
                                status=status.HTTP_400_BAD_REQUEST)

            if('coddir' in list(received.keys())):
                try:
                    coddir = DirClientes.objects.get(pk=received['coddir'])
                    dict_data.coddir = coddir
                except DirClientes.DoesNotExist:
                    return Response(
                        data={'message': 'Datos de facturación not exists'},
                        status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={'message': 'coddir not received'},
                                status=status.HTTP_400_BAD_REQUEST)

            if('coddirEnvio' in list(received.keys())):
                try:
                    coddirEnvio = DirClientes.objects.get(
                        pk=received['coddirEnvio'])
                    dict_data.coddirEnvio = coddirEnvio
                except DirClientes.DoesNotExist:
                    return Response(
                        data={'message': 'Direccion de envío not exists'},
                        status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={'message': 'coddirEnvio not received'},
                                status=status.HTTP_400_BAD_REQUEST)

            if('formapago' in list(received.keys())):
                try:
                    formapago = FormasPago.objects.get(
                        pk=received['formapago'])
                    dict_data.formaPago = formapago
                except FormasPago.DoesNotExist:
                    return Response(data={'message': 'formapago not exists'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={'message': 'formapago not received'},
                                status=status.HTTP_400_BAD_REQUEST)

            dict_data.save()

            if 'hasRate' in list(received.keys()) and received['hasRate']:
                linea = {
                    'id': Articulo.objects.filter(descripcion='SIM')[0],  # credit article
                    'cantidad': 1,
                    'precio': 0,
                    'total': 0
                }
                received['lineasPedido'].append(linea)

            try:
                pedido = PedidoCli.objects.get(pk=dict_data.idpedido)
                totalPedido = 0
                for linea in received['lineasPedido']:
                    try:
                        if isinstance(linea['id'], Articulo):
                            articulo = linea['id']
                        else:
                            articulo = Articulo.objects.get(pk=linea['id'])

                        nuevaLinea = LineaPedidoCli()
                        nuevaLinea.idpedido = pedido
                        nuevaLinea.referencia = articulo
                        nuevaLinea.cantidad = linea['cantidad']
                        nuevaLinea.pvpunitario = linea['precio']
                        nuevaLinea.pvptotal = linea['total']
                        nuevaLinea.pvpsindto = linea['total']
                        nuevaLinea.cerrada = False
                        nuevaLinea.save()

                        totalPedido = totalPedido + linea['total']
                    except Articulo.DoesNotExist:
                        return Response(
                            data={'message': 'articulo no existe'},
                            status=status.HTTP_400_BAD_REQUEST)

                if pedido.formaEnvio:
                    totalPedido += pedido.formaEnvio.precio

                pedido.total = totalPedido
                pedido.totaleuros = totalPedido
                pedido.save()

                if 'stripe_token' in list(received.keys()):

                    user = customers.get_customer_for_user(
                        user=codcliente.consumer_user
                    )

                    if user is None:
                        user = customers.create(
                            user=codcliente.consumer_user,
                            card=received['stripe_token']
                        )
                        card = Card.objects.get(customer_id=user.id)
                    else:
                        card = sources.create_card(
                            customer=user,
                            token=received['stripe_token']
                        )
                    try:
                        charge = charges.create(
                            amount=decimal.Decimal(pedido.total),
                            customer=user.stripe_id,
                            currency="eur",
                            source=card.stripe_id
                        )
                        pedido.pagado = True
                        pedido.save()

                        sources.delete_card(
                            customer=user, source=card.stripe_id)

                    except Exception as inst:
                        sources.delete_card(
                            customer=user, source=card.stripe_id)
                        return Response(data={'message': inst.args},
                                        status=status.HTTP_400_BAD_REQUEST)

                serializer = PedidoscliSerializer(pedido, context={'request': request})
                return Response(data={'result': serializer.data},
                                status=status.HTTP_200_OK)

            except PedidoCli.DoesNotExist:
                return Response(data={'message': 'pedido no guardado'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'message': 'no se han recibido líneas'},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        try:
            item = PedidoCli.objects.get(pk=id)
        except PedidoCli.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PedidoscliAPIListView(APIView):

    def get(self, request, format=None):
        received = self.request.query_params

        if('codcliente' in list(received.keys())):
            items = PedidoCli.objects.filter(
                codcliente=received['codcliente']).order_by('-fecha',
                                                            '-idpedido')
        else:
            return Response(data={'message': 'Cliente no recibido'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = PedidoscliSerializer(items, many=True,
                                          context={'request': request})
        return Response(serializer.data)

# Facturas


from rest_framework import pagination


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 10000


class FacturascliViewSet(viewsets.ModelViewSet):
    """
    API endpoint to View,Edit,Add, list facturasCli.
    """
    queryset = facturasCli.objects.all()
    serializer_class = FacturascliSerializer
    pagination_class = LargeResultsSetPagination
    # permission_classes = (AllowAny,)

    def get_queryset(self):
        token = self.request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        query = self.request.query_params
        queryset = self.queryset.filter(codcliente__token=token)

        order = '-'

        if 'order' in list(query.keys()):
            if query['order'] == 'asc':
                order = ''

        return queryset.order_by('-idfactura').order_by(order + 'idfactura')


class ImpuestosAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Impuesto.objects.get(pk=id)
            serializer = ImpuestosSerializer(item)
            return Response(serializer.data)
        except Impuesto.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Impuesto.objects.get(pk=id)
        except Impuesto.DoesNotExist:
            return Response(status=404)
        serializer = ImpuestosSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Impuesto.objects.get(pk=id)
        except Impuesto.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ImpuestosAPIListView(APIView):

    def get(self, request, format=None):
        items = Impuesto.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ImpuestosSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ImpuestosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FormasEnvioViewSet(viewsets.ModelViewSet):
    """
    API endpoint para mostrar formas de envío.
    """
    queryset = FormasEnvio.objects.all().order_by('precio')
    serializer_class = FormasEnvioSerializer
    paginate_by = 500
    paginate_by_param = 'page_size'
    max_paginate_by = 500

    def get_serializer_context(self):
        query = self.request.query_params
        if 'lang' in list(query.keys()):
            lang = query['lang']
        else:
            lang = ''
        return {'lang': lang}


class FormasPagoViewSet(viewsets.ModelViewSet):
    """
    API endpoint para mostrar formas de envío.
    """
    queryset = FormasPago.objects.all().order_by('nombre')
    serializer_class = FormaspagoSerializer
    permission_classes = (AllowAny,)
    paginate_by = 500
    paginate_by_param = 'page_size'
    max_paginate_by = 500

    def get_serializer_context(self):
        query = self.request.query_params
        if 'lang' in list(query.keys()):
            lang = query['lang']
        else:
            lang = ''
        return {'lang': lang}


def ultimospedidosdashboard(request):
    print('ARREEEE')
    pedidos = PedidoCli.objects.all().order_by('-idpedido')[:5]
    
    orders = []
    for pedido in pedidos:
        if pedido.estado == 0:
            estado = 'En proceso'
        elif pedido.estado == 1:
            estado = 'Enviado'
        elif pedido.estado == 2:
            estado = 'Entregado'
        elif pedido.estado == 3:
            estado = 'Cancelado'

        fecha = datetime.strptime(
            str(pedido.fecha), '%Y-%m-%d').strftime('%d/%m/%Y')

        info = {
            'pedidoId': pedido.idpedido,
            'clienteId': pedido.codcliente.codcliente,
            'clienteEmail': pedido.codcliente.email,
            'total': pedido.totaleuros,
            'fecha': fecha,
            'estado': estado
        }
        orders.append(info)

    print(orders)
    return HttpResponse(
        json.dumps({'results': orders}),
        content_type='application/json; utf-8')


''' Genera PDF de una factura '''


def factura_pdf(request, pk):
    try:
        factura = facturasCli.objects.get(pk=pk)
    except facturasCli.DoesNotExist:
        raise Http404("Factura no existe")

    lineas = lineasfacturascli.objects.filter(idfactura=pk)

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

    template = 'pdf/bill-template-pdf.html'
    context = {
        'factura': factura,
        'lineas': lineas,
        'company': company
    }

    # return render(request,template, context)
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf(template, file_object=resp, context=context)
    return result


def contrato_pdf(request, linea):
    try:
        linea = MobilsClients.objects.get(pk=linea)
    except MobilsClients.DoesNotExist:
        raise Http404("Esta linea no existe")

    cliente = linea.codcliente
    direccion = linea.coddir
    cuenta = linea.codcuenta
    cliente.birthday_omv = cliente.birthday_omv.strftime('%d/%m/%Y')
    template = 'pdf/contract.html'
    context = {'linea': linea, 'cliente': cliente, 'direccion': direccion,
               'cuenta': cuenta}

    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf(template, file_object=resp, context=context)
    return result
