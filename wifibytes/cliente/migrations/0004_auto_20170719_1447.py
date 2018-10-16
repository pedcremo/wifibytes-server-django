# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20170719_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentasbcocli',
            name='entidad',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Entidad'),
        ),
    ]
