# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_auto_20170711_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template1',
            name='imagen1',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen1', blank=True),
        ),
        migrations.AlterField(
            model_name='template1',
            name='imagen2',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen2', blank=True),
        ),
        migrations.AlterField(
            model_name='template1',
            name='imagen3',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen3', blank=True),
        ),
        migrations.AlterField(
            model_name='template1',
            name='imagen_fondo_cabecera',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'imagen_fondo_cabecera', blank=True),
        ),
        migrations.AlterField(
            model_name='template1',
            name='imagen_fondo_cuerpo',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'imagen_fondo_cuerpo', blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='imagen1',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen1', blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='imagen2',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen2', blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='imagen3',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen3', blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='imagen4',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen4', blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='imagen_fondo_cabecera',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'imagen_fondo_cabecera', blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='imagen_fondo_cuerpo',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'imagen_fondo_cuerpo', blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='franja_1_fondo',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'imagen_fondo_cabecera', blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='franja_2_fondo',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'imagen_fondo_cabecera', blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='imagen1',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen1', blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='imagen2',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen2', blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='imagen3',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen3', blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='imagen4',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen4', blank=True),
        ),
    ]
