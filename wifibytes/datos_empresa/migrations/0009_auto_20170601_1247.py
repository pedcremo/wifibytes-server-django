# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0008_auto_20170601_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosempresa',
            name='social_facebook',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Facebook', blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='social_twitter',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Twitter', blank=True),
        ),
    ]
