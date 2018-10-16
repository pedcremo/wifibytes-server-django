__author__ = 'wearecactus'
import os
import ast
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from cliente.models import Cliente

os.environ['DJANGO_SETTINGS_MODULE'] = 'wifibytes.settings.local'


def cliente_token(id_cliente, token):
    try:
        token = str(token.split(' ')[1])
    except Exception:
        return Response(data={"message": 'Invalid Signature'},
                        status=status.HTTP_401_UNAUTHORIZED)
    try:
        cliente = Cliente.objects.get(pk=str(id_cliente))
        if cliente.token == token:
            if cliente.is_active:
                return cliente
            else:
                return Response(data={"message": 'Inactive Client'},
                                status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(data={"message": 'Unauthorized token'},
                            status=status.HTTP_401_UNAUTHORIZED)
    except Cliente.DoesNotExist:
        return Response(data={"message": "Client does not exist"},
                        status=status.HTTP_404_NOT_FOUND)
