# encoding:utf-8
from django.db import models
from tinymce.models import HTMLField

class Home(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    titulo = models.CharField(verbose_name=("titulo"), max_length=100, blank=False)
    subtitulo = models.CharField(verbose_name=("subtitulo"), max_length=100, blank=False)
    caja_izquierda_titulo = models.CharField(verbose_name=("caja_izquierda_titulo"), max_length=100, blank=False)
    caja_izquierda_texto = HTMLField()
    caja_derecha_titulo = models.CharField(verbose_name=("caja_derecha_titulo"), max_length=100, blank=False)
    caja_derecha_texto = HTMLField()
    activo = models.BooleanField(default=False,  editable=True, null=False)
    idioma = models.ForeignKey('internationalization.Idioma', null=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name="Textos Inicio"

    def save(self, *args, **kwargs):

        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1

        super(Home, self).save(*args, **kwargs)



class TarifaDescriptorGenerico(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)

    pretitulo = models.CharField(verbose_name=("pretitulo"), max_length=100, blank=False)
    titulo = models.CharField(verbose_name=("titulo"), max_length=100, blank=False)

    caja_1_titulo = models.CharField(verbose_name=("caja_1_titulo"), max_length=100, blank=False)
    caja_1_texto = HTMLField()
    caja_1_icono = models.FileField(upload_to="pagina_tarifas")

    caja_2_titulo = models.CharField(verbose_name=("caja_2_titulo"), max_length=100, blank=False)
    caja_2_texto = HTMLField()
    caja_2_icono = models.FileField(upload_to="pagina_tarifas")

    caja_3_titulo = models.CharField(verbose_name=("caja_3_titulo"), max_length=100, blank=False)
    caja_3_texto = HTMLField()
    caja_3_icono = models.FileField(upload_to="pagina_tarifas")

    caja_4_titulo = models.CharField(verbose_name=("caja_4_titulo"), max_length=100, blank=False)
    caja_4_texto = HTMLField()
    caja_4_icono = models.FileField(upload_to="pagina_tarifas")
    activo = models.BooleanField(default=False,  editable=True, null=False)
    idioma = models.ForeignKey('internationalization.Idioma', null=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Textos cajitas tarifa"

    def save(self, *args, **kwargs):

        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1

        super(TarifaDescriptorGenerico, self).save(*args, **kwargs)


class PaletaColores(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    titulo = models.CharField(verbose_name=("titulo"), max_length=100, blank=False)
    hexadecimal = models.CharField(verbose_name=("hexadecimal"), max_length=100, blank=False)

    def __str__(self):
        return str(self.titulo)

    def save(self, *args, **kwargs):

        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by("-id")[0].id + 1

        super(PaletaColores, self).save(*args, **kwargs)


class TxtContacto(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    email = models.CharField(verbose_name=("email"), max_length=100, blank=False)
    telefono = models.CharField(verbose_name=("telefono"), max_length=100, blank=False)
    provincia = models.CharField(verbose_name=("provincia"), max_length=100, blank=False)
    codigo_postal = models.CharField(verbose_name=("codigo_postal"), max_length=100, blank=False)
    calle = models.CharField(verbose_name=("calle"), max_length=100, blank=False)
    activo = models.BooleanField(default=False,  editable=True, null=False)
    idioma = models.ForeignKey('internationalization.Idioma', null=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1

        super(TxtContacto, self).save(*args, **kwargs)
