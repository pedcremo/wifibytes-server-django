# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0012_auto_20170602_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosempresa',
            name='location_lat',
            field=models.DecimalField(null=True, verbose_name=b'Latitud', max_digits=20, decimal_places=20, blank=True),
        ),
        migrations.AlterField(
            model_name='datosempresa',
            name='location_long',
            field=models.DecimalField(null=True, verbose_name=b'Longitud', max_digits=20, decimal_places=20, blank=True),
        ),
    ]
