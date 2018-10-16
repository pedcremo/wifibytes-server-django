# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('internationalization', '0001_initial'),
        ('datos_empresa', '0020_auto_20170607_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextoContrato',
            fields=[
                ('texto_contrato_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('key', models.CharField(max_length=200, null=True, blank=True)),
                ('content', tinymce.models.HTMLField(null=True, blank=True)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('idioma', models.ForeignKey(to='internationalization.Idioma', null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Texto Contrato',
                'verbose_name_plural': 'Texto Contratos',
            },
        ),
        migrations.CreateModel(
            name='TextosContrato',
            fields=[
                ('textos_contrato_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('textos_contrato_default', models.BooleanField(default=False, verbose_name=b'Textos Contrato por Defecto')),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('created_at', models.IntegerField(default=0, editable=False)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Textos Contrato',
                'verbose_name_plural': 'Textos Contratos',
            },
        ),
        migrations.AddField(
            model_name='textocontrato',
            name='textos_contrato_fk',
            field=models.ForeignKey(related_name='textos_contrato_fk', verbose_name=b'Textos Contrato', to='datos_empresa.TextosContrato'),
        ),
        migrations.AlterUniqueTogether(
            name='textocontrato',
            unique_together=set([('textos_contrato_fk', 'key', 'idioma')]),
        ),
    ]
