# -*- coding: utf-8 -*-


from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0007_auto_20170601_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosempresa',
            name='aviso_cookies_en',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Aviso Cookies [EN]', blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='aviso_cookies_es',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Aviso Cookies [ES]', blank=True),
        ),
    ]
