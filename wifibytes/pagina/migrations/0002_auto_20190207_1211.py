# Generated by Django 2.1.5 on 2019-02-07 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='idioma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='internationalization.Idioma'),
        ),
        migrations.AlterField(
            model_name='tarifadescriptorgenerico',
            name='idioma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='internationalization.Idioma'),
        ),
        migrations.AlterField(
            model_name='txtcontacto',
            name='idioma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='internationalization.Idioma'),
        ),
    ]
