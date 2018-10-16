# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_auto_20170719_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilsclients',
            name='dc_icc_anterior',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mobilsclients',
            name='icc_anterior',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
