# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icc', '0003_auto_20170711_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rangoicc',
            old_name='rango_icc_default',
            new_name='rango_icc_activo',
        ),
    ]
