# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template1',
            name='articulo',
            field=models.ForeignKey(related_name='template1_articulo', to='catalogo.Articulo'),
        ),
    ]
