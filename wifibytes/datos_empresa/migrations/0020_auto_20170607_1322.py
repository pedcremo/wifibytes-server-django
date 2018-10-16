# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0019_auto_20170605_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoempresa',
            name='content',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
    ]
