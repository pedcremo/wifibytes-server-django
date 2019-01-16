# encoding:utf-8

from rest_framework.response import Response
from rest_framework.views import APIView
from causa.serializers import CausaSerializer
from causa.models import Causa

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from wifibytes.authlib import *
from wifibytes.configuracion_email import *
import datetime


class NewCausaAPIView(APIView):

    def post(self, request, format=None):
        print("-----------------")
        print(request.DATA)
        print("-----------------")
        print(request.FILES)
        print("======================")
        query = request.DATA

        if 'nombre' in list(query.keys()):
            nombre = query['nombre']

        if 'descripcion' in list(query.keys()):
            descripcion = query['descripcion']

        if 'remitente' in list(query.keys()):
            remitente = query['remitente']

        if 'email' in list(query.keys()):
            email = query['email']


        b = Causa(nombre=nombre, descripcion=descripcion, visible=0, activo=0)
        b.save()
        #instancia de email
        email_instance = Email()

        if email_instance.sendemail_causa(remitente, nombre) and email_instance.sendemail_gracias(email, remitente, nombre):
            message = 'Email Send'
            return Response(data={"message":message}, status=status.HTTP_200_OK)
        else:
            message = 'Error Send email'
            return Response(data={"message":message}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializerCausa.data, status=201)


class CausaAPIView(APIView):

    def get(self, request, id, format=None):

        try:
            item = Causa.objects.get(pk=id)
            serializer = CausaSerializer(item)
            return Response(serializer.data)
        except Causa.DoesNotExist:
            return Response(status=404)


class CausaAPIListView(APIView):

    def get(self, request, format=None):
        query = self.request.QUERY_PARAMS
        # if 'destacado' in query.keys():
        #     q_destacado = query.get('destacado')
        #     try:
        #         queryset = Causa.objects.filter(destacado=q_destacado,visible=True).order_by('-fechainicio')[:5]
        #         serializer = CausaSerializer(queryset, many=True)
        #         return Response(serializer.data, status=status.HTTP_200_OK)
        #     except Causa.DoesNotExist:
        #         return Response(data={"message": "HTTP_400_BAD_REQUEST"}, status=status.HTTP_400_BAD_REQUEST)
        # el
        if 'actual' in list(query.keys()):
            try:
                queryset = Causa.objects.filter(activo=True,visible=True).order_by('-fechainicio')[:1]
                serializer = CausaSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Causa.DoesNotExist:
                return Response(data={"message": "HTTP_400_BAD_REQUEST"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset = Causa.objects.filter(visible=True).order_by('-fechainicio')[:5]
            serializer = CausaSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
