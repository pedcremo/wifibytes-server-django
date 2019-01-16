# -*- coding: utf-8 -*-
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from catalogo.models import (
    Articulo,
    Familia,
    Marca
)
from pagina.models import PaletaColores
from django.conf import settings
from datetime import datetime
from django.utils.dateformat import format
import csv
import os

# Class MUST be named 'Command'


class Command(BaseCommand):

    help = "That's Your help message"

    option_list = BaseCommand.option_list + (
        make_option('--myoption', action='store',
                    dest='myoption',
                    default='default',
                    help='Option help message'),
    )

    def handle(self, *app_labels, **options):
        """
        app_labels - app labels (eg. myapp in "manage.py reset myapp")
        options - configurable command line options
        """

        if options['myoption'] == 'default':
            now = int(format(datetime.now(), 'U'))
            before = now - 86400

            # ------------------------------------------------------------
            # Familias
            # ------------------------------------------------------------
            print("Importando familias")

            path = settings.MEDIA_URL+'csv/to_import/eneboo_familias.csv'
            reader = csv.DictReader(open(path))

            # Guardar Datos en diccionario
            result = {}
            for row in reader:
                for column, value in row.items():
                    if value == 'None':
                        value = None
                    result.setdefault(column, []).append(value)

            for i in range(len(result['codfamilia'])):
                try:
                    familia = Familia.objects.get(pk=result['codfamilia'][i])
                except Familia.DoesNotExist:
                    familia = Familia()
                    familia.codfamilia = result['codfamilia'][i]

                familia.nombre = result['descripcion'][i]
                familia.save()
                # print "Importado Familia codfamilia => ", result['codfamilia'][i]

            print("Familias importadas")
            print("Importando articulos")
            # ------------------------------------------------------------
            # Articulos
            # ------------------------------------------------------------
            path = settings.MEDIA_URL+'csv/to_import/eneboo_articulos.csv'
            reader = csv.DictReader(open(path))

            # Guardar Datos en diccionario
            result = {}
            for row in reader:
                for column, value in row.items():
                    if value == 'None':
                        value = None
                    result.setdefault(column, []).append(value)

            for i in range(len(result['referencia'])):
                try:
                    articulo = Articulo.objects.get(pk=result['referencia'][i])
                except Articulo.DoesNotExist:
                    # Campos por defecto no null
                    articulo = Articulo()
                    articulo.referencia = result['referencia'][i]
                    articulo.template = 1
                    # articulo.marca = Marca.objects.filter()[:1].get()

                articulo.descripcion = result['descripcion'][i]
                articulo.secompra = result['secompra'][i]
                articulo.pvp = 0
                if result['pvp'][i]:
                    articulo.pvp = result['pvp'][i]
                articulo.stockfis = 0
                if result['stockfis'][i]:
                    articulo.stockfis = result['stockfis'][i]
                articulo.stockmax = 0
                if result['stockmax'][i]:
                    articulo.stockmax = result['stockmax'][i]
                articulo.stockmin = 0
                if result['stockmin'][i]:
                    articulo.stockmin = result['stockmin'][i]
                articulo.codimpuesto = result['codimpuesto'][i]
                articulo.observaciones = result['observaciones'][i]
                articulo.codbarras = result['codbarras'][i]
                articulo.nostock = result['nostock'][i]
                articulo.controlstock = result['controlstock'][i]
                articulo.tipocodbarras = result['tipocodbarras'][i]
                articulo.sevende = result['sevende'][i]
                articulo.venta_online = result['venta_online'][i]
                if result['venta_online'][i] is None:
                    articulo.venta_online = False

                # Comprobar familia
                try:
                    articulo.codfamilia = Familia.objects.get(
                        pk=result['codfamilia'][i]
                    )
                except Familia.DoesNotExist:
                    pass

                articulo.save()
                # print "Importado Articulo referencia => ", result['referencia'][i]

            print('Total Articulos => ', len(result['referencia']))

            elapsed = int(format(datetime.now(), 'U')) - now
            return "Importación terminada - %ss" % elapsed

        raise CommandError('Only the default is supported')
