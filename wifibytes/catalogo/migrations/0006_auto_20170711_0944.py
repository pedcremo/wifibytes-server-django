# -*- coding: utf-8 -*-


from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_auto_20170711_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template1',
            name='caja_4_texto',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='caja_1_texto',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='caja_1_titulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'caja_1_titulo', blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='caja_2_texto',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='caja_2_titulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'caja_2_titulo', blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='caja_3_texto',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='caja_3_titulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'caja_3_titulo', blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='caja_4_texto',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='caja_4_titulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'caja_4_titulo', blank=True),
        ),
        migrations.AlterField(
            model_name='template2',
            name='imagen1',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen1'),
        ),
        migrations.AlterField(
            model_name='template2',
            name='imagen2',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen2'),
        ),
        migrations.AlterField(
            model_name='template2',
            name='imagen3',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen3'),
        ),
        migrations.AlterField(
            model_name='template2',
            name='imagen4',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen4'),
        ),
        migrations.AlterField(
            model_name='template2',
            name='imagen_fondo_cabecera',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'imagen_fondo_cabecera'),
        ),
        migrations.AlterField(
            model_name='template2',
            name='imagen_fondo_cuerpo',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'imagen_fondo_cuerpo'),
        ),
        migrations.AlterField(
            model_name='template2',
            name='pretitulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'pretitulo', blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='caja_1_texto',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='caja_1_titulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'caja_1_titulo', blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='caja_2_texto',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='caja_2_titulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'caja_2_titulo', blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='franja_1_fondo',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'imagen_fondo_cabecera'),
        ),
        migrations.AlterField(
            model_name='template3',
            name='franja_1_texto',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='franja_2_fondo',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'imagen_fondo_cabecera'),
        ),
        migrations.AlterField(
            model_name='template3',
            name='franja_2_texto',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template3',
            name='imagen1',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen1'),
        ),
        migrations.AlterField(
            model_name='template3',
            name='imagen2',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen2'),
        ),
        migrations.AlterField(
            model_name='template3',
            name='imagen3',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen3'),
        ),
        migrations.AlterField(
            model_name='template3',
            name='imagen4',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen4'),
        ),
        migrations.AlterField(
            model_name='template3',
            name='pretitulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'pretitulo', blank=True),
        ),
    ]
