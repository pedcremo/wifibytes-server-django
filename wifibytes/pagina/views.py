# encoding:utf-8

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from pagina.serializers import *
from pagina.models import *

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from wifibytes.authlib import *
from django.http import HttpResponseRedirect, Http404
from wifibytes.configuracion_email import *

import requests
from ipaddress import ip_address, ip_network

#Get push event from git repository
class PushFromGitRepoAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        # Verify if request came from GitHub
        forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
        client_ip_address = ip_address(forwarded_for)
        whitelist = requests.get('https://api.github.com/meta').json()['hooks']

        for valid_ip in whitelist:
            if client_ip_address in ip_network(valid_ip):
                break
            else:
                return Response("Permission denied.", status=status.HTTP_403_FORBIDDEN)  
        return Response("hola caracola", status=status.HTTP_200_OK)  

class HomeAPIListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        queryset = Home.objects.all()
        serializer = HomeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FamiliaDescriptorAPIListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        queryset = FamiliaDescriptor.objects.all()
        serializer = FamiliaDescriptorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TarifaDescriptorAPIListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        queryset = TarifaDescriptorGenerico.objects.all()
        serializer = TarifaDescriptorGenericoSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class TxtContactoAPIListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        queryset = TxtContacto.objects.all()
        serializer = TxtContactoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PaletaColoresView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        queryset = PaletaColores.objects.all()
        serializer = PaletaColoresSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PaletaColoresDetailView(APIView):

    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return PaletaColores.objects.filter(pk=pk)
        except PaletaColores.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        paletacolores = self.get_object(pk)
        query = self.request.query_params

        serializer = PaletaColoresSerializer(paletacolores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Contacto(APIView):

    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        print("-----------------")
        print(request.data)
        print("-----------------")
        print(request.FILES)
        print("======================")
        query = request.data

        if 'nombre' in list(query.keys()):
            nombre = query['nombre']

        if 'telefono' in list(query.keys()):
            telefono = query['telefono']

        if 'email' in list(query.keys()):
            email = query['email']

        if 'descripcion' in list(query.keys()):
            descripcion = query['descripcion']

        # instancia de email
        email_instance = Email()

        if email_instance.sendemail_contacto(nombre, telefono, email, descripcion):
            message = 'Email Send'
            return Response(data={"message": message}, status=status.HTTP_200_OK)
        else:
            message = 'Error Send email'
            return Response(data={"message": message}, status=status.HTTP_400_BAD_REQUEST)
