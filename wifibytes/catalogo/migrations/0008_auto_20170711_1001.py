# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_auto_20170711_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template1',
            name='caja_1_texto',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template1',
            name='caja_2_texto',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template1',
            name='caja_3_texto',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
    ]
