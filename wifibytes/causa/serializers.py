# encoding:utf-8

from rest_framework.serializers import ModelSerializer
from causa.models import Causa


class CausaSerializer(ModelSerializer):

    class Meta:
    	#fields = ('codcausa', 'nombre', 'descripcion', 'thumbnail_url', 'fechainicio', 'visible', 'recaudacion', 'activo', 'valido_altrebit')
        model = Causa
        depth = 0
        fields = '__all__'