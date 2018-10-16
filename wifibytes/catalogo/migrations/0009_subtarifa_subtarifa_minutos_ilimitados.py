# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0008_auto_20170711_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtarifa',
            name='subtarifa_minutos_ilimitados',
            field=models.BooleanField(default=False),
        ),
    ]
