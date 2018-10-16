# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0010_auto_20170601_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosempresa',
            name='aviso_cookies_en',
            field=models.TextField(null=True, verbose_name=b'Aviso Cookies [EN]', blank=True),
        ),
        migrations.AlterField(
            model_name='datosempresa',
            name='aviso_cookies_es',
            field=models.TextField(null=True, verbose_name=b'Aviso Cookies [ES]', blank=True),
        ),
        migrations.AlterField(
            model_name='datosempresa',
            name='aviso_legal_en',
            field=models.TextField(null=True, verbose_name=b'Aviso Legal [EN]', blank=True),
        ),
    ]
