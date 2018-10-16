# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0026_infoempresa_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosEmail',
            fields=[
                ('datos_email_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('email_receiver', models.CharField(max_length=50, null=True, verbose_name=b'Email Receptor', blank=True)),
                ('email_sender', models.CharField(max_length=50, null=True, verbose_name=b'Email Envio', blank=True)),
                ('email_sender_password', models.CharField(max_length=50, null=True, verbose_name=b'Password Email Envio', blank=True)),
                ('server', models.CharField(max_length=50, null=True, verbose_name=b'Servidor', blank=True)),
                ('port', models.IntegerField(default=25, null=True, verbose_name=b'Puerto Servidor', blank=True)),
                ('datos_email_default', models.BooleanField(default=False, verbose_name=b'Datos Email por Defecto')),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('datos_empresa_fk', models.ForeignKey(verbose_name=b'Datos Empresa', to='datos_empresa.DatosEmpresa')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Datos Email',
                'verbose_name_plural': 'Datos Email',
            },
        ),
    ]
