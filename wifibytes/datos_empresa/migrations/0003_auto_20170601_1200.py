# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0002_auto_20170601_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosempresa',
            name='cifnif',
            field=models.CharField(max_length=20, null=True, verbose_name=b'CIF/NIF', blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='icon_logo',
            field=models.FileField(upload_to=b'media', null=True, verbose_name=b'Icono Logo Url', blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='logo',
            field=models.FileField(upload_to=b'media', null=True, verbose_name=b'Logo Url', blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='name',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Nombre Empresa', blank=True),
        ),
    ]
