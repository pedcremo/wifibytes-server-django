# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20170719_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentasbcocli',
            name='bic',
            field=models.CharField(max_length=11, null=True, verbose_name=b'BIC', blank=True),
        ),
        migrations.AlterField(
            model_name='cuentasbcocli',
            name='ctadc',
            field=models.CharField(max_length=2, null=True, verbose_name=b'CTADC', blank=True),
        ),
        migrations.AlterField(
            model_name='cuentasbcocli',
            name='cuenta',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Cuenta', blank=True),
        ),
        migrations.AlterField(
            model_name='cuentasbcocli',
            name='idusuarioalta',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Id Usuario Alta', blank=True),
        ),
        migrations.AlterField(
            model_name='cuentasbcocli',
            name='idusuariomod',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Id usuario ', blank=True),
        ),
    ]
