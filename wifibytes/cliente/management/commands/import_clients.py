# -*- coding: utf-8 -*-
import csv
import os
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db.models import Q
from datetime import datetime
from django.utils.dateformat import format
from django.http import HttpResponse
from wifibytes.utils import intorzero
from geo.models import Provincia
from omv.models import Omv
from catalogo.models import Tarifa
from cliente.models import (
    Cliente,
    MobilsClients,
    CuentasbcoCli,
    DirClientes
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
        ID_CSV = '1479478920'

        if options['myoption'] == 'default':

            # Importar clientes
            path = settings.MEDIA_URL + 'csv/to_import/eneboo_clientes.csv'
            reader = csv.DictReader(open(path))

            # Guardar Datos en diccionario
            result = {}
            for row in reader:
                for column, value in row.iteritems():
                    if value == 'None':
                        value = None
                    result.setdefault(column, []).append(value)

            print "\n---> Importando clientes\n"
            for i in range(len(result['codcliente'])):

                try:  # Obtener Cliente
                    cliente = Cliente.objects.get(
                        Q(pk=result['codcliente'][i]))
                    nombre = result['nombre'][i].replace('´', '')
                    cliente.nombre = nombre.replace(
                        cliente.apellido, '').strip()
                    cliente.apellido = nombre.replace(
                        cliente.nombre, '').strip()
                except Cliente.DoesNotExist:
                    cliente = Cliente()
                    cliente.nombre = result['nombre'][i].replace('´', '')
                    cliente.codcliente = result['codcliente'][i]
                    cliente.cifnif = result['cifnif'][i]
                    cliente.is_active = False
                except Exception as msg:
                    print "Error al buscar el cliente -> %s" % (
                        msg)

                cliente.email = result['email'][i]
                cliente.nombrecomercial = result['nombrecomercial'][i]
                cliente.telefono1 = result['telefono1'][i]
                cliente.tipoidfiscal = result['tipoidfiscal'][i]
                cliente.debaja = result['debaja'][i]
                cliente.observaciones = result['observaciones'][i]
                try:
                    cuenta = CuentasbcoCli.objects.get(
                        pk=int(result['codcuentadom'][i])
                    )
                    cliente.codcuentadom = cuenta
                except CuentasbcoCli.DoesNotExist:
                    pass
                except Exception as msg:
                    pass

                try:
                    cliente.save()
                    # print "Cliente guardado %s" % result['codcliente'][i]
                except Exception as msg:
                    print "ERROR Importando Client (%s) -> %s" % (
                        result['codcliente'][i], msg)

            # --- DIRECCIONES --- #
            # Importar Direcciones
            path = settings.MEDIA_URL + 'csv/to_import/eneboo_direcciones.csv'
            reader = csv.DictReader(open(path))

            # Guardar Datos en diccionario
            result = {}
            for row in reader:
                for column, value in row.iteritems():
                    if value == 'None':
                        value = None
                    result.setdefault(column, []).append(value)

            print "\n---> Importando direcciones\n"
            for i in range(len(result['id'])):
                try:  # Obtener Direccion
                    direccion = DirClientes.objects.get(
                        pk=result['id'][i]
                    )
                except DirClientes.DoesNotExist:
                    # print '\t+++ -> Direccion Nueva'
                    direccion = DirClientes()
                    direccion.id = result['id'][i]

                try:
                    cliente = Cliente.objects.get(
                        pk=result['codcliente'][i]
                    )
                    direccion.codcliente = cliente
                    direccion.domenvio = intorzero(result['domenvio'][i])
                    direccion.domfacturacion = intorzero(
                        result['domfacturacion'][i]
                    )
                    direccion.direccion = result['direccion'][i]
                    direccion.codpais = result['codpais'][i]
                    direccion.ciudad = result['ciudad'][i]
                    direccion.provincia = result['provincia'][i]
                    try:
                        idprovincia = Provincia.objects.get(
                            pk=int(result['idprovincia'][i])
                        )
                        direccion.idprovincia = idprovincia
                    except Exception as msg:
                        direccion.provincia = None

                    direccion.apartado = result['apartado'][i]
                    direccion.codpostal = result['codpostal'][i]
                    direccion.save()
                except Cliente.DoesNotExist:
                    print '\txxx -> El Cliente De Direccion no existe (%s)' % (
                        result['codcliente'][i]
                    )

            # --- CUENTAS --- #
            # Importar Cuentas
            path = settings.MEDIA_URL + 'csv/to_import/eneboo_cuentasbcocli.csv'
            reader = csv.DictReader(open(path))

            # Guardar Datos en diccionario
            result = {}
            for row in reader:
                for column, value in row.iteritems():
                    if value == 'None':
                        value = None
                    result.setdefault(column, []).append(value)
            print "\n---> Importando cuentas\n"
            for i in range(len(result['codcuenta'])):
                try:  # Obtener Direccion
                    cuenta = CuentasbcoCli.objects.get(
                        pk=result['codcuenta'][i]
                    )
                except CuentasbcoCli.DoesNotExist:
                    # print '\t+++ -> Direccion Nueva'
                    cuenta = CuentasbcoCli()
                    cuenta.codcuenta = result['codcuenta'][i]

                try:
                    cliente = Cliente.objects.get(
                        pk=result['codcliente'][i]
                    )
                    cuenta.codcliente = cliente
                    cuenta.ctaentidad = result['ctaentidad'][i]
                    cuenta.iban = result['iban'][i]
                    cuenta.codiban = result['iban'][i][:4]
                    cuenta.entidad = result['entidad'][i]
                    cuenta.codigocuenta = result['codigocuenta'][i]
                    cuenta.codpais = result['codpais'][i]
                    cuenta.ctaagencia = result['ctaagencia'][i]
                    cuenta.bic = result['bic'][i]
                    # cuenta.titular = result['titular'][i]
                    cuenta.codcuenta = result['codcuenta'][i]
                    cuenta.idusuariomod = result['idusuariomod'][i]
                    cuenta.cuenta = result['cuenta'][i]
                    # cuenta.fechaalta = result['fechaalta'][i]
                    # cuenta.fechamod = result['fechamod'][i]
                    # cuenta.horaalta = result['horaalta'][i]
                    # cuenta.horamod = result['horamod'][i]
                    cuenta.idusuarioalta = result['idusuarioalta'][i]
                    cuenta.ctadc = result['ctadc'][i]
                    cuenta.save()
                except Cliente.DoesNotExist:
                    print '\txxx -> El Cliente De Cuenta no existe (%s)' % (
                        result['codcliente'][i]
                    )

            # --- MOBILS --- #
            path = settings.MEDIA_URL + 'csv/to_import/eneboo_mobils_clients.csv'
            reader = csv.DictReader(open(path))

            # Guardar Datos en diccionario
            result = {}
            for row in reader:
                for column, value in row.iteritems():
                    result.setdefault(column, []).append(value)

            print "\n---> Importando mobils\n"
            for i in range(len(result['id_mobils_clients'])):

                try:  # Obtener Mobil
                    linea = MobilsClients.objects.get(
                        pk=result['id_mobils_clients'][i]
                    )
                except MobilsClients.DoesNotExist:
                    # print '\t+++ -> Mobil Nuevo'
                    linea = MobilsClients()
                    linea.id_mobilsclients = result['id_mobils_clients'][i]
                try:
                    cliente = Cliente.objects.get(
                        pk=result['codcliente'][i]
                    )
                    linea.codcliente = cliente
                    try:  # Obtener Tarifa
                        tarifa = Tarifa.objects.get(
                            tarifa_siglas=result['tarifa'][i]
                        )
                    except Tarifa.DoesNotExist:
                        tarifa = Tarifa()
                        tarifa.nombretarifa = result['tarifa'][i]
                        tarifa.precio = 0
                        tarifa.sms = 0
                        tarifa.voz = 0
                        tarifa.datos = 0
                        tarifa.activo = False
                        tarifa.destacado = False
                        tarifa.tarifa_siglas = result['tarifa'][i]
                        tarifa.save()
                    linea.codtarifa = tarifa
                    linea.mobil = result['mobil'][i]
                    linea.save()
                except Cliente.DoesNotExist:
                    print "\txxx -> El cliente no existe. (linea: %s)" % (
                        str(result['id_mobils_clients'][i]))

            return "\n--->  Script Importar Mobils finalizado \n"
            return "\n--->  Script Importar Clientes finalizado \n"

        raise CommandError('Only the default is supported')
