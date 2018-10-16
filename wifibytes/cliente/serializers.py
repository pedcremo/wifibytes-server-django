# encoding:utf-8

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer
from cliente.models import *
from geo.models import Provincia
from geo.serializers import ProvinciaSerializer
from catalogo.serializers import TarifaSerializer


class DireccionesSerializer(ModelSerializer):
    provincia_info = serializers.SerializerMethodField('provincia')

    def provincia(self, obj):
        if obj.idprovincia:
            serializer = ProvinciaSerializer(
                obj.idprovincia, many=False, read_only=True)
            return serializer.data
        else:
            return None

    class Meta:
        model = DirClientes
        fields = (
            'id', 'codcliente', 'domenvio', 'domfacturacion', 'nombre',
            'cifnif', 'direccion', 'codpais', 'ciudad', 'provincia',
            'codpostal', 'apartado', 'telefono', 'numero', 'idprovincia',
            'provincia_info', 'default')


class ClienteSerializer(ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('codcliente', 'nombre', 'apellido', 'segundo_apellido',
                  'telefono', 'cifnif', 'email', 'nombrecomercial', 'genero',
                  'tipo_cliente', 'password', 'consumerSigned', 'newsletter',
                  'is_active', 'cifnif_imageA', 'tipo_documento',
                  'birthday_omv', 'token')
        extra_kwargs = {'password': {'write_only': True},
                        'cifnif_imageA': {'write_only': True},
                        'is_active': {'write_only': True},
                        'token': {'write_only': True}}

        read_only_fields = ('codcliente')
        # consumerContract


class LineaSerializer(ModelSerializer):
    client_info = serializers.SerializerMethodField('client')
    address_info = serializers.SerializerMethodField('address')
    account_info = serializers.SerializerMethodField('account')
    tarifa_info = serializers.SerializerMethodField('tarifa')
    buzon_voz_info = serializers.SerializerMethodField('buzon_voz')
    roaming_info = serializers.SerializerMethodField('roaming')

    def roaming(self, obj):
        return {
            'value': obj.roaming,
            'status': obj.roaming_procesing
        }

    def buzon_voz(self, obj):
        return {
            'value': obj.buzon_voz,
            'status': obj.buzon_voz_procesing
        }

    def client(self, obj):
        if obj.codcliente:
            serializer = ClienteSerializer(
                obj.codcliente, many=False, read_only=True)
            return serializer.data
        else:
            return None

    def address(self, obj):
        if obj.coddir:
            serializer = DireccionesSerializer(
                obj.coddir, many=False, read_only=True)
            return serializer.data
        else:
            return None

    def account(self, obj):
        if obj.codcuenta:
            serializer = CuentaSerializer(
                obj.codcuenta, many=False, read_only=True)
            return serializer.data
        else:
            return None

    def tarifa(self, obj):
        if obj.codtarifa:
            serializer = TarifaSerializer(
                obj.codtarifa, many=False, read_only=True,
                context=self.context)
            return serializer.data
        else:
            return None

    class Meta:
        model = MobilsClients
        fields = (
            'id_mobilsclients', 'mobil', 'codcliente', 'dc_icc_anterior',
            'codtarifa', 'roaming', 'coddir', 'tipoTarifaAntigua',
            'tipoSim', 'companiaAnterior', 'icc_anterior', 'origen',
            'activa', 'alta', 'codcuenta', 'draft', 'client_info',
            'address_info', 'account_info', 'tarifa_info',
            'buzon_voz_info', 'roaming_info'
        )
        depth = 0


class CuentaSerializer(ModelSerializer):

    class Meta:
        model = CuentasbcoCli
        fields = ('codcuenta', 'codcliente', 'iban', 'codiban', 'ctaentidad',
                  'ctaagencia', 'ctadc', 'cuenta', 'entidad', 'codigocuenta',
                  'bic', 'codpais', 'titular')


class ServicioSerializer(ModelSerializer):
    client_info = serializers.SerializerMethodField('client')
    address_info = serializers.SerializerMethodField('address')
    account_info = serializers.SerializerMethodField('account')

    def client(self, obj):
        if obj.servicio_consumer:
            serializer = ClienteSerializer(
                obj.servicio_consumer, many=False, read_only=True)
            return serializer.data
        else:
            return None

    def address(self, obj):
        if obj.servicio_direccion:
            serializer = DireccionesSerializer(
                obj.servicio_direccion, many=False, read_only=True)
            return serializer.data
        else:
            return None

    def account(self, obj):
        if obj.servicio_cuenta:
            serializer = CuentaSerializer(
                obj.servicio_cuenta, many=False, read_only=True)
            return serializer.data
        else:
            return None

    class Meta:
        model = Servicio
        depth = 0
        fields = ('servicio_id', 'servicio_compania_anterior',
                  'servicio_telefono_anterior', 'servicio_draft',
                  'servicio_activo', 'servicio_consumer', 'servicio_direccion',
                  'servicio_tarifa', 'servicio_cuenta', 'client_info',
                  'address_info', 'account_info')


# VVVVVVVVVVVVVV


class cuentasbcocliSerializer(ModelSerializer):

    class Meta:
        model = CuentasbcoCli
        depth = 0


class dirclientesSerializer(ModelSerializer):
    provincia_info = serializers.SerializerMethodField('provincia')

    def provincia(self, obj):
        if obj.idprovincia:
            serializer = ProvinciaSerializer(obj.idprovincia, many=False,
                                             read_only=True)
            return serializer.data
        else:
            return None

    class Meta:
        fields = (
            'id', 'codcliente', 'domenvio', 'domfacturacion', 'nombre',
            'cifnif', 'direccion', 'codpais', 'ciudad', 'provincia',
            'codpostal', 'apartado', 'telefono', 'numero', 'idprovincia',
            'provincia_info')
        model = DirClientes
        depth = 0


class mobilsclientsSerializer(ModelSerializer):
    codtarifa_info = serializers.SerializerMethodField('codtarifa')
    roaming_info = serializers.SerializerMethodField('roaming')
    buzon_voz_info = serializers.SerializerMethodField('buzon_voz')

    def codtarifa(self, obj):
        if obj.codtarifa:
            serializer = TarifaSerializer(
                obj.codtarifa, many=False, read_only=True
            )
            return serializer.data
        else:
            return None

    def roaming(self, obj):
        return {
            'value': obj.roaming,
            'status': obj.roaming_procesing
        }

    def buzon_voz(self, obj):
        return {
            'value': obj.buzon_voz,
            'status': obj.buzon_voz_procesing
        }

    class Meta:
        fields = (
            'id_mobilsclients', 'mobil', 'nuevoicc', 'codcliente', 'codcuenta',
            'codtarifa', 'codtarifa_info', 'fechaContrato', 'imageContrato',
            'roaming', 'roaming_info', 'buzon_voz', 'buzon_voz_info',
            'coddir', 'origen', 'tipoTarifaAntigua', 'tipoSim',
            'companiaAnterior', 'icc_anterior', 'dc_icc_anterior',
            'activa', 'alta', 'omv_solicitud', 'signature_id',
            'document_id', 'created_at', 'updated_at', 'draft'
        )
        model = MobilsClients
        depth = 2


class ClienteSerializerGet(ModelSerializer):

    class Meta:
        fields = ('nombre', 'apellido', 'segundo_apellido', 'cifnif',
                  'email', 'newsletter')
        model = Cliente


# class ClienteSerializer(ModelSerializer):
#
#     class Meta:
#         fields = (
#             'nombre', 'apellido', 'segundo_apellido', 'cifnif', 'email',
#             'password', 'newsletter')
#         model = Cliente


class ClienteListSerializer(HyperlinkedModelSerializer):

    direcciones = serializers.SerializerMethodField('get_status2')

    def get_status2(self, obj):
        items = DirClientes.objects.filter(codcliente=obj.codcliente)
        serializer = dirclientesSerializer(items, many=True, read_only=True)
        return serializer.data

    cuentas = serializers.SerializerMethodField('get_status3')

    def get_status3(self, obj):
        items = CuentasbcoCli.objects.filter(codcliente=obj.codcliente)
        serializer = cuentasbcocliSerializer(items, many=True, read_only=True)
        return serializer.data

    mobils = serializers.SerializerMethodField('get_status4')

    def get_status4(self, obj):
        items = MobilsClients.objects.filter(codcliente=obj.codcliente)
        serializer = mobilsclientsSerializer(items, many=True, read_only=True)
        return serializer.data

    class Meta:
        fields = ('codcliente', 'nombre', 'apellido', 'segundo_apellido',
                  'telefono', 'cifnif', 'email', 'nombrecomercial', 'cuentas',
                  'direcciones', 'mobils', 'consumerContract', 'tipo_cliente',
                  'consumerSigned', 'newsletter', 'is_active', 'password',
                  'tipo_documento', 'birthday_omv')
        model = Cliente
        extra_kwargs = {'password': {'write_only': True}}
