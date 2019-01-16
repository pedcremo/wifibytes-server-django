# -*- coding: utf-8 -*-


from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RangoICC',
            fields=[
                ('rango_icc_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('rango_icc_init', models.IntegerField(default=0, verbose_name=b'Rango Inicial')),
                ('rango_icc_end', models.IntegerField(default=0, verbose_name=b'Rango Final')),
                ('rango_icc_default', models.BooleanField(default=False, verbose_name=b'Rango por Defecto')),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('created_at', models.IntegerField(default=0, editable=False)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Rango ICC',
                'verbose_name_plural': 'Rangos ICC',
            },
        ),
    ]
