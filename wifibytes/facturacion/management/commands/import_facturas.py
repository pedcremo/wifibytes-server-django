# -*- coding: utf-8 -*-
import csv
import os
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import datetime
from django.utils.dateformat import format
from facturacion.models import (
    facturasCli, PedidoCli, FormasEnvio, FormasPago, lineasfacturascli,
    PedidoCli)

from geo.models import Pais, Provincia
from cliente.models import *
from django.utils.dateparse import parse_date
from time import time
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
        ID_CSV = '1478707748'
        if options['myoption'] == 'default':
            now = int(format(datetime.now(), 'U'))
            before = now - 86400

            # ------------------------------------------------------------
            # Formas de pago
            # ------------------------------------------------------------
            path = settings.MEDIA_URL+'csv/to_import/eneboo_formaspago.csv'
            reader = csv.DictReader(open(path))
            print("Importando formas de pago")

            # Guardar Datos en diccionario
            result = {}
            for row in reader:
                for column, value in row.items():
                    result.setdefault(column, []).append(value)

            for i in range(len(result['codpago'])):

                try:
                    try:
                        pago = FormasPago.objects.get(
                            cod_eneboo=result['codpago'][i]
                        )
                    except FormasPago.DoesNotExist:
                        pago = FormasPago()

                    pago.nombre = result['descripcion'][i]
                    pago.descripcion = result['descripcion'][i]
                    pago.cod_eneboo = result['codpago'][i]
                    pago.activa = False

                    pago.save()
                except Exception as msg:
                    print("ERROR Importando Forma Pago => %s" % (
                        result['codpago'][i]))

            print('Total formas pago => %s en %s segundos' % (
                len(result['codpago']),
                int(format(datetime.now(), 'U')) - now))


        # ------------------------------------------------------------
        # Facturas
        # ------------------------------------------------------------
        path = settings.MEDIA_URL+'csv/to_import/eneboo_facturascli.csv'
        reader = csv.DictReader(open(path))

        # Guardar Datos en diccionario
        result = {}
        for row in reader:
            for column, value in row.items():
                if value == 'None':
                    value = None
                result.setdefault(column, []).append(value)
        for i in range(len(result['idfactura'])):

            try:  # Obtener factura
                factura = facturasCli.objects.get(
                    pk=result['idfactura'][i]
                )
            except facturasCli.DoesNotExist:
                factura = facturasCli()
                factura.idfactura = result['idfactura'][i]

            try:  # Clase FormasPago
                factura.codpago = FormasPago.objects.get(
                    cod_eneboo=result['codpago'][i]
                )
            except FormasPago.DoesNotExist:
                factura.codpago = FormasPago.objects.filter()[:1].get()

            try:  # Clase Pais
                factura.codpais = Pais.objects.get(
                    pk=result['codpais'][i]
                )
            except Pais.DoesNotExist:
                try:
                    factura.codpais = Pais.objects.filter()[:1].get()
                except Exception as msg:
                    factura.codpais = None

            try:  # Clase Provincia
                factura.provincia = Provincia.objects.get(
                    pk=result['provincia'][i]
                )
            except Exception as msg:
                factura.provincia = None

            factura.codigo = result['codigo'][i]
            factura.totaleuros = float(result['totaleuros'][i])
            factura.hora = result['hora'][i]
            factura.direccion = result['direccion'][i]
            factura.tasaconv = result['tasaconv'][i]
            factura.codejercicio = result['codejercicio'][i]
            factura.total = float(result['total'][i])
            factura.tpv = result['tpv'][i]
            factura.automatica = result['automatica'][i]
            factura.nombrecliente = result['nombrecliente'][i]
            factura.idfactura = result['idfactura'][i]
            factura.observaciones = result['observaciones'][i]
            factura.deabono = result['deabono'][i]
            factura.editable = bool(result['editable'][i])
            factura.codalmacen = result['codalmacen'][i]
            factura.cifnif = result['cifnif'][i]
            factura.nogenerarasiento = result['nogenerarasiento'][i]
            factura.codigorect = result['codigorect'][i]
            factura.codagente = result['codagente'][i]
            factura.fecha = result['fecha'][i]
            factura.apartado = result['apartado'][i]
            factura.codserie = result['codserie'][i]
            factura.codpostal = result['codpostal'][i]
            factura.ciudad = result['ciudad'][i]
            factura.numero = result['numero'][i]
            factura.coddivisa = result['coddivisa'][i]

            try:
                factura.porcomision = float(result['porcomision'][i])
            except Exception as msg:
                factura.porcomision = None

            try:
                factura.idfacturarect = int(result['idfacturarect'][i])
            except Exception as msg:
                factura.idfacturarect = None

            try:
                factura.coddir = DirClientes.objects.get(
                    pk=int(result['coddir'][i]))
            except Exception as msg:
                factura.coddir = None

            try:
                factura.codcliente = Cliente.objects.get(
                    pk=result['codcliente'][i])
            except Cliente.DoesNotExist:
                print("No se encuentra el cliente factura %s" % (
                    result['idfactura'][i]))
                continue

            try:
                factura.totalrecargo = float(result['totalrecargo'][i])
            except Exception as msg:
                factura.totalrecargo = None

            try:
                factura.recfinanciero = float(result['recfinanciero'][i])
            except Exception as msg:
                factura.recfinanciero = 0

            try:
                factura.idpagodevol = int(result['idpagodevol'][i])
            except Exception as msg:
                factura.idpagodevol = None

            try:
                factura.neto = float(result['neto'][i])
            except Exception as msg:
                factura.neto = 0

            try:
                factura.totalirpf = float(result['totalirpf'][i])
            except Exception as msg:
                factura.totalirpf = 0

            try:
                factura.irpf = float(result['irpf'][i])
            except Exception as msg:
                factura.irpf = 0

            try:
                factura.totaliva = float(result['totaliva'][i])
            except Exception as msg:
                factura.totaliva = 0

            try:
                factura.save()
            except Exception as msg:
                print("ERROR Importando Factura => %s" % (
                    result['idfactura'][i]))

        print('Total Facturas => %s en %s segundos' % (
            len(result['idfactura']),
            int(format(datetime.now(), 'U')) - now))

        # ------------------------------------------------------------
        # Lineas Facturas
        # ------------------------------------------------------------
        path = settings.MEDIA_URL+'csv/to_import/eneboo_lineasfacturascli.csv'
        reader = csv.DictReader(open(path))

        # Guardar Datos en diccionario
        result = {}
        for row in reader:
            for column, value in row.items():
                if value == 'None':
                    value = None
                result.setdefault(column, []).append(value)
                # print column, value
            # print "-"*40
        for i in range(len(result['idfactura'])):

            try:
                try:
                    linea_factura = lineasfacturascli.objects.get(
                        pk=result['idfactura'][i]
                    )
                except lineasfacturascli.DoesNotExist:
                    # print 'Factura Nueva'
                    linea_factura = lineasfacturascli()
                    linea_factura.idlinea = result['idlinea'][i]

                try:
                    linea_factura.idfactura = facturasCli.objects.get(
                        pk=result['idfactura'][i])
                except facturasCli.DoesNotExist:
                    print("Factura no encontrada, linea %s" % (
                        result['idlinea'][i]))
                    continue

                linea_factura.pvptotal = result['pvptotal'][i]
                linea_factura.cantidad = result['cantidad'][i]
                linea_factura.irpf = result['irpf'][i]
                linea_factura.recargo = result['recargo'][i]
                linea_factura.dtolineal = result['dtolineal'][i]
                linea_factura.descripcion = result['descripcion'][i]
                linea_factura.idalbaran = result['idalbaran'][i]
                linea_factura.codimpuesto = result['codimpuesto'][i]
                linea_factura.porcomision = result['porcomision'][i]
                linea_factura.iva = result['iva'][i]
                linea_factura.dtopor = result['dtopor'][i]
                linea_factura.pvpsindto = result['pvpsindto'][i]
                linea_factura.idliquidacio = result['idliquidacio'][i]
                linea_factura.pvpunitario = result['pvpunitario'][i]
                linea_factura.referencia = result['referencia'][i]
                linea_factura.save()

            except Exception as msg:
                print("ERROR Importando lineaFactura (%s) => %s" % (
                    result['idlinea'][i], msg))

        # ------------------------------------------------------------
        # Pedidos
        # ------------------------------------------------------------
        path = settings.MEDIA_URL+'csv/to_import/eneboo_pedidoscli.csv'
        reader = csv.DictReader(open(path))

        # Guardar Datos en diccionario
        result = {}
        for row in reader:
            for column, value in row.items():
                if value == 'None':
                    value = None
                result.setdefault(column, []).append(value)

        for i in range(len(result['idpedido'])):

            try:
                try:
                    pedido = PedidoCli.objects.get(
                        pk=result['idpedido'][i]
                    )
                except PedidoCli.DoesNotExist:
                    # print 'Factura Nueva'
                    pedido = PedidoCli()
                    pedido.idpedido = result['idpedido'][i]

                try:
                    pedido.codcliente = Cliente.objects.get(
                        pk=result['codcliente'][i])
                except Cliente.DoesNotExist:
                    print("Cliente no encontrado pedido %s" % (
                        result['codcliente'][i]))
                    continue

                try:
                    pedido.coddir = DirClientes.objects.get(
                        pk=result['coddir'][i])
                except Cliente.DoesNotExist:
                    print("Direccion no encontrada pedido %s" % (
                        result['coddir'][i]))
                    continue

                try:
                    pedido.coddirEnvio = DirClientes.objects.get(
                        pk=result['coddirEnvio'][i])
                except Cliente.DoesNotExist:
                    print("Direccion envio no encontrada pedido %s" % (
                        result['coddirEnvio'][i]))
                    continue

                try:
                    pedido.codpago = FormasPago.objects.get(
                        pk=result['codpago'][i])
                except FormasPago.DoesNotExist:
                    print("Forma pago no encontrada pedido %s" % (
                        result['codpago'][i]))
                    continue

                try:
                    pedido.formaPago = formaPago.objects.get(
                        pk=result['formaPago'][i])
                except formaPago.DoesNotExist:
                    print("Cliente no encontrado pedido %s" % (
                        result['codcliente'][i]))
                    continue


                pedido.codpais = result['codpais'][i]
                pedido.cifnif = result['cifnif'][i]
                pedido.nombrecliente = result['nombrecliente'][i]
                pedido.direccion = result['direccion'][i]
                pedido.provincia = result['provincia'][i]
                pedido.idprovincia = result['idprovincia'][i]
                pedido.ciudad = result['ciudad'][i]
                pedido.codpostal = result['codpostal'][i]
                pedido.nombreclienteFacturacion = result[
                    'nombreclienteFacturacion'][i]
                pedido.cifnifFacturacion = result['cifnifFacturacion'][i]
                pedido.direccionEnvio = result['direccionEnvio'][i]
                pedido.provinciaEnvio = result['provinciaEnvio'][i]
                pedido.idprovinciaEnvio = result['idprovinciaEnvio'][i]
                pedido.ciudadEnvio = result['ciudadEnvio'][i]
                pedido.codpostalEnvio = result['codpostalEnvio'][i]
                pedido.codigo = result['codigo'][i]
                pedido.codserie = result['codserie'][i]
                pedido.coddivisa = result['coddivisa'][i]
                pedido.tasaconv = result['tasaconv'][i]
                pedido.codejercicio = result['codejercicio'][i]
                pedido.irpf = result['irpf'][i]
                pedido.totaleuros = result['totaleuros'][i]
                pedido.total = result['total'][i]
                pedido.totaliva = result['totaliva'][i]
                pedido.neto = result['neto'][i]
                pedido.porcomision = result['porcomision'][i]
                pedido.idpresupuesto = result['idpresupuesto'][i]
                pedido.observaciones = result['observaciones'][i]
                pedido.servido = result['servido'][i]
                pedido.editable = result['editable'][i]
                pedido.codalmacen = result['codalmacen'][i]
                pedido.fechasalida = result['fechasalida'][i]
                pedido.numero = result['numero'][i]
                pedido.fecha = result['fecha'][i]
                pedido.estado = result['estado'][i]
                pedido.pagado = result['pagado'][i]

                generar_factura
                pedido.save()

            except Exception as msg:
                print("ERROR Importando lineaFactura (%s) => %s" % (
                    result['idlinea'][i], msg))

        print('Total Facturas => %s en %s segundos' % (
            len(result['idfactura']),
            int(format(datetime.now(), 'U')) - now))

        raise CommandError('Only the default is supported')
