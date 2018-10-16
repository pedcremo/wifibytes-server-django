# encoding:utf-8
from rest_framework import serializers
from .models import Pais, Comunidad, Provincia


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('codpais', 'bandera', 'validarprov', 'codiso', 'nombre')


class ProvinciaSerializer(serializers.ModelSerializer):
    # pais = serializers.SerializerMethodField('paises')
    #
    # def paises(self, obj):
    #     if obj.codpais:
    #         items = Pais.objects.get(
    #             pk=obj.codpais.pk)
    #         serializer = PaisSerializer(
    #             items, many=False, read_only=True)
    #         return serializer.data
    #     else:
    #         return None

    class Meta:
        model = Provincia
        fields = ('idprovincia', 'provincia', 'codpais',  # 'pais',
                  'codcomunidad', 'codigo')
