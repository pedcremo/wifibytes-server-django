# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SermepaIdTPV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idtpv', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='SermepaResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('Ds_Date', models.DateField()),
                ('Ds_Hour', models.TimeField()),
                ('Ds_SecurePayment', models.IntegerField()),
                ('Ds_MerchantData', models.CharField(max_length=1024)),
                ('Ds_Card_Country', models.IntegerField(null=True, blank=True)),
                ('Ds_Card_Type', models.CharField(max_length=1, null=True, blank=True)),
                ('Ds_Terminal', models.IntegerField()),
                ('Ds_MerchantCode', models.CharField(max_length=9)),
                ('Ds_ConsumerLanguage', models.IntegerField()),
                ('Ds_Response', models.CharField(max_length=4)),
                ('Ds_Order', models.CharField(max_length=12)),
                ('Ds_Currency', models.IntegerField()),
                ('Ds_Amount', models.IntegerField()),
                ('Ds_Signature', models.CharField(max_length=256)),
                ('Ds_AuthorisationCode', models.CharField(max_length=256)),
                ('Ds_TransactionType', models.CharField(max_length=1)),
                ('Ds_Merchant_PayMethods', models.CharField(max_length=1, null=True, blank=True)),
                ('Ds_Merchant_Identifier', models.CharField(max_length=40, null=True, blank=True)),
                ('Ds_ExpiryDate', models.CharField(max_length=4, null=True, blank=True)),
                ('Ds_Merchant_Group', models.CharField(max_length=9, null=True, blank=True)),
                ('Ds_Card_Number', models.CharField(max_length=40, null=True, blank=True)),
            ],
        ),
    ]
