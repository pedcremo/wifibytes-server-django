# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosempresa',
            name='cifnif',
        ),
        migrations.RemoveField(
            model_name='datosempresa',
            name='icon_logo',
        ),
        migrations.RemoveField(
            model_name='datosempresa',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='datosempresa',
            name='name',
        ),
    ]
