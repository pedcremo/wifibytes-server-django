# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20170719_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentasbcocli',
            name='entidad',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Entidad', blank=True),
        ),
    ]
