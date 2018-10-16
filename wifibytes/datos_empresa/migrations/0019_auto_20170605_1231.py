# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0018_auto_20170605_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosempresa',
            name='icon_logo',
            field=models.FileField(upload_to=b'icon_logo', null=True, verbose_name=b'Icono Logo Url', blank=True),
        ),
        migrations.AlterField(
            model_name='datosempresa',
            name='logo',
            field=models.FileField(upload_to=b'logo', null=True, verbose_name=b'Logo Url', blank=True),
        ),
    ]
