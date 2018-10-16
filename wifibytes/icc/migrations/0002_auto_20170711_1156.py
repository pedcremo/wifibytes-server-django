# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('icc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangoicc',
            name='rango_icc_end',
            field=models.IntegerField(default=0, verbose_name=b'Rango Final', validators=[django.core.validators.MaxValueValidator(1000000000000000000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='rangoicc',
            name='rango_icc_init',
            field=models.IntegerField(default=0, verbose_name=b'Rango Inicial', validators=[django.core.validators.MaxValueValidator(1000000000000000000), django.core.validators.MinValueValidator(0)]),
        ),
    ]
