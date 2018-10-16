# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0014_auto_20170602_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosempresa',
            name='location_lat',
            field=models.DecimalField(null=True, verbose_name=b'Latitud', max_digits=9, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='datosempresa',
            name='location_long',
            field=models.DecimalField(null=True, verbose_name=b'Longitud', max_digits=9, decimal_places=6, blank=True),
        ),
    ]
