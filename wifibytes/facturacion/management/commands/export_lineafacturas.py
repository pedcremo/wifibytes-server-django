# encoding=utf8
import sys
import imp
imp.reload(sys)
sys.setdefaultencoding('utf8')

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

from facturacion.models import facturasCli, lineasfacturascli

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

        if options['myoption'] == 'default':
            try:
                os.mkdir(os.path.join(settings.MEDIA_URL, 'csv'))
            except:
                pass

            now = int(format(datetime.now(), 'U'))
            before = now - 86400

            lineas = lineasfacturascli.objects.filter(
                idfactura__pk__gte=900000)

            outfile_path = os.path.join(
                settings.MEDIA_URL, 'csv', "to_export/lineafacturas.csv")

            outfile = open(outfile_path, 'wb')
            writer = csv.writer(outfile)
            writer.writerow([
                'pvptotal','cantidad','irpf','recargo',
                'dtolineal','descripcion','idlinea','idfactura',
                'idalbaran','codimpuesto','porcomision','iva',
                'dtopor','pvpsindto','idliquidacio','pvpunitario',
                'referencia'
            ])

            for linea in lineas:
                pvptotal = linea.pvptotal
                cantidad = linea.cantidad
                irpf = 0
                recargo = 0
                dtolineal = 0
                descripcion = linea.referencia.descripcion.encode('UTF-8')
                idlinea = linea.idlinea
                idfactura = linea.idfactura.pk # Class facturasCli
                idalbaran = linea.idalbaran
                codimpuesto = linea.codimpuesto
                porcomision = 0
                iva = linea.iva
                dtopor = linea.dtopor
                pvpsindto = linea.pvpsindto
                idliquidacio = linea.idliquidacio
                pvpunitario = linea.pvpunitario
                referencia = linea.referencia.pk

                writer.writerow([
                    pvptotal,cantidad,irpf,recargo,
                    dtolineal,descripcion,idlinea,idfactura,
                    idalbaran,codimpuesto,porcomision,iva,
                    dtopor,pvpsindto,idliquidacio,pvpunitario,
                    referencia
                ])

            outfile.close()

            facturas_time = int(format(datetime.now(), 'U'))
            elapsed = facturas_time - now
            print("Facturas exportadas - %ss" % elapsed)

            elapsed = int(format(datetime.now(), 'U')) - now
            return "Exportación terminada - %ss" % elapsed

        else:
            raise CommandError('Only the default is supported')
