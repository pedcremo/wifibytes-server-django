# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0011_auto_20170601_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosempresa',
            name='location',
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='location_lat',
            field=models.DecimalField(null=True, verbose_name=b'Latitud', max_digits=10, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='location_long',
            field=models.DecimalField(null=True, verbose_name=b'Longitud', max_digits=10, decimal_places=10, blank=True),
        ),
    ]
