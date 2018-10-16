# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilsclients',
            name='buzon_voz_procesing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mobilsclients',
            name='roaming_procesing',
            field=models.BooleanField(default=False),
        ),
    ]
