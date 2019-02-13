from django.db import models
from datetime import datetime
from django.utils.dateformat import format
from tinymce.models import HTMLField
import uuid


class DatosEmpresa(models.Model):
    datos_empresa_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(
        max_length=300, null=True, blank=True,
        verbose_name='Nombre Empresa')
    cifnif = models.CharField(
        max_length=20, null=True, blank=True,
        verbose_name='CIF/NIF')
    phone = models.CharField(
        max_length=20, null=True, blank=True,
        verbose_name='Telefono')
    logo = models.FileField(
        verbose_name=("Logo Url"),
        upload_to='logo', null=True, blank=True)
    icon_logo = models.FileField(
        verbose_name=("Icono Logo Url"),
        upload_to='icon_logo', null=True, blank=True)
    mapa_cobertura = models.FileField(
        verbose_name=("Mapa Cobertura Url"),
        upload_to='mapa_cobertura', null=True, blank=True)
    city = models.CharField(
        max_length=300, null=True, blank=True,
        verbose_name='Ciudad')
    province = models.CharField(
        max_length=300, null=True, blank=True,
        verbose_name='Provincia')
    country = models.CharField(
        max_length=300, null=True, blank=True,
        verbose_name='Pais')
    zipcode = models.CharField(
        max_length=300, null=True, blank=True,
        verbose_name='Cod.Postal')
    address = models.CharField(
        max_length=300, null=True, blank=True,
        verbose_name='Direccion')
    location_lat = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True,
        verbose_name='Latitud')
    location_long = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True,
        verbose_name='Longitud')
    datos_empresa_default = models.BooleanField(
        default=False, verbose_name='Empresa por Defecto')
    social_twitter = models.CharField(
        max_length=300, null=True, blank=True, verbose_name='Twitter')
    social_facebook = models.CharField(
        max_length=300, null=True, blank=True, verbose_name='Facebook')

    updated_at = models.IntegerField(default=0, editable=False)
    created_at = models.IntegerField(default=0, editable=False)

    @property
    def textos(self):
        textos = InfoEmpresa.objects.filter(datos_empresa_fk=self.pk)
        return textos

    @property
    def configuracion_email(self):
        config = DatosEmail.objects.filter(
            datos_empresa_fk=self.pk, datos_email_default=True
        ).first()
        return config

    def __str__(self):
        return str(self.datos_empresa_id)

    class Meta:
        verbose_name = 'Datos Empresa'
        verbose_name_plural = 'Datos Empresa'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))

        if not self.created_at:
            self.created_at = self.updated_at

        if self.datos_empresa_default:
            DatosEmpresa.objects.all().update(datos_empresa_default=False)
            self.datos_empresa_default = True

        super(DatosEmpresa, self).save(*args, **kwargs)


class InfoEmpresa(models.Model):
    info_empresa_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    datos_empresa_fk = models.ForeignKey(
        DatosEmpresa, verbose_name='Datos Empresa',
        related_name='datos_empresa_fk', null=False,on_delete=models.CASCADE
    )
    key = models.CharField(max_length=200, null=True, blank=True)
    content = HTMLField(null=True, blank=True)
    image = models.FileField(
        verbose_name=("Info Empresa Imagen"),
        upload_to='info_empresa_image', null=True, blank=True)
    idioma = models.ForeignKey('internationalization.Idioma', null=True,on_delete=models.CASCADE)
    updated_at = models.IntegerField(default=0, editable=False)
    created_at = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return str(self.info_empresa_id)

    class Meta:
        verbose_name = 'Info Empresa'
        verbose_name_plural = 'Info Empresas'
        ordering = ['-created_at']
        unique_together = ['datos_empresa_fk', 'key', 'idioma']

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))
        if not self.created_at:
            self.created_at = self.updated_at
        super(InfoEmpresa, self).save(*args, **kwargs)


class TextosContrato(models.Model):
    textos_contrato_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    textos_contrato_default = models.BooleanField(
        default=False, verbose_name='Textos Contrato por Defecto')
    updated_at = models.IntegerField(default=0, editable=False)
    created_at = models.IntegerField(default=0, editable=False)

    @property
    def textos(self):
        textos = Texto.objects.filter(textos_contrato_fk=self.pk).order_by('-created_at')
        return textos

    def __str__(self):
        return str(self.textos_contrato_id)

    class Meta:
        verbose_name = 'Textos Contrato'
        verbose_name_plural = 'Textos Contratos'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))

        if not self.created_at:
            self.created_at = self.updated_at

        if self.textos_contrato_default:
            TextosContrato.objects.all().update(textos_contrato_default=False)
            self.textos_contrato_default = True

        super(TextosContrato, self).save(*args, **kwargs)


class Texto(models.Model):
    texto_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    textos_contrato_fk = models.ForeignKey(
        TextosContrato, verbose_name='Textos Contrato',
        related_name='textos_contrato_fk', null=False,on_delete=models.CASCADE
    )
    key = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    content = models.TextField(max_length=10000, blank=True, null=True)
    idioma = models.ForeignKey('internationalization.Idioma', null=True,on_delete=models.CASCADE)
    updated_at = models.IntegerField(default=0, editable=False)
    created_at = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return str(self.texto_id)

    class Meta:
        verbose_name = 'Texto Contrato'
        verbose_name_plural = 'Texto Contratos'
        ordering = ['-created_at']
        unique_together = ['textos_contrato_fk', 'key', 'idioma']

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))
        if not self.created_at:
            self.created_at = self.updated_at
        super(Texto, self).save(*args, **kwargs)


class DatosEmail(models.Model):
    datos_email_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    datos_empresa_fk = models.ForeignKey(
        DatosEmpresa, verbose_name='Datos Empresa',
        null=False,on_delete=models.CASCADE
    )
    email_receiver = models.CharField(
        max_length=50, null=True, blank=True,
        verbose_name='Email Envio')
    emailname_receiver = models.CharField(
        max_length=50, null=True, blank=True,
        verbose_name='Envio nombre')        
    email_sender = models.CharField(
        max_length=50, null=True, blank=True,
        verbose_name='Usuario SMTP')
    email_sender_password = models.CharField(
        max_length=50, null=True, blank=True,
        verbose_name='Password SMTP')
    server = models.CharField(
        max_length=50, null=True, blank=True,
        verbose_name='Servidor')
    port = models.IntegerField(
        default=25, null=True, blank=True,
        verbose_name='Puerto Servidor')
    datos_email_default = models.BooleanField(
        default=False, verbose_name='Datos Email por Defecto')

    updated_at = models.IntegerField(default=0, editable=False)
    created_at = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return str(self.datos_email_id)

    class Meta:
        verbose_name = 'Datos Email'
        verbose_name_plural = 'Datos Email'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))

        if not self.created_at:
            self.created_at = self.updated_at

        if self.datos_email_default:
            DatosEmail.objects.all().update(datos_email_default=False)
            self.datos_email_default = True

        super(DatosEmail, self).save(*args, **kwargs)
