# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0017_auto_20170602_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosempresa',
            name='aviso_cookies_en',
        ),
        migrations.RemoveField(
            model_name='datosempresa',
            name='aviso_cookies_es',
        ),
        migrations.RemoveField(
            model_name='datosempresa',
            name='aviso_legal_en',
        ),
        migrations.RemoveField(
            model_name='datosempresa',
            name='aviso_legal_es',
        ),
        migrations.AlterField(
            model_name='datosempresa',
            name='logo',
            field=models.FileField(upload_to=b'', null=True, verbose_name=b'Logo Url', blank=True),
        ),
    ]
