# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0027_datosemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosempresa',
            name='mapa_cobertura',
            field=models.FileField(upload_to=b'mapa_cobertura', null=True, verbose_name=b'Mapa Cobertura Url', blank=True),
        ),
    ]
