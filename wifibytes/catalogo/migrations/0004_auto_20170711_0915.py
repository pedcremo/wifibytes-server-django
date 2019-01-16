# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20170711_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template1',
            name='caja_1_titulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'caja_1_titulo', blank=True),
        ),
        migrations.AlterField(
            model_name='template1',
            name='caja_2_titulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'caja_2_titulo', blank=True),
        ),
        migrations.AlterField(
            model_name='template1',
            name='caja_3_titulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'caja_3_titulo', blank=True),
        ),
        migrations.AlterField(
            model_name='template1',
            name='caja_4_titulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'caja_4_titulo', blank=True),
        ),
        migrations.AlterField(
            model_name='template1',
            name='imagen1',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen1'),
        ),
        migrations.AlterField(
            model_name='template1',
            name='imagen2',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen2'),
        ),
        migrations.AlterField(
            model_name='template1',
            name='imagen3',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'Imagen3'),
        ),
        migrations.AlterField(
            model_name='template1',
            name='imagen_fondo_cabecera',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'imagen_fondo_cabecera'),
        ),
        migrations.AlterField(
            model_name='template1',
            name='imagen_fondo_cuerpo',
            field=models.FileField(upload_to=b'Templates', null=True, verbose_name=b'imagen_fondo_cuerpo'),
        ),
        migrations.AlterField(
            model_name='template1',
            name='pretitulo',
            field=models.CharField(max_length=100, null=True, verbose_name=b'pretitulo', blank=True),
        ),
    ]
