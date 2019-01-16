# -*- coding: utf-8 -*-
import csv
import os
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import datetime
from django.utils.dateformat import format
from facturacion.models import(
    PedidoCli,
    FormasEnvio,
    FormasPago,
)
from cliente.models import *
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

        ID_CSV = '1478700290'

        if options['myoption'] == 'default':
            now = int(format(datetime.now(), 'U'))
            before = now - 86400

            # ------------------------------------------------------------
            # Pedidos
            # ------------------------------------------------------------
            path = settings.MEDIA_URL+'csv/pedidos_'+ID_CSV+'.csv'
            reader = csv.DictReader(open(path))

            # Guardar Datos en diccionario
            result = {}
            for row in reader:
                for column, value in row.items():
                    result.setdefault(column, []).append(value)

            for i in range(len(result['idpedido'])):

                try:  # Obtener pedido
                    pedido = PedidoCli.objects.get(pk=result['idpedido'][i])
                except PedidoCli.DoesNotExist:
                    print('Pedido Nuevo')
                    pedido = PedidoCli()
                    pedido.idpedido = result['idpedido'][i]

                try:  # Clase Cliente
                    pedido.codcliente = Cliente.objects.get(
                        pk=result['codcliente'][i]
                    )
                except Cliente.DoesNotExist:
                    pedido.codcliente = None

                try:  # Clase DirClientes
                    pedido.coddir = DirClientes.objects.get(
                        pk=result['coddir'][i]
                    )
                    pedido.coddirEnvio = DirClientes.objects.get(
                        pk=result['coddir'][i]
                    )
                except DirClientes.DoesNotExist:
                    pedido.coddir = None

                try:  # Clase FormasEnvio
                    pedido.formaEnvio = FormasEnvio.objects.filter()[:1].get()
                except FormasEnvio.DoesNotExist:
                    pedido.formaEnvio = None

                try:  # Clase FormasPago
                    pedido.formaPago = FormasPago.objects.filter()[:1].get()
                except FormasPago.DoesNotExist:
                    pedido.formaPago = None

                pedido.cifnif = result['cifnif'][i]
                pedido.nombrecliente = result['nombrecliente'][i]
                pedido.direccion = result['direccion'][i]
                pedido.provincia = result['provincia'][i]
                pedido.idprovincia = result['idprovincia'][i]
                pedido.ciudad = result['ciudad'][i]
                pedido.codpostal = result['codpostal'][i]
                pedido.nombreclienteFacturacion = None
                pedido.cifnifFacturacion = None
                pedido.codpais = result['codpais'][i]
                pedido.direccionEnvio = None
                pedido.provinciaEnvio = None
                pedido.idprovinciaEnvio = None
                pedido.ciudadEnvio = None
                pedido.codpostalEnvio = None
                pedido.codpago = result['codpago'][i]
                pedido.codigo = result['codigo'][i]
                pedido.codserie = result['codserie'][i]
                pedido.coddivisa = result['coddivisa'][i]
                pedido.tasaconv = result['tasaconv'][i]
                pedido.codejercicio = result['codejercicio'][i]
                pedido.irpf = result['irpf'][i]
                pedido.totaleuros = float(result['totaleuros'][i])
                pedido.total = float(result['total'][i])
                pedido.totaliva = result['totaliva'][i]
                pedido.neto = float(result['neto'][i])
                pedido.porcomision = result['porcomision'][i]
                pedido.idpresupuesto = result['idpresupuesto'][i]
                pedido.observaciones = result['observaciones'][i]
                pedido.servido = result['servido'][i]
                pedido.editable = result['editable'][i]
                pedido.codalmacen = result['codalmacen'][i]
                pedido.numero = result['numero'][i]
                pedido.estado = 0  # Default ?
                pedido.pagado = False  # Default ?
                pedido.generar_factura = True

                # Probl parseDate
                # pedido.fecha = result['fecha'][i]
                # pedido.fechasalida = result['fechasalida'][i]

                pedido.save()
                try:  # Guardar Pedido
                    print("Importado Pedido idpedido => ", result['idpedido'][i])
                except:
                    print("ERROR Importando Pedido idpedido => ", result['idpedido'][i])


            print('Total Pedidos => ', len(result['idpedido']))

            elapsed = int(format(datetime.now(), 'U')) - now
            return "Importación terminada - %ss" % elapsed

        raise CommandError('Only the default is supported')
