# -*- coding: utf-8 -*-
import csv
import os
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db.models import Q
from datetime import datetime
from django.utils.dateformat import format
from django.http import HttpResponse
from wifibytes.utils import intorzero
from geo.models import Provincia
from catalogo.models import Tarifa
from geo.models import Pais, Provincia


class Command(BaseCommand):

    help = "That's Your help message"

    option_list = BaseCommand.option_list + (
        make_option('--myoption', action='store',
                    dest='myoption',
                    default='default',
                    help='Option help message'),
    )

    def handle(self, *app_labels, **options):

        if options['myoption'] == 'default':

            # --- PAISES --- #
            path = settings.MEDIA_URL+'csv/to_import/eneboo_paises.csv'
            reader = csv.DictReader(open(path))

            result = {}
            for row in reader:
                for column, value in row.iteritems():
                    if value == 'None':
                        value = None
                    result.setdefault(column, []).append(value)

            print "\n---> Importando paises\n"
            for i in range(len(result['codpais'])):

                try:
                    pais = Pais.objects.get(pk=result['codpais'][i])
                except Pais.DoesNotExist:
                    pais = Pais()
                except Exception as msg:
                    print "Error al buscar el pais -> %s" % (
                        msg)

                pais.codpais = result['codpais'][i]
                pais.codiso = result['codiso'][i]
                pais.nombre = result['nombre'][i]

                try:
                    pais.save()
                except Exception as msg:
                    print u"ERROR Importando País (%s) -> %s" % (
                        result['codpais'][i], msg)

            # --- PROVINCIAS --- #
            path = settings.MEDIA_URL+'csv/to_import/eneboo_provincias.csv'
            reader = csv.DictReader(open(path))

            result = {}
            for row in reader:
                for column, value in row.iteritems():
                    result.setdefault(column, []).append(value)

            print "\n---> Importando provincias\n"
            for i in range(len(result['idprovincia'])):
                try:
                    provincia = Provincia.objects.get(
                        pk=result['idprovincia'][i]
                    )
                except Provincia.DoesNotExist:
                    provincia = Provincia()

                provincia.idprovincia = result['idprovincia'][i]
                provincia.provincia = result['provincia'][i]
                provincia.codigo = result['codigo'][i]

                try:
                    pais = Pais.objects.get(pk=result['codpais'][i])
                    provincia.codpais = pais
                except Pais.DoesNotExist:
                    print u"ERROR Importando provincia (%s) -> %s" % (
                        result['codpais'][i], 'El pais no existe')

                try:
                    provincia.save()
                except Exception as msg:
                    print "ERROR Importando provincia (%s) -> %s" % (
                        result['idprovincia'][i], msg)

            return "\n--->  Script Importar Geo finalizado \n"

        raise CommandError('Only the default is supported')
