# -*- coding: utf-8 -*-
import csv
import os
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import datetime
from django.utils.dateformat import format
from django.utils.dateparse import parse_date
from facturacion.models import(
    PedidoCli,
    LineaPedidoCli,
    Impuesto
)
from catalogo.models import(
    Articulo,
)


class Command(BaseCommand):

    help = "That's Your help message"

    option_list = BaseCommand.option_list + (
        make_option('--myoption', action='store',
                    dest='myoption',
                    default='default',
                    help='Option help message'),
    )

    def handle(self, *app_labels, **options):

        ID_CSV = '1478703635'

        if options['myoption'] == 'default':
            now = int(format(datetime.now(), 'U'))
            before = now - 86400

            # ------------------------------------------------------------
            # Linea Pedidos
            # ------------------------------------------------------------
            path = settings.MEDIA_URL+'csv/lineapedidos_'+ID_CSV+'.csv'
            reader = csv.DictReader(open(path))

            # Guardar Datos en diccionario
            result = {}
            for row in reader:
                for column, value in row.items():
                    result.setdefault(column, []).append(value)

            for i in range(len(result['idlinea'])):

                try:  # Obtener linea
                    linea = LineaPedidoCli.objects.get(pk=result['idlinea'][i])
                except PedidoCli.DoesNotExist:
                    print('Linea Pedido Nueva')
                    linea = LineaPedidoCli()
                    linea.idlinea = result['idlinea'][i]

                try:  # Clase Articulo
                    linea.referencia = Articulo.objects.get(
                        pk=result['referencia'][i]
                    )
                except Articulo.DoesNotExist:
                    linea.referencia = None

                try:  # Clase PedidoCli
                    linea.idpedido = PedidoCli.objects.get(
                        pk=result['idpedido'][i]
                    )
                except PedidoCli.DoesNotExist:
                    linea.referencia = None

                linea.descripcion = result['descripcion'][i]  # ? Revisar
                linea.cerrada = result['cerrada'][i]
                try:
                    linea.idlineapresupuesto = int(
                        result['idlineapresupuesto'][i]
                    )
                except ValueError:
                    linea.idlineapresupuesto = None
                try:
                    linea.cantidad = float(result['cantidad'][i])
                except ValueError:
                    linea.cantidad = None
                try:
                    linea.pvpunitario = float(result['pvpunitario'][i])
                except ValueError:
                    linea.pvpunitario = None
                try:
                    linea.pvpsindto = float(result['pvpsindto'][i])
                except ValueError:
                    linea.pvpsindto = None
                try:
                    linea.porcomision = float(result['porcomision'][i])
                except ValueError:
                    linea.porcomision = None
                try:
                    linea.iva = float(result['iva'][i])
                except ValueError:
                    linea.iva = None
                try:
                    linea.totalenalbaran = float(result['totalenalbaran'][i])
                except ValueError:
                    linea.totalenalbaran = None

                # try: # Clase Impuesto
                #     linea.codimpuesto = Impuesto.objects.get(
                #     pk=result['codimpuesto'][i]
                # )
                # except Impuesto.DoesNotExist:
                #    linea.codimpuesto = None

                try:  # Guardar linea
                    linea.save()
                    print("Importado Linea Pedido idlinea => ", result['idlinea'][i])
                except:
                    print("ERROR Importando Linea Pedido idlinea => ", result['idlinea'][i])

            print('Total Linea Pedidos => ', len(result['idlinea']))

            elapsed = int(format(datetime.now(), 'U')) - now
            return "Importación terminada - %ss" % elapsed

        raise CommandError('Only the default is supported')
