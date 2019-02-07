# Generated by Django 2.1.5 on 2019-02-07 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callapi',
            name='codigo_omv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserOmv_CallApi', to='omv.Omv', verbose_name='Codigo OMV'),
        ),
        migrations.AlterField(
            model_name='callapi',
            name='typecall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TypeCallApi_CallApi', to='omv.TypeCallApi', verbose_name='Tipo de Call'),
        ),
        migrations.AlterField(
            model_name='paramcallapi',
            name='call_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CallApi_ParamCallApi', to='omv.CallApi', verbose_name='Call OMV'),
        ),
        migrations.AlterField(
            model_name='paramcallbackapi',
            name='call_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CallApi_ParamCallBackApi', to='omv.CallApi', verbose_name='Call OMV'),
        ),
        migrations.AlterField(
            model_name='userapiomv',
            name='codigo_omv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserOmv_Omv', to='omv.Omv', verbose_name='Codigo OMV'),
        ),
    ]
