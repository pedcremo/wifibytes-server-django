# encoding:utf-8

from rest_framework.serializers import ModelSerializer
from omv.models import Omv


class OmvSerializer(ModelSerializer):

    class Meta:
        model = Omv
        depth = 0
