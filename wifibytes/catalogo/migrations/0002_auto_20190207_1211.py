# Generated by Django 2.1.5 on 2019-02-07 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='camara',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Articulo_Camara', to='catalogo.Camara'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='codfamilia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familia_codfamilia', to='catalogo.Familia'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Articulo_Marca', to='catalogo.Marca'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='pantalla',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Articulo_Pantalla', to='catalogo.Pantalla'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='procesador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Articulo_Procesador', to='catalogo.Procesador'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='ram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Articulo_Ram', to='catalogo.Ram'),
        ),
        migrations.AlterField(
            model_name='familia',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Familia_PaletaColores', to='pagina.PaletaColores'),
        ),
        migrations.AlterField(
            model_name='subtarifa',
            name='subtarifa_omv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='omv.Omv', verbose_name='Omv asociado a Tarifa'),
        ),
        migrations.AlterField(
            model_name='subtarifa',
            name='subtarifa_tarifa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtarifa_tarifa', to='catalogo.Tarifa', verbose_name='Tarifa'),
        ),
        migrations.AlterField(
            model_name='tarifa',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tarifa_PaletaColores', to='pagina.PaletaColores'),
        ),
        migrations.AlterField(
            model_name='template1',
            name='articulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='template1_articulo', to='catalogo.Articulo'),
        ),
        migrations.AlterField(
            model_name='template1',
            name='idioma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='internationalization.Idioma'),
        ),
        migrations.AlterField(
            model_name='template2',
            name='articulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='template2_articulo', to='catalogo.Articulo'),
        ),
        migrations.AlterField(
            model_name='template2',
            name='idioma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='internationalization.Idioma'),
        ),
        migrations.AlterField(
            model_name='template3',
            name='articulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='template3_articulo', to='catalogo.Articulo'),
        ),
        migrations.AlterField(
            model_name='template3',
            name='idioma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='internationalization.Idioma'),
        ),
    ]
