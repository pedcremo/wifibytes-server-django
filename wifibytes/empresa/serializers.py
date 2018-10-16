# encoding:utf-8

from rest_framework.serializers import ModelSerializer
from empresa.models import Empresa


class EmpresaSerializer(ModelSerializer):

    class Meta:
        model = Empresa
        depth = 0
