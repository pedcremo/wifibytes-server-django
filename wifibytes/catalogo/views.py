# encoding:utf-8

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

import json
import datetime

from catalogo.serializers import *
from catalogo.models import *


class FiltrosView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):

        filters_dict = {}

        Marca_queryset = Marca.objects.all()
        Marca_serializer = MarcaSerializer(Marca_queryset, many=True)
        filters_dict['marca'] = Marca_serializer.data

        Pantalla_queryset = Pantalla.objects.all()
        Pantalla_serializer = PantallaSerializer(Pantalla_queryset, many=True)
        filters_dict['pantalla'] = Pantalla_serializer.data

        Procesador_queryset = Procesador.objects.all()
        Procesador_serializer = ProcesadorSerializer(
            Procesador_queryset, many=True)
        filters_dict['procesador'] = Procesador_serializer.data

        Ram_queryset = Ram.objects.all()
        Ram_serializer = RamSerializer(Ram_queryset, many=True)
        filters_dict['ram'] = Ram_serializer.data

        Camara_queryset = Camara.objects.all()
        Camara_serializer = CamaraSerializer(Camara_queryset, many=True)
        filters_dict['camara'] = Camara_serializer.data

        return Response(filters_dict, status=status.HTTP_200_OK)


class ArticuloViewSet(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Articulo.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ArticuloSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(activo=True)
        query = self.request.QUERY_PARAMS

        if 'destacado' in query.keys():
            queryset = queryset.filter(destacado=True)
            paginator = PageNumberPagination()
            queryset = paginator.paginate_queryset(queryset, request)

        if 'familia' in query.keys():
            familia = query['familia']
            queryset = queryset.filter(codfamilia__slug=familia)

        return queryset

    def get_serializer_context(self):
        query = self.request.QUERY_PARAMS
        if 'lang' in query.keys():
            lang = query['lang']
        else:
            lang = ''
        return {'lang': lang, 'request': self.request}


class FamiliaViewSet(viewsets.ModelViewSet):
    """
    API endpoint to View,Edit,Add, list products.
    """
    queryset = Familia.objects.all()
    permission_classes = [AllowAny]
    serializer_class = FamiliaSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return self.queryset

    def get_serializer_context(self):
        query = self.request.QUERY_PARAMS
        if 'lang' in query.keys():
            lang = query['lang']
        else:
            lang = ''
        return {'lang': lang, 'request': self.request}


class TarifaViewSet(viewsets.ModelViewSet):
    """
    API endpoint to View,Edit,Add, list products.
    """
    queryset = Tarifa.objects.all()
    permission_classes = [AllowAny]
    serializer_class = TarifaSerializer
    http_method_names = ['get']

    def get_queryset(self):
        query = self.request.QUERY_PARAMS
        queryset = self.queryset
        if 'destacado' in query.keys():
            queryset = queryset.filter(destacado=True)

        return queryset.filter(activo=True)

    def get_serializer_context(self):
        query = self.request.QUERY_PARAMS
        if 'lang' in query.keys():
            lang = query['lang']
        else:
            lang = ''
        return {'lang': lang, 'request': self.request}


# class TarifaView(APIView):
#     permission_classes = (AllowAny,)

#     def get(self, request, format=None):
#         query = self.request.QUERY_PARAMS

#         if 'destacado' in query.keys():
#             try:
#                 tarifas = Tarifa.objects.filter(destacado=True, activo=True)
#                 serializer = TarifaSerializer(tarifas, many=True)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except Tarifa.DoesNotExist:
#                 message = 'No hay tarifas destacadas'
#                 return Response(data={"message": message},
#                                 status=status.HTTP_400_BAD_REQUEST)

#         tarifas = Tarifa.objects.filter(activo=True)
#         serializer = TarifaSerializer(tarifas, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class TarifaDetailView(APIView):

    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Tarifa.objects.filter(pk=pk)
        except Tarifa.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tarifa = self.get_object(pk)
        serializer = TarifaSerializer(tarifa, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Template1APIListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        queryset = Template1.objects.all()
        serializer = Template1Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Template2APIListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        queryset = Template2.objects.all()
        serializer = Template2Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Template3APIListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        queryset = Template3.objects.all()
        serializer = Template3Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# VVVVVVVVVVVVVVVVVVVVVVVVVVVV

class ArticuloView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):

        query = self.request.QUERY_PARAMS

        if 'destacado' in query.keys():
            queryset = Articulo.objects.filter(destacado=True)
            paginator = PageNumberPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ArticuloSerializer(result_page, many=True,
                                            context={'lang': query.get('lang', ''),
                                                     'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        if 'familia' in query.keys():
            familia = query['familia']
            queryset = Articulo.objects.filter(codfamilia__slug=familia)
            if queryset.count() > 0:
                serializer = PaginatedArticleSerializer(
                    queryset, request, 8)
                return Response(serializer.data)
            else:
                return Response(
                    {'message': 'No hay articulos'},
                    status=status.HTTP_200_OK)

        queryset = Articulo.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(queryset, request)

        serializer = ArticuloSerializer(result_page, many=True,
                                        context={'lang': query.get('lang', ''),
                                                 'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticuloDetailView(APIView):

    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Articulo.objects.filter(pk=pk)
        except Articulo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        articulo = self.get_object(pk)

        serializer = ArticuloSerializer(articulo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
