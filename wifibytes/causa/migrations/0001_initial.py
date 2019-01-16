# -*- coding: utf-8 -*-


from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Causa',
            fields=[
                ('codcausa', models.IntegerField(verbose_name=b'Codigo causa', serialize=False, editable=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('descripcion', tinymce.models.HTMLField()),
                ('thumbnail_url', models.FileField(upload_to=b'media', null=True, verbose_name=b'Thumbnail Url', blank=True)),
                ('fechainicio', models.DateField(null=True, verbose_name=b'Fecha de Inicio', blank=True)),
                ('visible', models.IntegerField(blank=True, null=True, verbose_name=b'visible', choices=[(0, b'False'), (1, b'True')])),
                ('recaudacion', models.FloatField(default=0, verbose_name=b'Recaudaci\xc3\xb3n', blank=True)),
                ('activo', models.BooleanField(default=0, verbose_name=b'Causa Actual')),
                ('valido_altrebit', models.BooleanField(default=0, verbose_name=b'Causa Actual')),
            ],
        ),
    ]
