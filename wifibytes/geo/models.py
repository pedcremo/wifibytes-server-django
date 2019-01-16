# encoding:utf-8
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Pais(models.Model):
    codpais = models.CharField(max_length=20, primary_key=True, null=False,
                               blank=False)
    codiso = models.CharField(max_length=2, null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Paises'

    def __unicode__(self):
        return str(self.nombre)


class Comunidad(models.Model):
    codcomunidad = models.IntegerField(primary_key=True,
                                       null=False, editable=False)
    codpais = models.ForeignKey(Pais, null=False, blank=False,on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Comunidades'

    def __unicode__(self):
        return str(self.nombre)

    def save(self, *args, **kwargs):

        if not self.codcomunidad:
            no = Comunidad.objects.count()
            if no == 0:
                self.codcomunidad = 1
            else:
                self.codcomunidad = self.__class__.objects.all().order_by(
                    "-codcomunidad")[0].codcomunidad + 1

        super(Comunidad, self).save(*args, **kwargs)


class Provincia(models.Model):
    idprovincia = models.IntegerField(
        primary_key=True, null=False, editable=False)
    provincia = models.CharField(max_length=50, null=False, blank=False)
    codpais = models.ForeignKey(Pais, null=False, blank=False,on_delete=models.PROTECT)
    codcomunidad = models.ForeignKey(Comunidad, null=True, blank=True,on_delete=models.SET_NULL)
    codigo = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Provincias'

    def __unicode__(self):
        return str(self.provincia)

    def save(self, *args, **kwargs):

        if not self.idprovincia:
            no = self.__class__.objects.all().order_by(
                    "-idprovincia")
            if no.count() == 0:
                self.idprovincia = 900000
            else:
                actual = no[0].idprovincia
                self.idprovincia = 900000 if actual < 900000 else (actual + 1)

        super(Provincia, self).save(*args, **kwargs)
