# encoding:utf-8
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from pagina.models import *
from wifibytes.functions import get_full_image_url


class HomeSerializer(ModelSerializer):

    lang = serializers.SerializerMethodField('_lang')

    def _lang(self, obj):
        if obj.idioma:
            return str(obj.idioma.codigo)
        return None

    class Meta:
        model = Home
        depth = 0
        fields = (
            'pk', 'titulo', 'subtitulo',
            'caja_izquierda_titulo', 'caja_izquierda_texto',
            'caja_derecha_titulo', 'caja_derecha_texto',
            'activo', 'idioma', 'lang'
        )


class PaletaColoresSerializer(ModelSerializer):

    class Meta:
        model = PaletaColores
        depth = 0
        fields = '__all__'


class TarifaDescriptorGenericoSerializer(ModelSerializer):

    caja_1_icono = SerializerMethodField('get_caja_1_icono_url')
    caja_2_icono = SerializerMethodField('get_caja_2_icono_url')
    caja_3_icono = SerializerMethodField('get_caja_3_icono_url')
    caja_4_icono = SerializerMethodField('get_caja_4_icono_url')

    lang = serializers.SerializerMethodField('_lang')

    def _lang(self, obj):
        if obj.idioma:
            return str(obj.idioma.codigo)
        return None
    
    def get_image(self, image):
        if image:
            return get_full_image_url(
                self.context['request'], image.url)
        else:
            return None

    def get_caja_1_icono_url(self, obj):
        return self.get_image(obj.caja_1_icono)

    def get_caja_2_icono_url(self, obj):
        return self.get_image(obj.caja_2_icono)

    def get_caja_3_icono_url(self, obj):
        return self.get_image(obj.caja_3_icono)

    def get_caja_4_icono_url(self, obj):
        return self.get_image(obj.caja_4_icono)

    class Meta:
        model = TarifaDescriptorGenerico
        depth = 0
        fields = '__all__'


class TxtContactoSerializer(ModelSerializer):

    class Meta:
        model = TxtContacto
        depth = 0
        fields = '__all__'