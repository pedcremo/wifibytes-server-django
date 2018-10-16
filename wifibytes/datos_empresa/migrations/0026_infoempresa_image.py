# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0025_auto_20170608_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoempresa',
            name='image',
            field=models.FileField(upload_to=b'info_empresa_image', null=True, verbose_name=b'Info Empresa Imagen', blank=True),
        ),
    ]
