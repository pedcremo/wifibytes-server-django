# -*- coding: utf-8 -*-
import csv
import os
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import datetime
from django.utils.dateformat import format
from facturacion.models import(
    lineasfacturascli,
    facturasCli
)
from catalogo.models import(
    Articulo,
)
from django.utils.dateparse import parse_date

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

        ID_CSV = '1478770598'

        if options['myoption'] == 'default':
            now = int(format(datetime.now(), u'U'))
            before = now - 86400

            # ------------------------------------------------------------
            # Linea Facturas
            # ------------------------------------------------------------
            path = settings.MEDIA_URL+'csv/lineafacturas_'+ID_CSV+'.csv'
            reader = csv.DictReader(open(path))

            # Guardar Datos en diccionario
            result = {}
            for row in reader:
                for column, value in row.iteritems():
                    result.setdefault(column, []).append(value)

            for i in range(len(result['idlinea'])):

                try:  # Obtener linea
                    linea = lineasfacturascli.objects.get(pk=result['idlinea'][i])
                except lineasfacturascli.DoesNotExist:
                    print 'Linea Factura Nueva'
                    linea = lineasfacturascli()
                    linea.idlinea = result['idlinea'][i]

                linea.idfactura = facturasCli.objects.get(pk=result['idfactura'][i])
                try:
                    linea.pvptotal = float(result['pvptotal'][i])
                except ValueError:
                    linea.pvptotal = 0
                try:
                    linea.cantidad = float(result['cantidad'][i])
                except ValueError:
                    linea.cantidad = 0
                try:
                    linea.irpf = float(result['irpf'][i])
                except ValueError:
                    linea.irpf = None
                try:
                    linea.recargo = float(result['recargo'][i])
                except ValueError:
                    linea.recargo = None
                try:
                    linea.dtolineal = float(result['dtolineal'][i])
                except ValueError:
                    linea.dtolineal = None
                linea.descripcion = result['descripcion'][i]
                try:
                    linea.idalbaran = int(result['idalbaran'][i])
                except ValueError:
                    linea.idalbaran = None
                linea.codimpuesto = result['codimpuesto'][i]
                try:
                    linea.porcomision = float(result['porcomision'][i])
                except ValueError:
                    linea.porcomision = None
                try:
                    linea.iva = float(result['iva'][i])
                except ValueError:
                    linea.iva = None
                try:
                    linea.dtopor = float(result['dtopor'][i])
                except ValueError:
                    linea.dtopor = 0
                try:
                    linea.pvpsindto = float(result['pvpsindto'][i])
                except ValueError:
                    linea.pvpsindto = 0
                try:
                    linea.idliquidacio = int(result['idliquidacio'][i])
                except ValueError:
                    linea.idliquidacio = None
                try:
                    linea.pvpunitario = float(result['pvpunitario'][i])
                except ValueError:
                    linea.pvpunitario = 0
                linea.referencia = result['referencia'][i]

                try:  # Guardar linea
                    linea.save()
                    print "Importado Linea Factura idlinea => ", result['idlinea'][i]
                except:
                    print "ERROR Importando Linea Factura idlinea => ", result['idlinea'][i]


            print 'Total Linea Facturas => ', AttributeErrorlen(result['idlinea'])

            elapsed = int(format(datetime.now(), u'U')) - now
            return u"Importación terminada - %ss" % elapsed

        raise CommandError('Only the default is supported')
