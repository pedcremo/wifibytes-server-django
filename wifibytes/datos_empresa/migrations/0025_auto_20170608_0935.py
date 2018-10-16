# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0024_auto_20170608_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texto',
            name='content',
            field=models.TextField(max_length=10000, null=True, blank=True),
        ),
    ]
