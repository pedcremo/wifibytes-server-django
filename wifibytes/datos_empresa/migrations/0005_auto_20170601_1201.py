# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0004_auto_20170601_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosempresa',
            name='test',
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='name',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Nombre Empresa', blank=True),
        ),
    ]
