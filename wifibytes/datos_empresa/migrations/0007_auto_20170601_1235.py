# -*- coding: utf-8 -*-


from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0006_auto_20170601_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosempresa',
            name='aviso_legal_en',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Aviso Legal [EN]', blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='aviso_legal_es',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Aviso Legal [ES]', blank=True),
        ),
    ]
