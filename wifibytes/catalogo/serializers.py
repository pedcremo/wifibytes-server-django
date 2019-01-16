# encoding:utf-8

from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SerializerMethodField
from catalogo.models import *
from pagina.serializers import *
from pagina.models import *
from rest_framework import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from wifibytes.functions import get_full_image_url


class ArticuloSerializer(ModelSerializer):

    templates = SerializerMethodField()
    descripcion = serializers.SerializerMethodField('get_descripcion_i18')
    descripcion_breve = serializers.SerializerMethodField('get_descripcion_breve_i18')
    descripcion_larga = serializers.SerializerMethodField('get_descripcion_larga_i18')
    imagen = serializers.SerializerMethodField('get_imagen_url')
    thumbnail = serializers.SerializerMethodField('get_thumbnail_url')

    class Meta:
        model = Articulo
        depth = 0

    def get_templates(self, obj):

        return_dict = {}
        try:
            lang = self.context['lang']
            if lang == '' or lang is None:
                lang = 'es'
        except Exception as error:
            print(error)
            lang = 'es'

        try:
            templates1 = Template1.objects.filter(
                articulo=obj.referencia, idioma__codigo=lang).first()
            return_dict['template1'] = Template1Serializer(templates1).data
        except Template1.DoesNotExist:
            print('No match')

        try:
            templates2 = Template2.objects.filter(
                articulo=obj.referencia, idioma__codigo=lang).first()
            return_dict['template2'] = Template2Serializer(templates2).data
        except Template2.DoesNotExist:
            print('No match')

        try:
            templates3 = Template3.objects.filter(
                articulo=obj.referencia, idioma__codigo=lang).first()
            return_dict['template3'] = Template3Serializer(templates3).data
        except Template3.DoesNotExist:
            print('No match')

        return return_dict

    # absolute image url
    def get_imagen_url(self, obj):
        if obj.imagen:
            return get_full_image_url(
                self.context['request'], obj.imagen.url)
        else:
            return None

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            return get_full_image_url(
                self.context['request'], obj.thumbnail.url)
        else:
            return None

    # check lang and select correct field
    def check_fields_i18(self, obj, param):
        field = "%s_%s" % (param, self.context.get('lang', ''))
        if not field in obj.__dict__:
            field = param
        return getattr(obj, field)

    ####### get fields i18 #########
    def get_descripcion_i18(self, obj):
        return self.check_fields_i18(obj, "descripcion")

    def get_descripcion_breve_i18(self, obj):
        return self.check_fields_i18(obj, "descripcion_breve")

    def get_descripcion_larga_i18(self, obj):
        return self.check_fields_i18(obj, "descripcion_larga")


class PaginatedArticleSerializer():
    def __init__(self, articles, request, num):
        paginator = Paginator(articles, num)
        page = request.QUERY_PARAMS.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        count = paginator.count

        previous = None if not articles.has_previous() else articles.previous_page_number()
        next = None if not articles.has_next() else articles.next_page_number()
        serializer = ArticuloSerializer(articles, many=True, context={
            'lang': request.QUERY_PARAMS.get('lang', ''), 'request': request})
        self.data = {'count': count, 'previous': previous,
                     'next': next, 'results': serializer.data}


class FamiliaSerializer(ModelSerializer):
    nombre = serializers.SerializerMethodField('get_nombre_i18')
    pretitulo = serializers.SerializerMethodField('get_pretitulo_i18')
    titulo = serializers.SerializerMethodField('get_titulo_i18')
    texto_cabecera = serializers.SerializerMethodField('get_texto_cabecera_i18')
    subtexto_cabecera = serializers.SerializerMethodField('get_subtexto_cabecera_i18')
    icono = serializers.SerializerMethodField('get_icon_url')
    thumbnail = serializers.SerializerMethodField('get_thumbnail_url')
    imagen_cabecera = serializers.SerializerMethodField('get_imagen_cabecera_url')

    class Meta:
        model = Familia
        depth = 1
        fields = ('codfamilia', 'slug', 'nombre', 'color', 'icono',
                  'pretitulo', 'titulo', 'precio_cabecera',
                  'imagen_cabecera', 'thumbnail', 'texto_cabecera',
                  'subtexto_cabecera')
        # excluded: 'activo', 'created_at', 'updated_at'
        # supported langs: es, va
        # fields_i18: nombre_*, pretitulo_*, titulo_*, texto_cabecera_*,
        #         subtexto_cabecera_*

    def get_icon_url(self, obj):
        if obj.icono:
            return get_full_image_url(
                self.context['request'], obj.icono.url)
        else:
            return None

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            return get_full_image_url(
                self.context['request'], obj.thumbnail.url)
        else:
            return None

    def get_imagen_cabecera_url(self, obj):
        if obj.imagen_cabecera:
            return get_full_image_url(
                self.context['request'], obj.imagen_cabecera.url)
        else:
            return None

    # check lang and select correct field
    def check_fields_i18(self, obj, param):
        field = "%s_%s" % (param, self.context.get('lang', ''))
        if not field in obj.__dict__:
            field = param
        return getattr(obj, field)

    ####### get fields i18 #########
    def get_nombre_i18(self, obj):
        return self.check_fields_i18(obj, "nombre")

    def get_pretitulo_i18(self, obj):
        return self.check_fields_i18(obj, "pretitulo")

    def get_titulo_i18(self, obj):
        return self.check_fields_i18(obj, "titulo")

    def get_texto_cabecera_i18(self, obj):
        return self.check_fields_i18(obj, "texto_cabecera")

    def get_subtexto_cabecera_i18(self, obj):
        return self.check_fields_i18(obj, "subtexto_cabecera")


class SubtarifaSerializer(ModelSerializer):
    class Meta:
        model = Subtarifa
        depth = 1
        fields = ('subtarifa_id', 'subtarifa_datos_internet',
                  'subtarifa_cent_minuto', 'subtarifa_est_llamada',
                  'subtarifa_precio_sms', 'subtarifa_minutos_gratis',
                  'subtarifa_minutos_ilimitados',
                  'subtarifa_velocidad_conexion_subida',
                  'subtarifa_velocidad_conexion_bajada',
                  'subtarifa_num_canales', 'subtarifa_siglas_omv',
                  'subtarifa_omv', 'tipo_tarifa', 'subtarifa_tarifa')


class TarifaSerializer(ModelSerializer):
    pretitulo = serializers.SerializerMethodField('get_pretitulo_i18')
    logo = serializers.SerializerMethodField('get_logo_url')
    subtarifas = serializers.SerializerMethodField('getSubtarifas')

    class Meta:
        model = Tarifa
        depth = 1
        fields = ('codtarifa', 'nombretarifa', 'slug', 'pretitulo', 'logo',
                  'precio', 'activo', 'destacado', 'color', 'subtarifas')
        # supported langs: es, va
        # fields_i18: pretitulo_*

    def getSubtarifas(self, obj):
        if hasattr(obj, 'subtarifa_tarifa'):
            items = obj.subtarifa_tarifa
            serializer = SubtarifaSerializer(items, many=True,
                                             read_only=True)
            return serializer.data
        else:
            return None

    def get_logo_url(self, obj):
        try:
            if obj.logo:
                return get_full_image_url(
                    self.context['request'], obj.logo.url)
            else:
                return None
        except Exception as error:
            return None

    # check lang and select correct field
    def check_fields_i18(self, obj, param):
        field = "%s_%s" % (param, self.context.get('lang', ''))
        if not field in obj.__dict__:
            field = param
        return getattr(obj, field)

    ####### get fields i18 #########
    def get_pretitulo_i18(self, obj):
        return self.check_fields_i18(obj, "pretitulo")


class MarcaSerializer(ModelSerializer):

    class Meta:
        model = Marca
        depth = 0


class PantallaSerializer(ModelSerializer):

    class Meta:
        model = Pantalla
        depth = 0


class ProcesadorSerializer(ModelSerializer):

    class Meta:
        model = Procesador
        depth = 0


class RamSerializer(ModelSerializer):

    class Meta:
        model = Ram
        depth = 0


class CamaraSerializer(ModelSerializer):

    class Meta:
        model = Camara
        depth = 0


class Template1Serializer(ModelSerializer):

    class Meta:
        model = Template1
        depth = 0


class Template2Serializer(ModelSerializer):

    class Meta:
        model = Template2
        depth = 0


class Template3Serializer(ModelSerializer):

    class Meta:
        model = Template3
        depth = 0
