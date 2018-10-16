# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('icc', '0002_auto_20170711_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangoicc',
            name='rango_icc_end',
            field=models.BigIntegerField(default=0, verbose_name=b'Rango Final', validators=[django.core.validators.MaxValueValidator(999999999999999999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='rangoicc',
            name='rango_icc_init',
            field=models.BigIntegerField(default=0, verbose_name=b'Rango Inicial', validators=[django.core.validators.MaxValueValidator(999999999999999999), django.core.validators.MinValueValidator(0)]),
        ),
    ]
