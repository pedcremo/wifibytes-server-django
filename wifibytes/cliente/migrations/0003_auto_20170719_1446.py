# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20170717_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentasbcocli',
            name='entidad',
            field=models.CharField(default=b'---', max_length=100, verbose_name=b'Entidad'),
        ),
    ]
