# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('direccion', models.CharField(max_length=100, verbose_name=b'Direcci\xc3\xb3n')),
                ('id', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('codpago', models.CharField(max_length=10, verbose_name=b'Codigo Pago')),
                ('codejercicio', models.CharField(max_length=4, verbose_name=b'Codigo Ejercicio')),
                ('web', models.CharField(max_length=100, verbose_name=b'Web')),
                ('rmercantil', models.CharField(max_length=100, verbose_name=b'Registro Mercantil')),
                ('fax', models.CharField(max_length=20, verbose_name=b'Fax')),
                ('codpais', models.CharField(max_length=20, verbose_name=b'Codigo Pais')),
                ('lopd', tinymce.models.HTMLField()),
                ('email', models.CharField(max_length=100, verbose_name=b'Email')),
                ('codalmacen', models.CharField(max_length=4, verbose_name=b'Codigo Almacen')),
                ('cifnif', models.CharField(max_length=20, verbose_name=b'CIFNIF')),
                ('recequivalencia', models.BooleanField(default=None, verbose_name=b'REC Equivalencia')),
                ('logo', tinymce.models.HTMLField()),
                ('contintegrada', models.BooleanField(default=None)),
                ('provincia', models.CharField(max_length=100, verbose_name=b'Provincia')),
                ('administrador', models.CharField(max_length=100, verbose_name=b'Administraci\xc3\xb3n')),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('telefono', models.CharField(max_length=20, verbose_name=b'Telefono')),
                ('codedi', models.CharField(max_length=17, verbose_name=b'Codido de Direcci\xc3\xb3n')),
                ('codserie', models.CharField(max_length=2, verbose_name=b'Codigo Serie')),
                ('apartado', models.CharField(max_length=10, verbose_name=b'Apartado')),
                ('codpostal', models.CharField(max_length=10, verbose_name=b'Codigo Postal')),
                ('idprovincia', models.IntegerField(verbose_name=b'Id Provincia')),
                ('ciudad', models.CharField(max_length=100, verbose_name=b'Ciudad')),
                ('coddivisa', models.CharField(max_length=3, verbose_name=b'Codigo divisa')),
                ('stockpedidos', models.BooleanField(default=None, verbose_name=b'Stock pedidos')),
                ('codcuentarem', models.CharField(max_length=6, verbose_name=b'Codigo cuenta rem')),
            ],
        ),
    ]
