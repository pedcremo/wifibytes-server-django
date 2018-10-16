# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('codcomunidad', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Comunidades',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('codpais', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('codiso', models.CharField(max_length=2, null=True, blank=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('idprovincia', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('provincia', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=2, null=True, blank=True)),
                ('codcomunidad', models.ForeignKey(blank=True, to='geo.Comunidad', null=True)),
                ('codpais', models.ForeignKey(to='geo.Pais')),
            ],
            options={
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.AddField(
            model_name='comunidad',
            name='codpais',
            field=models.ForeignKey(to='geo.Pais'),
        ),
    ]
