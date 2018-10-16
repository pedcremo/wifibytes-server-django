# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('internationalization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name=b'titulo')),
                ('subtitulo', models.CharField(max_length=100, verbose_name=b'subtitulo')),
                ('caja_izquierda_titulo', models.CharField(max_length=100, verbose_name=b'caja_izquierda_titulo')),
                ('caja_izquierda_texto', tinymce.models.HTMLField()),
                ('caja_derecha_titulo', models.CharField(max_length=100, verbose_name=b'caja_derecha_titulo')),
                ('caja_derecha_texto', tinymce.models.HTMLField()),
                ('activo', models.BooleanField(default=False)),
                ('idioma', models.ForeignKey(to='internationalization.Idioma', null=True)),
            ],
            options={
                'verbose_name': 'Textos Inicio',
            },
        ),
        migrations.CreateModel(
            name='PaletaColores',
            fields=[
                ('id', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name=b'titulo')),
                ('hexadecimal', models.CharField(max_length=100, verbose_name=b'hexadecimal')),
            ],
        ),
        migrations.CreateModel(
            name='TarifaDescriptorGenerico',
            fields=[
                ('id', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('pretitulo', models.CharField(max_length=100, verbose_name=b'pretitulo')),
                ('titulo', models.CharField(max_length=100, verbose_name=b'titulo')),
                ('caja_1_titulo', models.CharField(max_length=100, verbose_name=b'caja_1_titulo')),
                ('caja_1_texto', tinymce.models.HTMLField()),
                ('caja_1_icono', models.FileField(upload_to=b'pagina_tarifas')),
                ('caja_2_titulo', models.CharField(max_length=100, verbose_name=b'caja_2_titulo')),
                ('caja_2_texto', tinymce.models.HTMLField()),
                ('caja_2_icono', models.FileField(upload_to=b'pagina_tarifas')),
                ('caja_3_titulo', models.CharField(max_length=100, verbose_name=b'caja_3_titulo')),
                ('caja_3_texto', tinymce.models.HTMLField()),
                ('caja_3_icono', models.FileField(upload_to=b'pagina_tarifas')),
                ('caja_4_titulo', models.CharField(max_length=100, verbose_name=b'caja_4_titulo')),
                ('caja_4_texto', tinymce.models.HTMLField()),
                ('caja_4_icono', models.FileField(upload_to=b'pagina_tarifas')),
                ('activo', models.BooleanField(default=False)),
                ('idioma', models.ForeignKey(to='internationalization.Idioma', null=True)),
            ],
            options={
                'verbose_name': 'Textos cajitas tarifa',
            },
        ),
        migrations.CreateModel(
            name='TxtContacto',
            fields=[
                ('id', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('email', models.CharField(max_length=100, verbose_name=b'email')),
                ('telefono', models.CharField(max_length=100, verbose_name=b'telefono')),
                ('provincia', models.CharField(max_length=100, verbose_name=b'provincia')),
                ('codigo_postal', models.CharField(max_length=100, verbose_name=b'codigo_postal')),
                ('calle', models.CharField(max_length=100, verbose_name=b'calle')),
                ('activo', models.BooleanField(default=False)),
                ('idioma', models.ForeignKey(to='internationalization.Idioma', null=True)),
            ],
        ),
    ]
