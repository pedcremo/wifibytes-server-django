# encoding:utf-8

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework import pagination

from facturacion.models import *
from catalogo.serializers import ArticuloSerializer
from django.conf import settings


class FormaspagoSerializer(ModelSerializer):
    nombre = serializers.SerializerMethodField('get_nombre_i18')
    descripcion = serializers.SerializerMethodField('get_descripcion_i18')

    class Meta:
        model = FormasPago
        depth = 0
        fields = ('codpago', 'nombre', 'descripcion', 'cod_eneboo','activa')
        # supported langs: es, va
        # fields_i18: nombre_*, descripcion_*
        # exclude: activa

    # check lang and select correct field
    def check_fields_i18(self, obj, param):
        lang = self.context.get('lang', '')
        field = "%s_%s" % (param, lang)
        if not field in obj.__dict__:
            field = param
        return getattr(obj, field)

    ####### get fields i18 #########
    def get_nombre_i18(self, obj):
        return self.check_fields_i18(obj, "nombre")

    def get_descripcion_i18(self, obj):
        return self.check_fields_i18(obj, "descripcion")


class LineaspedidoscliSerializer(ModelSerializer):

    def get_context(self):
        return self.context

    referencia = ArticuloSerializer(context=get_context)

    class Meta:
        model = LineaPedidoCli
        depth = 1
        exclude = ('idpedido',)


class PedidoscliSerializer(ModelSerializer):

    totalLineas = serializers.SerializerMethodField('get_total_lines')
    lineas = serializers.SerializerMethodField('get_lines')
    estadoText = serializers.SerializerMethodField('get_estado')
    estadoClass = serializers.SerializerMethodField('get_estado_class')

    def get_total_lines(self, obj):
        totalitems = LineaPedidoCli.objects.filter(idpedido=obj).count()
        return totalitems

    def get_lines(self, obj):
        lineas = LineaPedidoCli.objects.filter(idpedido=obj)
        serializer = LineaspedidoscliSerializer(
            lineas, many=True, read_only=True, context=self.context)
        return serializer.data

    def get_estado(self, obj):
        if(obj.estado == 0):
            return "En proceso"
        elif(obj.estado == 1):
            return "Enviado"
        elif(obj.estado == 2):
            return "Entregado"
        else:
            return "Cancelado"

    def get_estado_class(self, obj):
        if(obj.estado == 0):
            return "enproceso"
        elif(obj.estado == 1):
            return "enviado"
        elif(obj.estado == 2):
            return "entregado"
        else:
            return "cancelado"

    class Meta:
        fields = ('idpedido', 'fecha', 'total', 'nombrecliente', 'cifnif',
                  'direccion', 'provincia', 'ciudad', 'codpostal',
                  'direccionEnvio', 'ciudadEnvio', 'codpostalEnvio',
                  'provinciaEnvio', 'total', 'observaciones', 'fecha',
                  'formaEnvio', 'formaPago', 'estadoText', 'estadoClass',
                  'lineas', 'totalLineas', 'pagado', 'codpais', 'nombreclienteFacturacion', 'cifnifFacturacion')
        model = PedidoCli
        depth = 1


class ImpuestosSerializer(ModelSerializer):

    class Meta:
        model = Impuesto
        depth = 0


class FormasEnvioSerializer(serializers.ModelSerializer):
    nombre = serializers.SerializerMethodField('get_nombre_i18')
    descripcion = serializers.SerializerMethodField('get_descripcion_i18')

    class Meta:
        model = FormasEnvio
        depth = 0
        fields = ('idEnvio', 'nombre', 'descripcion', 'precio')
        # supported langs: es, va
        # fields_i18: nombre_*, descripcion_*

    # check lang and select correct field
    def check_fields_i18(self, obj, param):
        lang = self.context.get('lang', '')
        field = "%s_%s" % (param, lang)
        if not field in obj.__dict__:
            field = param
        return getattr(obj, field)

    ####### get fields i18 #########
    def get_nombre_i18(self, obj):
        return self.check_fields_i18(obj, "nombre")

    def get_descripcion_i18(self, obj):
        return self.check_fields_i18(obj, "descripcion")


class LineasFacturascliSerializer(ModelSerializer):

    class Meta:
        model = lineasfacturascli
        depth = 0


class FacturascliSerializer(ModelSerializer):
    lineas = serializers.SerializerMethodField('get_lines')
    factura_pdf = serializers.SerializerMethodField('_factura_pdf')

    def get_total_lines(self, obj):
        totalitems = lineasfacturascli.objects.filter(idfactura=obj).count()
        return totalitems

    def get_lines(self, obj):
        lineas = lineasfacturascli.objects.filter(idfactura=obj)
        serializer = LineasFacturascliSerializer(
            lineas, many=True, read_only=True)
        return serializer.data

    def _factura_pdf(self, obj):
        url = settings.URL_WEB_BACK + 'facturapdf/' + str(obj.pk)
        return url

    class Meta:
        # Definir mas campos
        fields = ('idfactura', 'codigo', 'numero', 'totaleuros', 'hora',
                  'direccion', 'codpago', 'codejercicio', 'total',
                  'ciudad', 'codpostal', 'automatica', 'nombrecliente',
                  'observaciones', 'codcliente', 'totaliva',
                  'fecha', 'lineas', 'factura_pdf')
        model = facturasCli
        depth = 0
