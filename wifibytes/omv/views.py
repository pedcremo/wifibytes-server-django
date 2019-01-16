# encoding:utf-8

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from omv.serializers import OmvSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from omv.models import *
from wifibytes.authlib import *
from wifibytes.omv_functions import (
    activarBuzonDeVoz, desactivarBuzonDeVoz,
    activarRoaming, desactivarRoaming
)
from cliente.models import MobilsClients


class OmvAPIListView(APIView):

    def get(self, request, format=None):
        queryset = Omv.objects.all()
        serializer = OmvSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SetServiciosView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):

        received = request.data
        try:
            client = Cliente.objects.get(consumer_user=request.user)
            #client = Cliente.objects.get(codcliente=900000)

        except Exception as error:
            print(error)
            return Response(
                'Cliente Incorrecto',
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            mobil = MobilsClients.objects.get(
                codcliente=client,
                mobil=received['linea']
            )
        except Exception as error:
            print (error)
            return Response(
                'Linea Movil Incorrecta',
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            if 'function' in list(received.keys()):
                if received['function'] == 'activarBuzonDeVoz':
                    try:
                        activarBuzonDeVoz(mobil)
                    except Exception as error:
                        print (error)
                    mobil.buzon_voz = True
                if received['function'] == 'desactivarBuzonDeVoz':
                    try:
                        desactivarBuzonDeVoz(mobil)
                    except Exception as error:
                        print (error)
                    mobil.buzon_voz = False
                if received['function'] == 'activarRoaming':
                    try:
                        activarRoaming(mobil)
                    except Exception as error:
                        print (error)
                    mobil.roaming = True
                if received['function'] == 'desactivarRoaming':
                    try:
                        desactivarRoaming(mobil)
                    except Exception as error:
                        print (error)
                    mobil.roaming = False
                mobil.save()
            else:
                return Response(
                    'Funcion Incorrecta',
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as error:
            return Response(
                'Error procesando la Peticion',
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {
                'buzon_voz': {
                    'status': mobil.buzon_voz_procesing,
                    'value': mobil.buzon_voz
                },
                'roaming': {
                    'status:': mobil.roaming,
                    'value': mobil.roaming_procesing
                }

            }
        )
        '''
        return Response(
            'Solicitud Procesada',
            status=status.HTTP_200_OK
        )
        '''
