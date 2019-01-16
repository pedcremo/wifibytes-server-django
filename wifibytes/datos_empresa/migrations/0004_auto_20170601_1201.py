# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0003_auto_20170601_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosempresa',
            name='name',
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='test',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Nombre Empresa', blank=True),
        ),
    ]
