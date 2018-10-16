# encoding:utf-8

from rest_framework import viewsets
from .models import Provincia
from .serializers import ProvinciaSerializer
from wifibytes.functions import LargeResultsSetPagination
from rest_framework.response import Response
# from django.utils.dateformat import format
# from datetime import datetime, timedelta


class ProvinciaViewSet(viewsets.ModelViewSet):

    """
    API endpoint to View,Edit,Add, list Provinces.
    """
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    # pagination_class = LargeResultsSetPagination
    # paginate_by = 50

    def list(self, request):
        queryset = self.queryset.order_by('provincia')
        serializer = ProvinciaSerializer(queryset, many=True)
        return Response({'results': serializer.data,
                         'count': len(serializer.data)})

    def get_queryset(self):
        query = self.request.QUERY_PARAMS
        queryset = self.queryset
        return queryset.order_by('provincia')
