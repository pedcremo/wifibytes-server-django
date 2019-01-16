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

from facturacion.models import PedidoCli, facturasCli
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

        if options['myoption'] == 'default':
            try:
                os.mkdir(os.path.join(settings.MEDIA_URL, 'csv'))
            except:
                pass

            now = int(format(datetime.now(), 'U'))
            before = now - 86400

            facturas = facturasCli.objects.filter(idfactura__gte=900000)

            outfile_path = os.path.join(
                settings.MEDIA_URL, 'csv', "to_export/facturas.csv")

            outfile = open(outfile_path, 'wb')
            writer = csv.writer(outfile)
            writer.writerow([
                'codigo','totaleuros','hora','direccion',
                'codpago','tasaconv','codejercicio','total',
                'tpv','idasiento','automatica','irpf',
                'nombrecliente','idfactura','observaciones','porcomision',
                'codcliente','codpais','deabono','editable',
                'codalmacen','coddir','cifnif','nogenerarasiento',
                'idfacturarect','provincia','codigorect','totalrecargo',
                'codagente','recfinanciero','fecha','idpagodevol',
                'neto','totalirpf','apartado','codserie',
                'codpostal','idprovincia','totaliva','ciudad',
                'numero','coddivisa'
            ])

            for factura in facturas:
                codigo = factura.codigo
                totaleuros = factura.totaleuros
                hora = factura.hora
                direccion = factura.coddir.direccion
                if factura.coddir.numero:
                    direccion += ', %s' % factura.coddir.numero
                codpago = factura.codpago.pk # Class FormasPago
                tasaconv = factura.tasaconv
                codejercicio = '0001'
                total = factura.total
                tpv = factura.tpv
                idasiento = factura.idasiento
                automatica = factura.automatica
                irpf = factura.irpf
                nombrecliente = factura.nombrecliente
                idfactura = factura.idfactura
                observaciones = factura.observaciones
                porcomision = 0
                codcliente = factura.codcliente.pk # Class cliente.Cliente
                codpais = factura.codpais # Class geo.Pais
                deabono = factura.deabono
                editable = factura.editable
                codalmacen = factura.codalmacen
                coddir = factura.coddir
                cifnif = factura.cifnif
                nogenerarasiento = factura.nogenerarasiento
                idfacturarect = factura.idfacturarect
                provincia = factura.provincia
                codigorect = factura.codigorect
                totalrecargo = 0
                codagente = factura.codagente
                recfinanciero = 0
                fecha = factura.fecha
                idpagodevol = factura.idpagodevol
                neto = factura.neto
                totalirpf = factura.totalirpf
                apartado = factura.apartado
                codserie = 'W'
                codpostal = factura.codpostal
                idprovincia = factura.idprovincia # Class geo.Provincia
                totaliva = factura.totaliva
                ciudad = factura.ciudad
                numero = factura.numero
                coddivisa = 'EUR'
                writer.writerow([
                    codigo,totaleuros,hora,direccion,
                    codpago,tasaconv,codejercicio,total,
                    tpv,idasiento,automatica,irpf,
                    nombrecliente,idfactura,observaciones,porcomision,
                    codcliente,codpais,deabono,editable,
                    codalmacen,coddir,cifnif,nogenerarasiento,
                    idfacturarect,provincia,codigorect,totalrecargo,
                    codagente,recfinanciero,fecha,idpagodevol,
                    neto,totalirpf,apartado,codserie,
                    codpostal,idprovincia,totaliva,ciudad,
                    numero,coddivisa
                ])

            outfile.close()

            facturas_time = int(format(datetime.now(), 'U'))
            elapsed = facturas_time - now
            print("Facturas exportadss - %ss" % elapsed)

            elapsed = int(format(datetime.now(), 'U')) - now
            return "Exportación terminada - %ss" % elapsed

        else:
            raise CommandError('Only the default is supported')
