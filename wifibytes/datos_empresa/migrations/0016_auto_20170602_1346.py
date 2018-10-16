# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0015_auto_20170602_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoEmpresa',
            fields=[
                ('info_empresa_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('key', models.CharField(max_length=200, null=True, blank=True)),
                ('content', models.TextField(max_length=30800, null=True, blank=True)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('datos_empresa_fk', models.ForeignKey(related_name='datos_empresa_fk', verbose_name=b'Datos Empresa', to='datos_empresa.DatosEmpresa')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Info Empresa',
                'verbose_name_plural': 'Info Empresas',
            },
        ),
        migrations.AlterUniqueTogether(
            name='infoempresa',
            unique_together=set([('datos_empresa_fk', 'key')]),
        ),
    ]
