# encoding:utf-8
from django.db import models


class Idioma(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.codigo

    def __str__(self):
        return self.codigo