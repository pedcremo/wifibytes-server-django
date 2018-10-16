# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallApi',
            fields=[
                ('call_id', models.IntegerField(verbose_name=b'ID', serialize=False, editable=False, primary_key=True)),
                ('url', models.CharField(max_length=120, verbose_name=b'url')),
                ('authfield', models.CharField(max_length=120, verbose_name=b'authfield info')),
                ('trans_call', models.IntegerField(blank=True, null=True, verbose_name=b'Tipo de Transacci\xc3\xb3n', choices=[(0, b'GET'), (1, b'POST'), (2, b'PUT')])),
            ],
        ),
        migrations.CreateModel(
            name='Omv',
            fields=[
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('descripcion', models.CharField(max_length=500, verbose_name=b'Descripci\xc3\xb3n')),
                ('codigo', models.IntegerField(verbose_name=b'Codigo', serialize=False, editable=False, primary_key=True)),
                ('activo', models.BooleanField(default=0, verbose_name=b'Activo')),
            ],
        ),
        migrations.CreateModel(
            name='ParamCallApi',
            fields=[
                ('id', models.IntegerField(verbose_name=b'ID', serialize=False, editable=False, primary_key=True)),
                ('param_name', models.CharField(max_length=120, verbose_name=b'param nombre')),
                ('requerido', models.BooleanField(default=None, verbose_name=b'Requerido')),
                ('call_id', models.ForeignKey(related_name='CallApi_ParamCallApi', verbose_name=b'Call OMV', to='omv.CallApi')),
            ],
        ),
        migrations.CreateModel(
            name='ParamCallBackApi',
            fields=[
                ('id', models.IntegerField(verbose_name=b'ID', serialize=False, editable=False, primary_key=True)),
                ('param_name', models.CharField(max_length=120, verbose_name=b'param nombre')),
                ('call_id', models.ForeignKey(related_name='CallApi_ParamCallBackApi', verbose_name=b'Call OMV', to='omv.CallApi')),
            ],
        ),
        migrations.CreateModel(
            name='TypeCallApi',
            fields=[
                ('tid', models.IntegerField(verbose_name=b'ID', serialize=False, editable=False, primary_key=True)),
                ('nombre', models.CharField(max_length=120, verbose_name=b'nombre')),
            ],
        ),
        migrations.CreateModel(
            name='UserApiOmv',
            fields=[
                ('uid', models.IntegerField(verbose_name=b'UID', serialize=False, editable=False, primary_key=True)),
                ('user_login', models.CharField(max_length=30, verbose_name=b'User Login')),
                ('user_password', models.CharField(max_length=30, verbose_name=b'User Password')),
                ('codigo_omv', models.ForeignKey(related_name='UserOmv_Omv', verbose_name=b'Codigo OMV', to='omv.Omv')),
            ],
        ),
        migrations.AddField(
            model_name='callapi',
            name='codigo_omv',
            field=models.ForeignKey(related_name='UserOmv_CallApi', verbose_name=b'Codigo OMV', to='omv.Omv'),
        ),
        migrations.AddField(
            model_name='callapi',
            name='typecall',
            field=models.ForeignKey(related_name='TypeCallApi_CallApi', verbose_name=b'Tipo de Call', to='omv.TypeCallApi'),
        ),
    ]
