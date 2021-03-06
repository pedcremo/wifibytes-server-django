# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

from rest_framework.views import APIView

from datos_empresa.models import DatosEmpresa, Texto
from datos_empresa.serializers import DatosEmpresaSerializer, TextosContratoSerializer

class DatosEmpresaViewSet(viewsets.ModelViewSet):
    queryset = DatosEmpresa.objects.all()
    serializer_class = DatosEmpresaSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get']

    def get_serializer_context(self):
        query = self.request.query_params
        if 'lang' in list(query.keys()):
            lang = query['lang']
        else:
            lang = ''
        return {'lang': lang, 'request': self.request}

    def list(self, request):
        # print self.get_serializer_context(self)
        queryset = self.queryset.filter(datos_empresa_default=True).first()
        serializer = DatosEmpresaSerializer(
            queryset, many=False, context={'request': request}
        )
        return Response(serializer.data)

class TextosContratoListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):
        queryset = Texto.objects.all()        
        serializer = TextosContratoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)