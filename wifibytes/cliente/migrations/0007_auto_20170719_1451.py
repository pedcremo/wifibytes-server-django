# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_auto_20170719_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentasbcocli',
            name='ctaagencia',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cuentasbcocli',
            name='ctaentidad',
            field=models.CharField(max_length=4, null=True, verbose_name=b'Cuenta Entidad', blank=True),
        ),
        migrations.AlterField(
            model_name='cuentasbcocli',
            name='direntidad',
            field=models.CharField(max_length=150, null=True, verbose_name=b'Entidad', blank=True),
        ),
        migrations.AlterField(
            model_name='cuentasbcocli',
            name='iban',
            field=models.CharField(max_length=34, null=True, verbose_name=b'IBAN', blank=True),
        ),
    ]
