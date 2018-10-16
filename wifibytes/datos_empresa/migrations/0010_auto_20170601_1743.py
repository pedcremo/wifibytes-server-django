# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0009_auto_20170601_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosempresa',
            name='aviso_legal_es',
            field=models.TextField(null=True, verbose_name=b'Aviso Legal [ES]', blank=True),
        ),
    ]
