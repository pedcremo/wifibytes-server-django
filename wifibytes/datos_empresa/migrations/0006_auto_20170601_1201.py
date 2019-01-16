# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0005_auto_20170601_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosempresa',
            name='address',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Direccion', blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='city',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Ciudad', blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='country',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Pais', blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='datos_empresa_default',
            field=models.BooleanField(default=False, verbose_name=b'Empresa por Defecto'),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='location',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Localizacion', blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Telefono', blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='province',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Provincia', blank=True),
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='zipcode',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Cod.Postal', blank=True),
        ),
    ]
