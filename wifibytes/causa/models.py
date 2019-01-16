# encoding:utf-8


from django.db import models
from django.core.files import File
from django.core.validators import MaxValueValidator, MinValueValidator
from tinymce.models import HTMLField
import uuid
import hashlib, base64
from PIL import Image as Img
from PIL import ImageOps
import io

# Create your models here.
class Causa(models.Model):

    validoxaltrebit = ((0, 'False'), (1, 'True'),)
    visible = ((0, 'False'), (1, 'True'),)

    codcausa = models.IntegerField(verbose_name=("Codigo causa"), primary_key=True, editable=False)
    nombre = models.CharField(verbose_name=("Nombre"), max_length=100, blank=False)
    descripcion = HTMLField()
    thumbnail_url = models.FileField(verbose_name=("Thumbnail Url"), upload_to='media', null=True, blank=True)
    fechainicio = models.DateField(verbose_name=("Fecha de Inicio"), null=True, blank=True)
    visible = models.IntegerField(choices=visible, verbose_name=("visible"), null=True, blank=True)
    recaudacion = models.FloatField(verbose_name=("Recaudación"), default=0, blank=True)
    activo = models.BooleanField(verbose_name=("Causa Actual"), null=False, default=0,blank=False)
    valido_altrebit = models.BooleanField(verbose_name=("Causa Actual"), null=False,blank=False, default=0)

    def __unicode__(self):
        return str(self.codcausa)

    def save(self, *args, **kwargs):

        if not self.codcausa:
            no = Causa.objects.count()

            if no == 0:
                self.codcausa = 1
            else:
                self.codcausa = self.__class__.objects.all().order_by("-codcausa")[0].codcausa + 1

            try:
                # Image Variables
                imagename = str(uuid.uuid1().hex) + '.PNG'
                print('triying image')
                image = Img.open(io.StringIO(self.thumbnail_url.read()))
                width, height = image.size
                new_width = 750
                new_height = height * new_width / width
                temp_img = image.resize((new_width, new_height), Img.LANCZOS)
                print(temp_img.size)
                output = io.StringIO()
                temp_img.save(output, format='PNG', optimize=True)
                output.seek(0)
                new_img = File(output, imagename)
                self.thumbnail_url = new_img

            except Exception:
                print('ERROR: Error on team image')

        else:
            orig = Causa.objects.get(pk=self.pk)
            if orig.thumbnail_url != self.thumbnail_url:
                try:
                    # Image Variables
                    imagename = str(uuid.uuid1().hex) + '.PNG'
                    print('triying image')
                    image = Img.open(io.StringIO(self.thumbnail_url.read()))
                    width, height = image.size
                    new_width = 750
                    new_height = height * new_width / width
                    temp_img = image.resize((new_width, new_height), Img.LANCZOS)
                    print(temp_img.size)
                    output = io.StringIO()
                    temp_img.save(output, format='PNG', optimize=True)
                    output.seek(0)
                    new_img = File(output, imagename)
                    self.thumbnail_url = new_img

                except Exception:
                    print('ERROR: Error on team image')

        super(Causa, self).save(*args, **kwargs)
