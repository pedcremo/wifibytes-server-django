# encoding:utf-8

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from empresa.serializers import EmpresaSerializer
from empresa.models import Empresa

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from wifibytes.authlib import *


class EmpresaAPIListView(APIView):

    def get(self, request, format=None):
        queryset = Empresa.objects.all()
        serializer = EmpresaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
