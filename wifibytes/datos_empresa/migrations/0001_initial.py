# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosEmpresa',
            fields=[
                ('datos_empresa_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=300, null=True, verbose_name=b'Nombre Empresa', blank=True)),
                ('cifnif', models.CharField(max_length=20, null=True, verbose_name=b'CIF/NIF', blank=True)),
                ('logo', models.FileField(upload_to=b'media', null=True, verbose_name=b'Logo Url', blank=True)),
                ('icon_logo', models.FileField(upload_to=b'media', null=True, verbose_name=b'Icono Logo Url', blank=True)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('created_at', models.IntegerField(default=0, editable=False)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Datos Empresa',
                'verbose_name_plural': 'Datos Empresa',
            },
        ),
    ]
