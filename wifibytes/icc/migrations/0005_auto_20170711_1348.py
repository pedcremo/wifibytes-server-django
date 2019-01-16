# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icc', '0004_auto_20170711_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangoicc',
            name='rango_icc_activo',
            field=models.BooleanField(default=False, verbose_name=b'Rango Activo'),
        ),
    ]
