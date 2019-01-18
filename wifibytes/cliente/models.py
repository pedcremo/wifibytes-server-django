# encoding:utf-8
import os
from django.db import models
from datetime import datetime, timedelta
from hashlib import md5
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime as thetime
from datetime import datetime, timedelta
from django.utils.dateformat import format
from django.utils.timezone import utc
import hashlib
import base64
import datetime as thetime
from catalogo.models import *
from django.conf import settings
from tinymce.models import HTMLField
# PDF
from django.views.generic import View
#from ho import pisa
from io import StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.files.base import ContentFile, File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.signals import post_save, pre_delete, post_delete
from wifibytes.omv_functions import cancelarSolicitud
from reportlab.pdfgen import canvas
import uuid
import logging
import time
logger = logging.getLogger(__name__)


class GruposCliente(models.Model):

    codtarifa = models.ForeignKey(
        Tarifa,
        related_name='GruposClientes_Tarifa',
        verbose_name=("Codigo tarifa"),on_delete=models.PROTECT
    )

    nombre = models.CharField(
        verbose_name=("Nombre"), max_length=100, blank=False)
    codgrupo = models.IntegerField(
        verbose_name=("Codigo Grupo"),
        primary_key=True,
        editable=False
    )

    def __unicode__(self):
        return str(self.codgrupo)

    def save(self, *args, **kwargs):

        if not self.codgrupo:

            no = GruposCliente.objects.count()

            if no == 0:
                self.codgrupo = 1
            else:
                self.codgrupo = self.__class__.objects.all().order_by(
                    "-codgrupo")[0].codgrupo + 1

        super(GruposCliente, self).save(*args, **kwargs)


class Cliente(models.Model):
    regimeniva_type = (
        (0, ('General')),
        (1, ('Excento')),
    )
    tipoidfiscal_type = (
        (0, ('NIF')),
        (1, ('NIF/IVA')),
        (2, ('Pasaporte')),
        (3, ('Doc. Oficial País')),
        (4, ('Cert.Residencia')),
        (5, ('Otro'))
    )
    tchoices = ((0, 'No'), (1, 'Si'))
    tipos_cliente = ((0, 'RESIDENCIAL'),
                     (1, 'EMPRESA'), (5, 'AUTONOMO'), (2, 'EXTRANJERO'))
    tipos_documento = ((0, 'DNI'), (1, 'NIE'),
                       (4, 'CIF'), (2, 'PASAPORTE'))
    generos = (('H', 'Hombre'), ('M', 'Mujer'))

    codcliente = models.CharField(
        primary_key=True, default=False, editable=False, max_length=100)
    nombre = models.CharField(
        verbose_name=("Nombre"), max_length=100, blank=False)
    apellido = models.CharField(
        verbose_name=("Apellido"), max_length=100, blank=False)
    segundo_apellido = models.CharField(
        verbose_name=("Segundo Apellido"), max_length=100, blank=True,
        null=True)
    email = models.CharField(verbose_name=("Email"), max_length=50, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True,
                              choices=generos)
    nombrecomercial = models.CharField(
        verbose_name=("Nombre Comercial"), max_length=100, null=True,
        blank=True)
    cifnif = models.CharField(
        verbose_name=("Cif Nif"), max_length=12, blank=False)
    cifnif_imageA = models.FileField(
        upload_to="cliente_data", verbose_name=("CIFNIF CARA A"),
        blank=True, null=True)
    cifnif_imageB = models.FileField(
        upload_to="cliente_data", verbose_name=("CIFNIF CARA B"),
        blank=True, null=True)
    dni_apoderado = models.CharField(blank=True, null=True, max_length=50)
    fecha_registro = models.DateTimeField(
        verbose_name=("Suscripción"), editable=False)
    telefono = models.CharField(
        verbose_name=("Telefono"), max_length=30, null=True, blank=True)
    tipo_cliente = models.IntegerField(null=False, default=0, blank=False,
                                       choices=tipos_cliente)
    tipo_documento = models.IntegerField(null=False, default=0, blank=False,
                                         choices=tipos_documento)
    password = models.CharField(
        verbose_name=("Password"), max_length=70, null=True, blank=True)

    codcuentadom = models.ForeignKey(
        'cliente.CuentasbcoCli', verbose_name="Cuenta Domiciliacion",
        null=True,on_delete=models.SET_NULL)
    debaja = models.NullBooleanField(default=None, editable=False,
                                     null=True)  # para facturar

    consumer_user = models.OneToOneField(
        User, related_name='rel_Codcliente', editable=False,
        verbose_name=("Consumer User"), on_delete=models.SET_NULL, null=True)

    observaciones = HTMLField(null=True, blank=True)

    tipoidfiscal_type = models.IntegerField(verbose_name=(
        "Tipo Identificación Fiscal"), choices=tipoidfiscal_type, null=True,
        blank=True)
    token = models.CharField(max_length=300, null=True, blank=True)
    is_active = models.BooleanField(default=False,  editable=True, null=False)

    newsletter = models.BooleanField(default=False,  editable=True, null=False)

    subscriberType_omv = models.IntegerField(
        editable=True, null=True, blank=True)
    marketingConsent_omv = models.IntegerField(
        editable=True, null=True, blank=True)
    documentType_omv = models.IntegerField(
        editable=True, null=True, blank=True)
    fiscalId_omv = models.IntegerField(editable=True, null=True, blank=True)
    birthday_omv = models.DateField(verbose_name="Fecha de nacimiento",
                                    editable=True, null=True, blank=True)

    consumerContract = models.FileField(
        verbose_name="Contrato Cliente", upload_to="client_contract",
        null=True, editable=False)
    consumerSigned = models.IntegerField(
        verbose_name="Info revisada, ¿Se puede proceder con la firma?",
        default=0, choices=tchoices)
    created_at = models.IntegerField(default=0, editable=False)
    updated_at = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
        return str(self.nombre) + " " + str(self.apellido)

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))

        if not self.created_at:
            self.created_at = int(format(datetime.now(), 'U'))
            self.fecha_registro = thetime.datetime.utcnow().replace(
                tzinfo=utc, microsecond=0) + timedelta(days=30)

            if not self.codcliente:  # si el usuario no esta importado
                no = Cliente.objects.count()
                if no == 0:
                    self.codcliente = 900000
                else:
                    actual = int(self.__class__.objects.all().order_by(
                        "-codcliente")[0].codcliente)
                    if actual < 900000:
                        nuevo = 900000
                    else:
                        nuevo = actual + 1
                    self.codcliente = str(nuevo)
                    self.is_active = True

        if self.consumer_user is None:
            try:
                user = User.objects.get(username=self.codcliente)
            except User.DoesNotExist:
                user = User.objects.create_user(
                    self.codcliente, self.email, self.password)
                user.save()

            self.consumer_user = user

        if self.password != '':
            user = self.consumer_user
            user.set_password(self.password)
            user.save()
            self.password = ''

        super(Cliente, self).save(*args, **kwargs)


class CuentasbcoCli(models.Model):
    ctaentidad = models.CharField(
        verbose_name=("Cuenta Entidad"), max_length=4, null=True, blank=True)
    iban = models.CharField(
        verbose_name=("IBAN"), max_length=34, null=True, blank=True)
    codiban = models.CharField(max_length=4, null=True, blank=True)
    horaalta = models.DateField(
        verbose_name=("Fecha Creación"), null=True, blank=True)
    entidad = models.CharField(
        verbose_name=("Entidad"), max_length=100, null=True, blank=True)
    direntidad = models.CharField(
        verbose_name=("Entidad"), max_length=150, null=True, blank=True)
    horamod = models.DateTimeField(
        verbose_name=("Fecha Modificación"), null=True, blank=True)
    codcliente = models.ForeignKey(Cliente,  related_name='cuentasbco_cliente',on_delete=models.PROTECT)

    codigocuenta = models.CharField(
        verbose_name=("Codigo Cuenta"), max_length=30, blank=False, null=True)
    codpais = models.CharField(
        verbose_name=("Codigo Pais"), max_length=20, blank=True, null=True)
    ctaagencia = models.CharField(max_length=4, blank=True, null=True)
    bic = models.CharField(
        verbose_name=("BIC"), max_length=11, null=True, blank=True)
    titular = models.CharField(max_length=200, null=True, blank=True)
    codcuenta = models.IntegerField(primary_key=True, editable=False)

    idusuariomod = models.CharField(
        verbose_name=("Id usuario "), max_length=50, null=True, blank=True)
    cuenta = models.CharField(
        verbose_name=("Cuenta"), max_length=10, null=True, blank=True)
    fechaalta = models.DateField(
        verbose_name=("Fecha Alta"), null=True, blank=True)
    fechamod = models.DateField(
        verbose_name=("Fecha Mod"), null=True, blank=True)
    idusuarioalta = models.CharField(
        verbose_name=("Id Usuario Alta"), max_length=50, null=True, blank=True)
    ctadc = models.CharField(
        verbose_name=("CTADC"), max_length=2, null=True, blank=True)
    created_at = models.IntegerField(default=0, editable=False)
    updated_at = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
        return str(self.codcuenta)

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))

        if not self.codcuenta:
            self.created_at = int(format(datetime.now(), 'U'))

            try:  # si existen modificaciones
                currentObject = CuentasbcoCli.objects.get(
                    codcuenta=self.codcuenta
                )
            except CuentasbcoCli.DoesNotExist:
                no = CuentasbcoCli.objects.count()

                if no == 0:
                    self.codcuenta = 1
                else:
                    actual = self.__class__.objects.all().order_by(
                        "-codcuenta")[0].codcuenta
                    if actual < 900000:
                        nuevo = 900000
                    else:
                        nuevo = actual + 1
                    self.codcuenta = nuevo

        super(CuentasbcoCli, self).save(*args, **kwargs)


class DirClientes(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    codcliente = models.ForeignKey(
        Cliente, verbose_name=("Codigo Cliente"),
        related_name='DirClientes_Cliente',on_delete=models.PROTECT)
    domenvio = models.BooleanField(
        default=False, verbose_name=("Domicilio de Envio"), blank=False,
        null=False)
    domfacturacion = models.BooleanField(
        verbose_name=("Datos de Facturación"), default=False, blank=False,
        null=False)
    nombre = models.CharField(
        verbose_name=("Nombre / Empresa"), max_length=250, default=None,
        blank=True, null=True)
    cifnif = models.CharField(
        verbose_name=("DNI/CIF/NIE"), max_length=10, default=None, blank=True,
        null=True)
    direccion = models.CharField(
        verbose_name=("Dirección"), max_length=350, blank=False, null=False)
    numero = models.CharField(blank=True, null=False, max_length=350)
    codpais = models.CharField(
        verbose_name=("Codigo de Pais"), max_length=100, blank=True,
        null=True, default='ES')
    ciudad = models.CharField(
        verbose_name=("Ciudad"), max_length=100, blank=False, null=False)
    provincia = models.CharField(
        verbose_name=("Provincia"), max_length=100, null=True, blank=True)
    idprovincia = models.ForeignKey('geo.Provincia', related_name="dir_prov",
                                    verbose_name="Id Provincia", null=True,on_delete=models.SET_NULL)
    apartado = models.CharField(
        verbose_name=("Apartado"), max_length=10, null=True, blank=True)
    codpostal = models.CharField(
        verbose_name=("Codigo Postal"), max_length=10, null=True)
    telefono = models.IntegerField(
        verbose_name=("Teléfono de contacto"), null=True)
    default = models.BooleanField(default=False)
    created_at = models.IntegerField(default=0, editable=False)
    updated_at = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))
        if self.pk is None:
            self.created_at = int(format(datetime.now(), 'U'))
            no = self.__class__.objects.all().order_by("-id")
            if no.count() == 0:
                self.id = 900000
            else:
                actual = no[0].id
                self.id = 900000 if actual < 900000 else (actual + 1)

        if self.idprovincia and self.provincia != self.idprovincia.provincia:
            self.provincia = self.idprovincia.provincia

        super(DirClientes, self).save(*args, **kwargs)


class MobilsClients(models.Model):

    tipoTarifa = (
        (0, ('Contrato')),
        (1, ('Tarjeta'))
    )

    tipoSimChoice = (
        (0, ('Sim')),
        (1, ('Microsim')),
        (2, ('Nanosim'))
    )

    companias = (
        (0, ('Movistar')),
        (1, ('Vodafone')),
        (2, ('Orange')),
        (3, ('Yoigo')),
        (4, ('Pepephone')),
        (5, ('Simyo'))
    )

    tipoClienteChoices = (
        (0, ('Particular')),
        (1, ('Autónomo')),
        (2, ('Empresa'))
    )

    tipoOrigen = (
        (0, 'Alta'), (1, 'Portabilidad')
    )

    id_mobilsclients = models.IntegerField(
        primary_key=True, editable=False)
    mobil = models.CharField(
        verbose_name=("Móvil"), max_length=20, blank=True, null=True)
    nuevoicc = models.CharField(null=True, blank=True, max_length=50)
    codcliente = models.ForeignKey(
        Cliente, verbose_name=("Codigo Cliente"),
        related_name='MobilsClients_Cliente',on_delete=models.PROTECT)
    codcuenta = models.ForeignKey(
        CuentasbcoCli, verbose_name=("Cuenta Cliente"),
        related_name='MobilsClients_CuentasbcoCli', null=True, blank=True,on_delete=models.SET_NULL)
    codtarifa = models.ForeignKey(
        Tarifa, verbose_name=("Codigo Tarifa"),
        related_name='MobilsClients_Tarifa',on_delete=models.PROTECT)
    fechaContrato = models.DateField(
        verbose_name=("Fecha Contrato"), null=True, blank=True)
    imageContrato = models.FileField(
        upload_to="cliente_data", verbose_name=("Image Contrato"),
        null=True, blank=True)
    roaming = models.BooleanField(default=False, null=False)
    roaming_procesing = models.BooleanField(default=False, null=False)
    buzon_voz = models.BooleanField(default=False, null=False)
    buzon_voz_procesing = models.BooleanField(default=False, null=False)
    coddir = models.ForeignKey(
        DirClientes, verbose_name=("Datos de Facturación"),
        related_name="MobilsClients_DirClientes", null=True, blank=True,on_delete=models.SET_NULL)
    origen = models.IntegerField(null=False, blank=False, choices=tipoOrigen,
                                 default=0)
    tipoTarifaAntigua = models.IntegerField(verbose_name=(
        "Tipo de tarifa anterior"), choices=tipoTarifa, null=True, blank=True)
    tipoSim = models.IntegerField(verbose_name=(
        "Tipo de Sim"), choices=tipoSimChoice, null=True, blank=True)
    companiaAnterior = models.IntegerField(verbose_name=(
        "Compañía anterior"), choices=companias, null=True, blank=True)
    icc_anterior = models.CharField(null=True, blank=True, max_length=50)
    dc_icc_anterior = models.CharField(null=True, blank=True, max_length=2)
    activa = models.BooleanField(verbose_name=("Línea activa"), default=False)
    alta = models.BooleanField(verbose_name=("Línea dada de alta"),
                               default=False)
    omv_solicitud = models.CharField(verbose_name="N. de solicitud",
                                     max_length=100, null=True, blank=True)
    signature_id = models.CharField(null=True, blank=True, max_length=500)
    document_id = models.CharField(null=True, blank=True, max_length=500)
    created_at = models.IntegerField(default=0, editable=False)
    updated_at = models.IntegerField(default=0, editable=False)
    draft = models.BooleanField(verbose_name=("Borrador"), default=True)

    class Meta:
        verbose_name = "Línea"
        verbose_name_plural = "Líneas"

    def __unicode__(self):
        return str(self.id_mobilsclients)

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))

        if not self.created_at:
            self.created_at = int(format(datetime.now(), 'U'))
            if not self.id_mobilsclients:
                no = MobilsClients.objects.count()
                if no == 0:
                    self.id_mobilsclients = 900000
                else:
                    actual = self.__class__.objects.all().order_by(
                        "-id_mobilsclients")[0].id_mobilsclients
                    if actual < 900000:
                        nuevo = 900000
                    else:
                        nuevo = actual + 1
                    self.id_mobilsclients = nuevo
        else:
            old = MobilsClients.objects.get(pk=self.pk)
            if self.buzon_voz != old.buzon_voz:
                buzon_voz_procesing = True
                # LLamada Activar buzon_boz background
            if self.roaming != old.roaming:
                roaming = True
                # LLamada Activar roaming background
            if not self.mobil:
                self.mobil = self.codcliente.telefono
                try:
                    self.mobil = "Pendiente " + str(time.strftime("%d/%m/%Y"))
                except Exception as error:
                    self.mobil = self.codcliente.telefono

        super(MobilsClients, self).save(*args, **kwargs)


class Servicio(models.Model):
    servicio_id = models.IntegerField(primary_key=True, editable=False)
    servicio_compania_anterior = models.CharField(
        verbose_name=("Compañia anterior"), max_length=250, null=True)
    servicio_telefono_anterior = models.IntegerField(
        verbose_name=("Teléfono anterior"), null=True)
    servicio_draft = models.BooleanField(verbose_name=("Borrador"),
                                         default=False)
    created_at = models.IntegerField(default=0, editable=False)
    updated_at = models.IntegerField(default=0, editable=False)
    servicio_activo = models.BooleanField(verbose_name=("Activo"),
                                          default=False)
    servicio_consumer = models.ForeignKey(Cliente, null=False,
                                          verbose_name=("Cliente"),
                                          blank=False,on_delete=models.PROTECT)
    servicio_direccion = models.ForeignKey(DirClientes, null=True,
                                           verbose_name=("Dirección"),
                                           blank=False,on_delete=models.SET_NULL)
    servicio_tarifa = models.ForeignKey('catalogo.Tarifa', null=False,
                                        verbose_name=("Tarifa"),
                                        blank=False,on_delete=models.PROTECT)
    servicio_cuenta = models.ForeignKey(CuentasbcoCli, null=True, blank=False,on_delete=models.SET_NULL)

    def __unicode__(self):
        return str(self.servicio_id)

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))
        if not self.servicio_id:
            self.created_at = int(format(datetime.now(), 'U'))
            no = self.__class__.objects.count()
            if no == 0:
                self.servicio_id = 1
            else:
                self.servicio_id = self.__class__.objects.all(
                ).order_by("-servicio_id")[0].servicio_id + 1

        super(Servicio, self).save(*args, **kwargs)


def delete_user(sender, instance, **kwargs):
    print("IN")
    try:
        instance.consumer_user.delete()
        print((str(instance.consumer_user) + ' DELETED'))
    except Exception:
        pass


pre_delete.connect(
    delete_user, sender=Cliente, dispatch_uid="delete_user")


def delete_consumer(sender, instance, **kwargs):
    orphan_consumers = Cliente.objects.filter(consumer_user=None).delete()


post_delete.connect(delete_consumer, sender=User,
                    dispatch_uid="delete_consumer")
