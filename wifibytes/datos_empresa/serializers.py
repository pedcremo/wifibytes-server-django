# encoding:utf-8
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from wifibytes.functions import get_full_image_url
from django.conf import settings
from datos_empresa.models import DatosEmpresa, InfoEmpresa, Texto


class InfoEmpresaSerializer(ModelSerializer):
    lang = serializers.SerializerMethodField('_lang')
    image = serializers.SerializerMethodField('_image')

    def _lang(self, obj):
        if obj.idioma:
            return str(obj.idioma.codigo)
        else:
            return None

    def _image(self, obj):
        if obj.image:
            return str(settings.URL_WEB_BACK) + str(obj.image.url)
            return get_full_image_url(
                self.context['request'], obj.image.url)
        else:
            return None

    class Meta:
        model = InfoEmpresa
        fields = (
            'key', 'content', 'image', 'lang'
        )


class DatosEmpresaSerializer(ModelSerializer):
    logo = serializers.SerializerMethodField('_logo')
    icon_logo = serializers.SerializerMethodField('_icon_logo')
    mapa_cobertura = serializers.SerializerMethodField('_mapa_cobertura')
    facebook = serializers.SerializerMethodField('_facebook')
    twitter = serializers.SerializerMethodField('_twitter')
    textos = serializers.SerializerMethodField('_textos')

    def _logo(self, obj):
        if obj.logo:
            return get_full_image_url(
                self.context['request'], obj.logo.url)
        else:
            return None

    def _icon_logo(self, obj):
        if obj.icon_logo:
            return get_full_image_url(
                self.context['request'], obj.icon_logo.url)
        else:
            return None

    def _mapa_cobertura(self, obj):
        if obj.mapa_cobertura:
            return get_full_image_url(
                self.context['request'], obj.mapa_cobertura.url)
        else:
            return None

    def _facebook(self, obj):
        if obj.social_facebook:
            return str(obj.social_facebook)
        else:
            return None

    def _twitter(self, obj):
        if obj.social_twitter:
            return str(obj.social_twitter)
        else:
            return None

    def _textos(self, obj):
        if obj.textos:
            serializer = InfoEmpresaSerializer(
                obj.textos, many=True, read_only=True
            )
            return serializer.data
        else:
            return None

    class Meta:
        model = DatosEmpresa
        fields = (
            'name', 'cifnif', 'phone',
            'logo', 'icon_logo', 'mapa_cobertura',
            'address', 'city', 'province', 'country', 'zipcode',
            'location_lat', 'location_long',
            'facebook', 'twitter',
            'textos'
        )
class TextosContratoSerializer(ModelSerializer):
    
    class Meta:
        model = Texto
        depth = 0
        fields= '__all__'