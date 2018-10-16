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

from facturacion.models import PedidoCli
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

            '''pedidos = PedidoCli.objects.filter(
                created_at__gte=before,
                created_at__lt=now
            )'''

            pedidos = PedidoCli.objects.all()
            print 'NUMERO DE PEDIDOS', pedidos.count()

            outfile_path = os.path.join(
                settings.MEDIA_URL, 'csv', "to_export/pedidos.csv")

            outfile = open(outfile_path, 'wb')
            writer = csv.writer(outfile)
            writer.writerow([
                'codigo', 'totaleuros', 'idpresupuesto', 'direccion',
                'codpago', 'tasaconv', 'codejercicio', 'total',
                'irpf', 'nombrecliente', 'idpedido', 'observaciones',
                'porcomision', 'codcliente', 'servido', 'codpais',
                'editable', 'codalmacen', 'coddir', 'cifnif',
                'provincia', 'totalrecargo', 'codagente', 'recfinanciero',
                'fecha', 'neto', 'totalirpf', 'apartado',
                'codserie', 'codpostal', 'idprovincia', 'totaliva',
                'ciudad', 'fechasalida', 'numero', 'coddivisa'
            ])

            for pedido in pedidos:
                codigo = pedido.codigo
                totaleuros = pedido.totaleuros
                idpresupuesto = pedido.idpresupuesto
                direccion = pedido.direccion
                codpago = pedido.codpago
                tasaconv = pedido.tasaconv
                codejercicio = pedido.codejercicio
                total = pedido.total
                irpf = pedido.irpf
                nombrecliente = pedido.nombrecliente  # nombre ?? apellido?? comercial??
                idpedido = pedido.idpedido
                observaciones = pedido.observaciones
                porcomision = pedido.porcomision
                codcliente = pedido.codcliente.codcliente
                servido = pedido.servido
                codpais = pedido.codpais
                editable = pedido.editable
                codalmacen = pedido.codalmacen
                coddir = pedido.coddir
                cifnif = pedido.cifnif
                provincia = pedido.provincia
                totalrecargo = 0  # Comentado en el modelo
                codagente = None  # Comentado en el modelo
                recfinanciero = 0  # Comentado en el modelo
                fecha = pedido.fecha
                neto = pedido.neto
                totalirpf = 0  # Comentado en el modelo
                apartado = None  # Comentado en el modelo
                codserie = 'W'
                coddivisa = 'EUR'
                codpostal = pedido.codpostal
                idprovincia = pedido.idprovincia
                totaliva = pedido.totaliva
                ciudad = pedido.ciudad.encode('utf8')
                fechasalida = pedido.fechasalida
                numero = pedido.numero

                writer.writerow([
                    codigo, totaleuros, idpresupuesto, direccion,
                    codpago, tasaconv, codejercicio, total,
                    irpf, nombrecliente, idpedido, observaciones,
                    porcomision, codcliente, servido, codpais,
                    editable, codalmacen, coddir, cifnif,
                    provincia, totalrecargo, codagente, recfinanciero,
                    fecha, neto, totalirpf, apartado,
                    codserie, codpostal, idprovincia, totaliva,
                    ciudad, fechasalida, numero, coddivisa
                ])

            outfile.close()

            pedidos_time = int(format(datetime.now(), u'U'))
            elapsed = pedidos_time - now
            print "Pedidos exportados - %ss" % elapsed

            elapsed = int(format(datetime.now(), u'U')) - now
            return u"Exportación terminada - %ss" % elapsed

        else:
            raise CommandError('Only the default is supported')
