# -*- coding: utf-8 -*-
import sys
import imp
imp.reload(sys)
sys.setdefaultencoding('utf-8')
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from cliente.models import (
    Cliente, MobilsClients, CuentasbcoCli, DirClientes)
from django.conf import settings
from datetime import datetime
from django.utils.dateformat import format
from django.http import HttpResponse
import csv
import os

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
            '''clientes = Cliente.objects.filter(updated_at__gte=before,
                                              updated_at__lt=now)
            '''
            clientes = Cliente.objects.all()
            print('NUM CLIENTES', clientes.count())
            outfile_path = os.path.join(
                settings.MEDIA_URL, 'csv', "to_export/clientes.csv")

            outfile = open(outfile_path, 'wb')
            writer = csv.writer(outfile)
            writer.writerow([
                'codcliente', 'nombre', 'email', 'cifnif', 'nombrecomercial',
                'telefono1', 'codagente', 'regimeniva', 'codcuentarem',
                'codcuentadom', 'coddivisa', 'recargo', 'codserie',
                'ivaincluido', 'codsubcuenta', 'codpago', 'codgrupo',
                'tipoidfiscal', 'pppoepassword', 'pppoeusuari',
                'riesgoalcanzado', 'riesgomax', 'idsubcuenta', 'contacto',
                'capitalimpagado', 'web', 'mac', 'observaciones',
                'copiasfactura', 'node_connexio', 'ip_publica', 'codcontacto',
                'codedi', 'codtiporappel', 'fax', 'telefono2', 'debaja',
                'fechabaja', 'codagente'])

            for cliente in clientes:
                codcliente = cliente.codcliente
                apellido = ''
                if cliente.apellido:
                    apellido = cliente.apellido
                nombre = "%s %s" % (cliente.nombre, apellido)
                email = cliente.email
                cifnif = cliente.cifnif
                nombrecomercial = cliente.nombrecomercial
                telefono1 = cliente.telefono

                try:
                    codcuentadom = cliente.codcuentadom
                except:
                    codcuentadom = ''

                tipoidfiscal = cliente.tipo_cliente
                debaja = cliente.debaja
                observaciones = cliente.observaciones

                regimeniva = 'General'
                pppoepassword = ''
                pppoeusuari = ''
                riesgoalcanzado = '0'
                riesgomax = ''
                ivaincluido = ''
                contacto = ''
                idsubcuenta = ''
                capitalimpagado = ''
                recargo = ''
                web = ''
                mac = ''
                copiasfactura = '1'
                node_connexio = ''
                ip_publica = ''
                codcontacto = ''
                codcuentarem = '000001'
                codsubcuenta = ''
                codedi = ''
                codpago = 'DI'
                codtiporappel = ''
                codserie = 'W'
                codgrupo = 'ALTREB'
                coddivisa = 'EUR'
                fax = ''
                telefono2 = ''
                fechabaja = ''
                codagente = ''

                writer.writerow([
                    codcliente, nombre, email, cifnif, nombrecomercial,
                    telefono1, codagente, regimeniva, codcuentarem,
                    codcuentadom, coddivisa, recargo, codserie, ivaincluido,
                    codsubcuenta, codpago, codgrupo, tipoidfiscal,
                    pppoepassword, pppoeusuari, riesgoalcanzado, riesgomax,
                    idsubcuenta, contacto, capitalimpagado, web, mac,
                    observaciones, copiasfactura, node_connexio,
                    ip_publica, codcontacto, codedi, codtiporappel, fax,
                    telefono2, debaja, fechabaja, codagente])

            outfile.close()

            clientes_time = int(format(datetime.now(), 'U'))
            elapsed = clientes_time - now
            print("Clientes exportados - %ss" % elapsed)

            # ------------------------------------------------------------

            mobils = MobilsClients.objects.filter(updated_at__gte=before,
                                                  updated_at__lt=now)

            mobils = MobilsClients.objects.all()
            print('NUM MOBILS ', mobils.count())
            outfile_path = os.path.join(
                settings.MEDIA_URL, 'csv', "to_export/mobils_clients.csv")

            outfile = open(outfile_path, 'wb')
            writer = csv.writer(outfile)
            writer.writerow(['id_mobils_clients', 'tarifa', 'codcliente',
                             'codagente', 'mobil'])

            for mobilcli in mobils:
                id_mobils_clients = mobilcli.id_mobilsclients
                tarifa = mobilcli.codtarifa.pk
                codagente = ''
                tipoCliente = mobilcli.codcliente.tipo_cliente
                mobil = mobilcli.mobil
                codcliente = mobilcli.codcliente.pk
                codtarifa = mobilcli.codtarifa
                fechaContrato = mobilcli.fechaContrato
                imageContrato = mobilcli.imageContrato
                roaming = mobilcli.roaming
                buzon_voz = mobilcli.buzon_voz
                coddir = mobilcli.coddir
                tipoTarifaAntigua = mobilcli.tipoTarifaAntigua
                tipoSim = mobilcli.tipoSim
                companiaAnterior = mobilcli.companiaAnterior
                activa = mobilcli.activa

                writer.writerow([
                     id_mobils_clients, tarifa, codcliente, codagente, mobil])

            outfile.close()
            mobils_time = int(format(datetime.now(), 'U'))
            elapsed = mobils_time - clientes_time
            print("Lineas exportadas - %ss" % elapsed)

            # ------------------------------------------------------------

            cuentas = CuentasbcoCli.objects.filter(created_at__gte=before,
                                                   created_at__lt=now)
            cuentas = CuentasbcoCli.objects.all()
            print('NUM CUENTAS ', cuentas.count())

            outfile_path = os.path.join(
                settings.MEDIA_URL, 'csv', "to_export/cuentas.csv")

            outfile = open(outfile_path, 'wb')
            writer = csv.writer(outfile)
            writer.writerow([
                'codigocuenta', 'ctaentidad', 'iban', 'horaalta', 'entidad',
                'horamod', 'codcliente', 'codpais', 'ctaagencia', 'bic',
                'codcuenta', 'idusuariomod', 'cuenta', 'fechaalta', 'fechamod',
                'idusuarioalta', 'ctadc', 'descripcion', 'agencia'
            ])

            for cta in cuentas:
                codcuenta = cta.codcuenta
                ctaentidad = cta.ctaentidad
                ctaagencia = cta.ctaagencia
                iban = cta.iban
                codcliente = cta.codcliente.pk
                codpais = cta.codpais
                entidad = cta.entidad
                codigocuenta = cta.codigocuenta
                ctadc = cta.ctadc
                bic = cta.bic
                cuenta = cta.cuenta
                idusuariomod = cta.codcliente.pk
                idusuarioalta = cta.codcliente.pk
                horaalta = ''
                horamod = ''
                fechaalta = ''
                fechamod = ''
                descripcion = ''
                agencia = ''

                writer.writerow([
                    codigocuenta, ctaentidad, iban, horaalta, entidad,
                    horamod, codcliente, codpais, ctaagencia, bic, codcuenta,
                    idusuariomod, cuenta, fechaalta, fechamod, idusuarioalta,
                    ctadc, descripcion, agencia
                ])

            outfile.close()
            cuenta_time = int(format(datetime.now(), 'U'))
            elapsed = cuenta_time - mobils_time
            print("Cuentas exportadas - %ss" % elapsed)

            # ------------------------------------------------------------

            direcciones = DirClientes.objects.filter(created_at__gte=before,
                                                     created_at__lt=now)

            direcciones = DirClientes.objects.all()
            print('NUM DIRECCIONS ', direcciones.count())

            outfile_path = os.path.join(
                settings.MEDIA_URL, 'csv', "to_export/dirclientes.csv")

            outfile = open(outfile_path, 'wb')
            writer = csv.writer(outfile)
            writer.writerow([
                'id', 'direccion', 'domenvio', 'descripcion', 'codcliente',
                'codpais', 'domfacturacion', 'provincia', 'apartado',
                'codpostal', 'idprovincia', 'ciudad'])

            for dir in direcciones:
                direccion = dir.direccion

                domenvio = dir.domenvio
                id = dir.id
                descripcion = ''
                codcliente = dir.codcliente.pk
                codpais = dir.codpais
                domfacturacion = dir.domfacturacion
                provincia = dir.provincia
                apartado = dir.apartado
                codpostal = dir.codpostal
                try:
                    idprovincia = str(dir.idprovincia.pk)
                except Exception as msg:
                    idprovincia = ''

                try:
                    ciudad = str(dir.ciudad)
                except Exception as msg:
                    ciudad = ''

                writer.writerow([
                    id, direccion, domenvio, descripcion, codcliente, codpais,
                    domfacturacion, provincia, apartado, codpostal,
                    idprovincia, ciudad
                ])

            outfile.close()
            dir_time = int(format(datetime.now(), 'U'))
            elapsed = dir_time - cuenta_time
            print("Direcciones exportadas - %ss" % elapsed)

            elapsed = int(format(datetime.now(), 'U')) - now
            return "Exportación terminada - %ss" % elapsed

        raise CommandError('Only the default is supported')
