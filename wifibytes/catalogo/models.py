# encoding:utf-8
from django.core.files import File
from django.db import models
from django.template.defaultfilters import slugify
from PIL import Image as Img
from datetime import datetime
from django.utils.dateformat import format
from tinymce.models import HTMLField
import uuid
from io import StringIO
from django.db.models import Prefetch


class Familia(models.Model):
    codfamilia = models.CharField(verbose_name='Código Familia',
                                  primary_key=True, editable=True,
                                  max_length=4)
    slug = models.SlugField(editable=False)
    nombre = models.CharField(verbose_name="Nombre [ES]", max_length=200, blank=False)
    nombre_va = models.CharField(verbose_name="Nombre [VA]", max_length=200, blank=True)
    color = models.ForeignKey('pagina.PaletaColores',
                              related_name='Familia_PaletaColores', on_delete=models.PROTECT)
    icono = models.FileField(upload_to="familia")
    pretitulo = models.CharField(verbose_name="Pretitulo [ES]", max_length=200, blank=False)
    pretitulo_va = models.CharField(verbose_name="Pretitulo [VA]", max_length=200, blank=True)
    titulo = models.CharField(verbose_name="Titulo [ES]", max_length=200, blank=False)
    titulo_va = models.CharField(verbose_name="Titulo [VA]", max_length=200, blank=True)
    precio_cabecera = models.FloatField(null=True, blank=False)
    imagen_cabecera = models.FileField(null=True, upload_to="familia")
    thumbnail = models.FileField(
        null=True, upload_to="familia", editable=False)
    activo = models.BooleanField(default=False, editable=True, null=False)
    texto_cabecera = HTMLField(verbose_name="Texto cabecera [ES]",)
    texto_cabecera_va = HTMLField(verbose_name="Texto cabecera [VA]", blank=True)
    subtexto_cabecera = HTMLField(verbose_name="Subtexto cabecera [ES]")
    subtexto_cabecera_va = HTMLField(verbose_name="Subtexto cabecera [VA]", blank=True)
    created_at = models.IntegerField(default=0, editable=False)
    updated_at = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
        return str(self.nombre)

    class Meta:
        index_together = ['codfamilia', 'nombre']

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))
        self.slug = slugify(self.nombre)

        if not self.codfamilia:
            self.created_at = int(format(datetime.now(), 'U'))
            self.codfamilia = "%s" % (uuid.uuid4(),)

        try:
            orig = Familia.objects.get(pk=self.pk)
        except Familia.DoesNotExist:
            orig = None

        if orig is None or orig.imagen_cabecera != self.imagen_cabecera:
            try:
                # Image Variables
                if self.imagen_cabecera:
                    imagename = str(uuid.uuid1().hex) + '.PNG'
                    print('triying image')
                    image = Img.open(
                        StringIO.StringIO(self.imagen_cabecera.read()))
                    width, height = image.size
                    # horizontal 585
                    if width >= height:
                        new_height = 585
                        new_width = width * new_height / height
                    # vertical 560
                    else:
                        new_height = 560
                        new_width = width * new_height / height
                    temp_img = image.resize(
                        (new_width, new_height), Img.LANCZOS)
                    print((temp_img.size))
                    output = StringIO.StringIO()
                    temp_img.save(output, format='PNG', optimize=True)
                    output.seek(0)
                    new_img = File(output, imagename)
                    self.thumbnail = new_img
            except Exception:
                print('ERROR: Error on team image')

        super(Familia, self).save(*args, **kwargs)


class Marca(models.Model):
    Marca = models.CharField(max_length=100, blank=False, null=False)
    id = models.IntegerField(primary_key=True, editable=False)

    def __unicode__(self):
        return self.Marca

    def save(self, *args, **kwargs):
        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1

        super(self.__class__, self).save(*args, **kwargs)


class Pantalla(models.Model):
    num_pantalla = models.FloatField(blank=False, null=False)
    id = models.IntegerField(primary_key=True, editable=False)

    def __unicode__(self):
        return str(self.num_pantalla)

    def save(self, *args, **kwargs):
        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1

        super(self.__class__, self).save(*args, **kwargs)


class Procesador(models.Model):
    num_procesador = models.CharField(max_length=100, blank=False, null=False)
    id = models.IntegerField(primary_key=True, editable=False)

    def __unicode__(self):
        return str(self.num_procesador)

    def save(self, *args, **kwargs):
        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1

        super(self.__class__, self).save(*args, **kwargs)


class Ram(models.Model):
    num_ram = models.CharField(max_length=100, blank=False, null=False)
    id = models.IntegerField(primary_key=True, editable=False)

    def __unicode__(self):
        return str(self.num_ram)

    def save(self, *args, **kwargs):
        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1

        super(self.__class__, self).save(*args, **kwargs)


class Camara(models.Model):
    num_camara = models.FloatField(blank=False, null=False)
    id = models.IntegerField(primary_key=True, editable=False)

    def __unicode__(self):
        return str(self.num_camara)

    def save(self, *args, **kwargs):
        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1

        super(self.__class__, self).save(*args, **kwargs)


class Articulo(models.Model):
    tipocodbarras_type = (
        ('Code39', ('Code39')), ('Code128', ('Code128')),
        ('Code128B', ('Code128B')), ('Code128C', ('Code128C')),
        ('Code128R', ('Code128R')), ('EAN', ('EAN')), ('ISBN', ('ISBN')),
        ('UPC', ('UPC')), ('CodeI25', ('CodeI25')), ('CBR', ('CBR')),
        ('MSI', ('MSI')), ('PLS', ('PLS')), ('Code93', ('Code93')))

    template_type = (
        (1, ('Template 1')), (2, ('Template 2')), (3, ('Template 3')))

    # Campos Altrebit y Eneboo
    referencia = models.CharField(
        primary_key=True, editable=False, max_length=100)

    slug = models.SlugField(editable=False)
    codfamilia = models.ForeignKey(Familia, related_name='familia_codfamilia',
                                   null=False, blank=False, on_delete=models.PROTECT)
    descripcion = models.CharField(verbose_name="Descripción [ES]",
                                   max_length=250, blank=False, null=False)
    descripcion_va = models.CharField(verbose_name="Descripción [VA]",
                                      max_length=250, blank=True)
    pvp = models.FloatField(null=False, blank=False, default=0)
    stockfis = models.FloatField(null=False, blank=False, default=0)

    # Campos exclusivos Altrebit
    descripcion_breve = models.CharField(verbose_name="Descripción breve [ES]",
                                         max_length=250, blank=False,
                                         null=False)
    descripcion_breve_va = models.CharField(
        verbose_name="Descripción breve [VA]", max_length=250, blank=True)
    descripcion_larga = HTMLField(verbose_name="Especificaciones [ES]",
                                  blank=False, null=False)
    descripcion_larga_va = HTMLField(verbose_name="Especificaciones [VA]",
                                     blank=True)
    template = models.IntegerField(verbose_name="Template Seleccionado",
                                   choices=template_type, null=False,
                                   blank=False, editable=True)

    imagen = models.FileField(upload_to="pagina_tarifas",
                              verbose_name="Imagen")
    thumbnail = models.FileField(upload_to="pagina_tarifas",
                                 verbose_name="thumbnail")

    activo = models.BooleanField(verbose_name="Artículo Activo", null=False,
                                 default=0)
    visible = models.BooleanField(default=False, blank=False, null=False)

    marca = models.ForeignKey(Marca, related_name='Articulo_Marca',
                              blank=False, on_delete=models.PROTECT)
    pantalla = models.ForeignKey(Pantalla, related_name='Articulo_Pantalla',
                                 blank=True, null=True, on_delete=models.SET_NULL)
    procesador = models.ForeignKey(Procesador,
                                   related_name='Articulo_Procesador',
                                   blank=True, null=True, on_delete=models.SET_NULL)
    ram = models.ForeignKey(Ram, related_name='Articulo_Ram', blank=True,
                            null=True, on_delete=models.SET_NULL)
    camara = models.ForeignKey(Camara, related_name='Articulo_Camara',
                               blank=True, null=True, on_delete=models.SET_NULL)
    destacado = models.BooleanField(default=False,  editable=True, null=False)

    # Campos exclusivos Eneboo
    secompra = models.BooleanField(default=True, null=False, blank=False)
    stockmax = models.FloatField(null=False, blank=False, default=0)
    codimpuesto = models.CharField(max_length="10", null=True,
                                   default="IVA21%")
    observaciones = models.TextField(null=True, blank=True)
    codbarras = models.CharField(verbose_name="Codigo Barras", max_length=18,
                                 null=True, blank=True)
    nostock = models.BooleanField(default=False, null=False, blank=False)
    controlstock = models.BooleanField(default=False, null=False, blank=False)
    tipocodbarras = models.CharField(max_length=8, choices=tipocodbarras_type,
                                     null=True, blank=True)
    sevende = models.BooleanField(default=True, null=False, blank=False)
    venta_online = models.BooleanField(default=True, null=False, blank=False)
    stockmin = models.FloatField(null=False, blank=False, default=0)
    created_at = models.IntegerField(default=0, editable=False)
    updated_at = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
        return str(self.referencia) + " - " + str(self.descripcion)

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))
        self.slug = slugify(self.descripcion)

        try:  # si existen modificaciones
            currentObject = Articulo.objects.get(referencia=self.referencia)
        except Articulo.DoesNotExist:
            if not self.referencia:
                self.created_at = int(format(datetime.now(), 'U'))
                self.referencia = "%s" % (uuid.uuid4(),)
        try:
            orig = Articulo.objects.get(pk=self.pk)
        except Articulo.DoesNotExist:
            orig = None

        if orig is None or orig.imagen != self.imagen:
            try:
                # Image Variables
                if self.imagen:
                    imagename = str(uuid.uuid1().hex) + '.PNG'
                    print('triying image')
                    image = Img.open(StringIO.StringIO(self.imagen.read()))
                    width, height = image.size
                    # horizontal 220
                    if width >= height:
                        new_height = 220
                        new_width = width * new_height / height
                    # vertical 300
                    else:
                        new_height = 300
                        new_width = width * new_height / height
                    temp_img = image.resize(
                        (new_width, new_height), Img.LANCZOS)
                    output = StringIO.StringIO()
                    temp_img.save(output, format='PNG', optimize=True)
                    output.seek(0)
                    new_img = File(output, imagename)
                    self.thumbnail = new_img

            except Exception:
                print('ERROR: Error on team image')

        super(Articulo, self).save(*args, **kwargs)


class Tarifa(models.Model):

    codtarifa = models.IntegerField(primary_key=True, editable=False)
    nombretarifa = models.CharField(verbose_name="Nombre tarifa",
                                    max_length=100)
    slug = models.SlugField(editable=False)
    pretitulo = models.CharField(verbose_name="Pretitulo [ES]", max_length=100,
                                 blank=False)
    pretitulo_va = models.CharField(verbose_name="Pretitulo [VA]",
                                    max_length=100, blank=True)
    logo = models.FileField(upload_to="Logo")
    precio = models.FloatField(verbose_name=("Importe tarifa "), blank=False)
    activo = models.BooleanField(verbose_name="Activo", null=False, default=0)
    destacado = models.BooleanField(default=False, editable=True, null=False)
    color = models.ForeignKey('pagina.PaletaColores',
                              related_name='Tarifa_PaletaColores', null=True, on_delete=models.SET_NULL)
    created_at = models.IntegerField(default=0, editable=False)
    updated_at = models.IntegerField(default=0, editable=False)

    def get_queryset(self):
        subtarifas = Subtarifa.objects.filter(
            subtarifa_tarifa=self).select_related('subtarifa_tarifa')
        return super(Tarifa, self).get_queryset().prefetch_related(
            Prefetch('subtarifa_tarifa', queryset=subtarifas,
                     to_attr='subtarifa_tarifa'))

    @property
    def getSubtarifas(self):
        subtarifas = Subtarifa.objects.filter(
            subtarifa_tarifa=self)
        return subtarifas

    def __unicode__(self):
        return str(self.codtarifa)

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))
        self.slug = slugify(self.nombretarifa)
        if not self.codtarifa:
            self.created_at = int(format(datetime.now(), 'U'))
            no = self.__class__.objects.count()
            if no == 0:
                self.codtarifa = 1
            else:
                self.codtarifa = self.__class__.objects.all().order_by(
                    "-codtarifa")[0].codtarifa + 1

        super(self.__class__, self).save(*args, **kwargs)


class Subtarifa(models.Model):

    rate_type = (
        (1, ('Móvil')), (2, ('Fijo')), (3, ('Fibra')), (4, ('Wifi')),
        (5, ('TV')))

    subtarifa_id = models.IntegerField(primary_key=True, editable=False)
    subtarifa_datos_internet = models.FloatField(
        verbose_name=("Importe Datos"), blank=True, null=True)
    subtarifa_cent_minuto = models.FloatField(
        verbose_name=("Importe minutos (cent/min)"), blank=True, null=True)
    subtarifa_est_llamada = models.FloatField(blank=True, null=True)
    subtarifa_precio_sms = models.FloatField(
        verbose_name=("Importe sms"), blank=True, null=True)
    subtarifa_velocidad_conexion_subida = models.FloatField(
        verbose_name=("Velocidad de conexión subida"), blank=True, null=True)
    subtarifa_velocidad_conexion_bajada = models.FloatField(
        verbose_name=("Velocidad de conexión bajada"), blank=True, null=True)
    subtarifa_num_canales = models.IntegerField(blank=True, null=True)
    subtarifa_minutos_gratis = models.IntegerField(
        verbose_name=("Minutos gratis"), blank=True, null=True)
    subtarifa_minutos_ilimitados = models.BooleanField(
        default=False, null=False)
    subtarifa_siglas_omv = models.CharField(
        verbose_name="Siglas de la tarifa", max_length=100, blank=True,
        null=True)
    subtarifa_omv = models.ForeignKey(
        'omv.Omv', verbose_name="Omv asociado a Tarifa",
        null=True, blank=True, on_delete=models.SET_NULL)
    tipo_tarifa = models.IntegerField(
        null=False, default=0, blank=False, choices=rate_type)
    subtarifa_tarifa = models.ForeignKey(
        Tarifa, related_name='subtarifa_tarifa', verbose_name="Tarifa",
        blank=False, on_delete=models.PROTECT)
    created_at = models.IntegerField(default=0, editable=False)
    updated_at = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
        return str(self.subtarifa_id)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subtarifa_id)
        self.updated_at = int(format(datetime.now(), 'U'))
        if not self.subtarifa_id:
            self.created_at = int(format(datetime.now(), 'U'))
            no = self.__class__.objects.count()
            if no == 0:
                self.subtarifa_id = 1
            else:
                self.subtarifa_id = self.__class__.objects.all().order_by(
                    "-subtarifa_id")[0].subtarifa_id + 1

        super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Paquete Tarifa"
        verbose_name_plural = "Paquetes Tarifa"


class Template1(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    articulo = models.ForeignKey(
        "catalogo.Articulo", related_name='template1_articulo', on_delete=models.PROTECT)
    pretitulo = models.CharField(verbose_name=(
        "pretitulo"), max_length=100, null=True, blank=True)
    caja_1_titulo = models.CharField(verbose_name=(
        "caja_1_titulo"), max_length=100, null=True, blank=True)
    caja_1_texto = HTMLField(blank=True, null=True)
    caja_2_titulo = models.CharField(verbose_name=(
        "caja_2_titulo"), max_length=100, null=True, blank=True)
    caja_2_texto = HTMLField(blank=True, null=True)
    caja_3_titulo = models.CharField(verbose_name=(
        "caja_3_titulo"), max_length=100, null=True, blank=True)
    caja_3_texto = HTMLField(blank=True, null=True)
    caja_4_titulo = models.CharField(verbose_name=(
        "caja_4_titulo"), max_length=100, null=True, blank=True)
    caja_4_texto = HTMLField(blank=True, null=True)
    imagen1 = models.FileField(
        upload_to="Templates", verbose_name="Imagen1", blank=True, null=True)
    imagen2 = models.FileField(
        upload_to="Templates", verbose_name="Imagen2", blank=True, null=True)
    imagen3 = models.FileField(
        upload_to="Templates", verbose_name="Imagen3", blank=True, null=True)
    imagen_fondo_cabecera = models.FileField(
        upload_to="Templates", verbose_name="imagen_fondo_cabecera",
        blank=True, null=True)
    imagen_fondo_cuerpo = models.FileField(
        upload_to="Templates", verbose_name="imagen_fondo_cuerpo",
        blank=True, null=True)
    idioma = models.ForeignKey('internationalization.Idioma', null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1

        super(Template1, self).save(*args, **kwargs)


class Template2(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    articulo = models.ForeignKey(
        "catalogo.Articulo", related_name='template2_articulo',  on_delete=models.PROTECT)
    pretitulo = models.CharField(verbose_name=(
        "pretitulo"), max_length=100, null=True, blank=True)
    caja_1_titulo = models.CharField(verbose_name=(
        "caja_1_titulo"), max_length=100, null=True, blank=True)
    caja_1_texto = HTMLField(null=True, blank=True)
    caja_2_titulo = models.CharField(verbose_name=(
        "caja_2_titulo"), max_length=100, null=True, blank=True)
    caja_2_texto = HTMLField(blank=True, null=True)
    caja_3_titulo = models.CharField(verbose_name=(
        "caja_3_titulo"), max_length=100, null=True, blank=True)
    caja_3_texto = HTMLField(null=True, blank=True)
    caja_4_titulo = models.CharField(verbose_name=(
        "caja_4_titulo"), max_length=100, null=True, blank=True)
    caja_4_texto = HTMLField(blank=True, null=True)
    imagen1 = models.FileField(
        upload_to="Templates", verbose_name="Imagen1", blank=True, null=True)
    imagen2 = models.FileField(
        upload_to="Templates", verbose_name="Imagen2", blank=True, null=True)
    imagen3 = models.FileField(
        upload_to="Templates", verbose_name="Imagen3", blank=True, null=True)
    imagen4 = models.FileField(
        upload_to="Templates", verbose_name="Imagen4", blank=True, null=True)
    imagen_fondo_cabecera = models.FileField(
        upload_to="Templates", verbose_name="imagen_fondo_cabecera",
        blank=True, null=True)
    imagen_fondo_cuerpo = models.FileField(
        upload_to="Templates", verbose_name="imagen_fondo_cuerpo",
        blank=True, null=True)
    idioma = models.ForeignKey('internationalization.Idioma', null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1

        super(Template2, self).save(*args, **kwargs)


class Template3(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    articulo = models.ForeignKey(
        "catalogo.Articulo", related_name='template3_articulo', on_delete=models.PROTECT)
    pretitulo = models.CharField(verbose_name=(
        "pretitulo"), max_length=100, blank=True, null=True)
    franja_1_texto = HTMLField(blank=True, null=True)
    franja_1_fondo = models.FileField(
        upload_to="Templates", verbose_name="imagen_fondo_cabecera",
        blank=True, null=True)
    caja_1_titulo = models.CharField(verbose_name=(
        "caja_1_titulo"), max_length=100, blank=True, null=True)
    caja_1_texto = HTMLField(blank=True, null=True)
    caja_2_titulo = models.CharField(verbose_name=(
        "caja_2_titulo"), max_length=100, blank=True, null=True)
    caja_2_texto = HTMLField(blank=True, null=True)
    franja_2_texto = HTMLField(blank=True, null=True)
    franja_2_fondo = models.FileField(
        upload_to="Templates", verbose_name="imagen_fondo_cabecera",
        blank=True, null=True)
    imagen1 = models.FileField(
        upload_to="Templates", verbose_name="Imagen1",
        blank=True, null=True)
    imagen2 = models.FileField(
        upload_to="Templates", verbose_name="Imagen2", blank=True, null=True)
    imagen3 = models.FileField(
        upload_to="Templates", verbose_name="Imagen3", blank=True, null=True)
    imagen4 = models.FileField(
        upload_to="Templates", verbose_name="Imagen4", blank=True, null=True)
    idioma = models.ForeignKey('internationalization.Idioma', null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all(
                ).order_by("-id")[0].id + 1

        super(Template3, self).save(*args, **kwargs)
