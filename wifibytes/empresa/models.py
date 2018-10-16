# encoding:utf-8
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Empresa(models.Model):
    direccion = models.CharField(
        verbose_name=("Dirección"), max_length=100, blank=False)
    id = models.IntegerField(primary_key=True, editable=False)
    codpago = models.CharField(verbose_name=("Codigo Pago"), max_length=10)
    codejercicio = models.CharField(
        verbose_name=("Codigo Ejercicio"), max_length=4)
    web = models.CharField(verbose_name=("Web"), max_length=100)
    rmercantil = models.CharField(
        verbose_name=("Registro Mercantil"), max_length=100)
    fax = models.CharField(verbose_name=("Fax"), max_length=20)
    codpais = models.CharField(verbose_name=("Codigo Pais"), max_length=20)
    lopd = HTMLField()
    email = models.CharField(verbose_name=("Email"), max_length=100)
    codalmacen = models.CharField(
        verbose_name=("Codigo Almacen"), max_length=4)
    cifnif = models.CharField(
        verbose_name=("CIFNIF"), max_length=20, blank=False)
    recequivalencia = models.BooleanField(
        verbose_name=("REC Equivalencia"), default=None)
    logo = HTMLField()
    contintegrada = models.BooleanField(default=None)
    provincia = models.CharField(verbose_name=("Provincia"), max_length=100)
    administrador = models.CharField(
        verbose_name=("Administración"), max_length=100, blank=False)
    nombre = models.CharField(
        verbose_name=("Nombre"), max_length=100, blank=False)
    telefono = models.CharField(verbose_name=("Telefono"), max_length=20)
    codedi = models.CharField(
        verbose_name=("Codido de Dirección"), max_length=17)
    codserie = models.CharField(verbose_name=("Codigo Serie"), max_length=2)
    apartado = models.CharField(verbose_name=("Apartado"), max_length=10)
    codpostal = models.CharField(verbose_name=("Codigo Postal"), max_length=10)
    idprovincia = models.IntegerField(verbose_name=("Id Provincia"),)
    ciudad = models.CharField(verbose_name=("Ciudad"), max_length=100)
    coddivisa = models.CharField(verbose_name=("Codigo divisa"), max_length=3)
    stockpedidos = models.BooleanField(
        verbose_name=("Stock pedidos"), default=None)
    codcuentarem = models.CharField(
        verbose_name=("Codigo cuenta rem"), max_length=6)

    def __unicode__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        if not self.id:
            no = Empresa.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1

        super(Empresa, self).save(*args, **kwargs)
