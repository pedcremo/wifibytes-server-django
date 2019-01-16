# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20170711_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template2',
            name='articulo',
            field=models.ForeignKey(related_name='template2_articulo', to='catalogo.Articulo'),
        ),
        migrations.AlterField(
            model_name='template3',
            name='articulo',
            field=models.ForeignKey(related_name='template3_articulo', to='catalogo.Articulo'),
        ),
    ]
