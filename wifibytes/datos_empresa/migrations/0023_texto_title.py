# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_empresa', '0022_auto_20170607_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='texto',
            name='title',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
