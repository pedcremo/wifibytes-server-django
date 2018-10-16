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

from facturacion.models import (
    PedidoCli,
    LineaPedidoCli,
    Impuesto
)
from cliente.models import *


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

            now = int(format(datetime.now(), u'U'))
            before = now - 86400

            pedidos = PedidoCli.objects.filter(
                created_at__gte=before,
                created_at__lt=now
            )

            outfile_path = os.path.join(
                settings.MEDIA_URL, 'csv', "to_export/lineapedidos.csv")

            outfile = open(outfile_path, 'wb')
            writer = csv.writer(outfile)
            writer.writerow([
                'pvptotal','cantidad','irpf','recargo',
                'dtolineal','descripcion','idlinea','idpedido',
                'codimpuesto','cerrada','porcomision','iva',
                'dtopor','pvpsindto','idlineapresupuesto','pvpunitario',
                'referencia','totalenalbaran'
            ])

            for pedido in pedidos:
                lineas = LineaPedidoCli.objects.filter(idpedido=pedido.idpedido)
                for linea in lineas:

                    pvptotal = linea.pvptotal
                    cantidad = linea.cantidad
                    irpf = pedido.irpf
                    recargo = 0
                    dtolineal = 0
                    descripcion = linea.referencia.descripcion.encode('UTF-8')
                    idlinea = linea.idlinea
                    idpedido = pedido.idpedido
                    # codimpuesto = linea.codimpuesto # Class Impuesto
                    codimpuesto = "IVA18%"
                    cerrada = linea.cerrada
                    porcomision = 0
                    iva = linea.codimpuesto.iva
                    dtopor = 0
                    pvpsindto = linea.pvpsindto
                    idlineapresupuesto = linea.idlineapresupuesto
                    pvpunitario = linea.pvpunitario
                    referencia = linea.referencia.pk
                    totalenalbaran = 0

                    writer.writerow([
                        pvptotal,cantidad,irpf,recargo,
                        dtolineal,descripcion,idlinea,idpedido,
                        codimpuesto,cerrada,porcomision,iva,
                        dtopor,pvpsindto,idlineapresupuesto,pvpunitario,
                        referencia,totalenalbaran
                    ])

            outfile.close()

            lineapedidos__time = int(format(datetime.now(), u'U'))
            elapsed = lineapedidos__time - now
            print "Linea Pedidos exportados - %ss" % elapsed

            elapsed = int(format(datetime.now(), u'U')) - now
            return u"Exportación terminada - %ss" % elapsed

        else:
            raise CommandError('Only the default is supported')
