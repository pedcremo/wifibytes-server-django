# -*- coding: utf-8 -*-


from django.db import models, migrations
import tinymce.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('internationalization', '0001_initial'),
        ('datos_empresa', '0021_auto_20170607_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('texto_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('key', models.CharField(max_length=200, null=True, blank=True)),
                ('content', tinymce.models.HTMLField(null=True, blank=True)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('idioma', models.ForeignKey(to='internationalization.Idioma', null=True)),
                ('textos_contrato_fk', models.ForeignKey(related_name='textos_contrato_fk', verbose_name=b'Textos Contrato', to='datos_empresa.TextosContrato')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Texto Contrato',
                'verbose_name_plural': 'Texto Contratos',
            },
        ),
        migrations.AlterUniqueTogether(
            name='textocontrato',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='textocontrato',
            name='idioma',
        ),
        migrations.RemoveField(
            model_name='textocontrato',
            name='textos_contrato_fk',
        ),
        migrations.DeleteModel(
            name='TextoContrato',
        ),
        migrations.AlterUniqueTogether(
            name='texto',
            unique_together=set([('textos_contrato_fk', 'key', 'idioma')]),
        ),
    ]
