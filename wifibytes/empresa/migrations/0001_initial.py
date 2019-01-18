# Generated by Django 2.1.5 on 2019-01-18 10:45

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('codpago', models.CharField(max_length=10, verbose_name='Codigo Pago')),
                ('codejercicio', models.CharField(max_length=4, verbose_name='Codigo Ejercicio')),
                ('web', models.CharField(max_length=100, verbose_name='Web')),
                ('rmercantil', models.CharField(max_length=100, verbose_name='Registro Mercantil')),
                ('fax', models.CharField(max_length=20, verbose_name='Fax')),
                ('codpais', models.CharField(max_length=20, verbose_name='Codigo Pais')),
                ('lopd', tinymce.models.HTMLField()),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('codalmacen', models.CharField(max_length=4, verbose_name='Codigo Almacen')),
                ('cifnif', models.CharField(max_length=20, verbose_name='CIFNIF')),
                ('recequivalencia', models.BooleanField(default=None, verbose_name='REC Equivalencia')),
                ('logo', tinymce.models.HTMLField()),
                ('contintegrada', models.BooleanField(default=None)),
                ('provincia', models.CharField(max_length=100, verbose_name='Provincia')),
                ('administrador', models.CharField(max_length=100, verbose_name='Administración')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('telefono', models.CharField(max_length=20, verbose_name='Telefono')),
                ('codedi', models.CharField(max_length=17, verbose_name='Codido de Dirección')),
                ('codserie', models.CharField(max_length=2, verbose_name='Codigo Serie')),
                ('apartado', models.CharField(max_length=10, verbose_name='Apartado')),
                ('codpostal', models.CharField(max_length=10, verbose_name='Codigo Postal')),
                ('idprovincia', models.IntegerField(verbose_name='Id Provincia')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('coddivisa', models.CharField(max_length=3, verbose_name='Codigo divisa')),
                ('stockpedidos', models.BooleanField(default=None, verbose_name='Stock pedidos')),
                ('codcuentarem', models.CharField(max_length=6, verbose_name='Codigo cuenta rem')),
            ],
        ),
    ]
