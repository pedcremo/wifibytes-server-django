# -*- coding: utf-8 -*-
import csv
import os
from optparse import make_option
from django.conf import settings
from datetime import datetime
from django.utils.dateformat import format
from django.http import HttpResponse
from django.core.management.base import(
    BaseCommand,
    CommandError,
)
from catalogo.models import (
    Articulo,
    Familia,
)

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
            try:
                os.mkdir(os.path.join(settings.MEDIA_URL, 'csv'))
            except:
                pass

            now = int(format(datetime.now(), 'U'))
            before = now - 86400
            articulos = Articulo.objects.all()

            outfile_path = os.path.join(
                settings.MEDIA_URL, 'csv', "to_export/articulos.csv")

            outfile = open(outfile_path, 'wb')
            writer = csv.writer(outfile)
            writer.writerow([
                'temps_burst_pujada', 'secompra', 'pvp', 'pujada_maxima',
                'stockfis', 'baixada_maxima', 'codsubcuentairpfcom',
                'stockmax', 'descripcion', 'imagen', 'baixada_limitada',
                'codimpuesto', 'observaciones', 'idsubcuentacom', 'codbarras',
                'nostock', 'controlstock', 'temps_burst_baixada',
                'tipocodbarras', 'sevende', 'costemedio', 'venta_online',
                'pujada_burst_limit', 'baixada_burst_limit', 'pujada_limitada',
                'stockmin', 'codsubcuentacom', 'codfamilia', 'referencia'
            ])

            for articulo in articulos:
                temps_burst_pujada = None
                secompra = articulo.secompra
                pvp = articulo.pvp
                pujada_maxima = None
                stockfis = articulo.stockfis
                baixada_maxima = None
                codsubcuentairpfcom = None
                stockmax = articulo.stockmax
                imagen = articulo.imagen
                baixada_limitada = None
                codimpuesto = articulo.codimpuesto
                idsubcuentacom = None
                codbarras = articulo.codbarras
                nostock = articulo.nostock
                controlstock = articulo.controlstock
                temps_burst_baixada = None
                tipocodbarras = articulo.tipocodbarras
                sevende = articulo.sevende
                costemedio = None
                venta_online = articulo.venta_online
                pujada_burst_limit = None
                baixada_burst_limit = None
                pujada_limitada = None
                stockmin = articulo.stockmin
                codsubcuentacom = None
                if articulo.codfamilia:
                    codfamilia = articulo.codfamilia.codfamilia.encode('utf-8')
                else:
                    codfamilia = None
                if articulo.referencia:
                    referencia = articulo.referencia.encode('utf-8')
                else:
                    referencia = None
                if articulo.descripcion:
                    descripcion = articulo.descripcion.encode('utf-8')
                else:
                    descripcion = None
                if articulo.observaciones:
                    observaciones = articulo.observaciones.encode('utf-8')
                else:
                    observaciones = None

                writer.writerow([
                    temps_burst_pujada, secompra, pvp, pujada_maxima,
                    stockfis, baixada_maxima, codsubcuentairpfcom, stockmax,
                    descripcion, imagen, baixada_limitada, codimpuesto,
                    observaciones, idsubcuentacom, codbarras, nostock,
                    controlstock, temps_burst_baixada, tipocodbarras, sevende,
                    costemedio, venta_online, pujada_burst_limit,
                    baixada_burst_limit, pujada_limitada, stockmin,
                    codsubcuentacom, codfamilia, referencia
                ])

            outfile.close()

            articulos_time = int(format(datetime.now(), 'U'))
            elapsed = articulos_time - now
            print("Articulos exportados - %ss" % elapsed)

            # ------------------------------------------------------------

            familias = Familia.objects.all()
            outfile_path = os.path.join(
                settings.MEDIA_URL, 'csv', "to_export/familias.csv")

            outfile = open(outfile_path, 'wb')
            writer = csv.writer(outfile)
            writer.writerow(['codfamilia', 'descripcion'])

            for familia in familias:
                codfamilia = familia.codfamilia
                descripcion = familia.nombre.encode('utf-8')
                writer.writerow([codfamilia, descripcion])

            outfile.close()
            familias_time = int(format(datetime.now(), 'U'))
            elapsed = familias_time - articulos_time
            print("Familias exportadas - %ss" % elapsed)

            # ------------------------------------------------------------

            elapsed = int(format(datetime.now(), 'U')) - now
            return "Exportación terminada - %ss" % elapsed

        else:
            raise CommandError('Only the default is supported')
