# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internationalization', '0001_initial'),
        ('datos_empresa', '0016_auto_20170602_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoempresa',
            name='idioma',
            field=models.ForeignKey(to='internationalization.Idioma', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='infoempresa',
            unique_together=set([('datos_empresa_fk', 'key', 'idioma')]),
        ),
    ]
