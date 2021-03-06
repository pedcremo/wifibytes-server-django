# Generated by Django 2.1.5 on 2019-01-18 10:45

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('internationalization', '0001_initial'),
        ('omv', '0001_initial'),
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('referencia', models.CharField(editable=False, max_length=100, primary_key=True, serialize=False)),
                ('slug', models.SlugField(editable=False)),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripción [ES]')),
                ('descripcion_va', models.CharField(blank=True, max_length=250, verbose_name='Descripción [VA]')),
                ('pvp', models.FloatField(default=0)),
                ('stockfis', models.FloatField(default=0)),
                ('descripcion_breve', models.CharField(max_length=250, verbose_name='Descripción breve [ES]')),
                ('descripcion_breve_va', models.CharField(blank=True, max_length=250, verbose_name='Descripción breve [VA]')),
                ('descripcion_larga', tinymce.models.HTMLField(verbose_name='Especificaciones [ES]')),
                ('descripcion_larga_va', tinymce.models.HTMLField(blank=True, verbose_name='Especificaciones [VA]')),
                ('template', models.IntegerField(choices=[(1, 'Template 1'), (2, 'Template 2'), (3, 'Template 3')], verbose_name='Template Seleccionado')),
                ('imagen', models.FileField(upload_to='pagina_tarifas', verbose_name='Imagen')),
                ('thumbnail', models.FileField(upload_to='pagina_tarifas', verbose_name='thumbnail')),
                ('activo', models.BooleanField(default=0, verbose_name='Artículo Activo')),
                ('visible', models.BooleanField(default=False)),
                ('destacado', models.BooleanField(default=False)),
                ('secompra', models.BooleanField(default=True)),
                ('stockmax', models.FloatField(default=0)),
                ('codimpuesto', models.CharField(default='IVA21%', max_length=10, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('codbarras', models.CharField(blank=True, max_length=18, null=True, verbose_name='Codigo Barras')),
                ('nostock', models.BooleanField(default=False)),
                ('controlstock', models.BooleanField(default=False)),
                ('tipocodbarras', models.CharField(blank=True, choices=[('Code39', 'Code39'), ('Code128', 'Code128'), ('Code128B', 'Code128B'), ('Code128C', 'Code128C'), ('Code128R', 'Code128R'), ('EAN', 'EAN'), ('ISBN', 'ISBN'), ('UPC', 'UPC'), ('CodeI25', 'CodeI25'), ('CBR', 'CBR'), ('MSI', 'MSI'), ('PLS', 'PLS'), ('Code93', 'Code93')], max_length=8, null=True)),
                ('sevende', models.BooleanField(default=True)),
                ('venta_online', models.BooleanField(default=True)),
                ('stockmin', models.FloatField(default=0)),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Camara',
            fields=[
                ('num_camara', models.FloatField()),
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('codfamilia', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Código Familia')),
                ('slug', models.SlugField(editable=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre [ES]')),
                ('nombre_va', models.CharField(blank=True, max_length=200, verbose_name='Nombre [VA]')),
                ('icono', models.FileField(upload_to='familia')),
                ('pretitulo', models.CharField(max_length=200, verbose_name='Pretitulo [ES]')),
                ('pretitulo_va', models.CharField(blank=True, max_length=200, verbose_name='Pretitulo [VA]')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo [ES]')),
                ('titulo_va', models.CharField(blank=True, max_length=200, verbose_name='Titulo [VA]')),
                ('precio_cabecera', models.FloatField(null=True)),
                ('imagen_cabecera', models.FileField(null=True, upload_to='familia')),
                ('thumbnail', models.FileField(editable=False, null=True, upload_to='familia')),
                ('activo', models.BooleanField(default=False)),
                ('texto_cabecera', tinymce.models.HTMLField(verbose_name='Texto cabecera [ES]')),
                ('texto_cabecera_va', tinymce.models.HTMLField(blank=True, verbose_name='Texto cabecera [VA]')),
                ('subtexto_cabecera', tinymce.models.HTMLField(verbose_name='Subtexto cabecera [ES]')),
                ('subtexto_cabecera_va', tinymce.models.HTMLField(blank=True, verbose_name='Subtexto cabecera [VA]')),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Familia_PaletaColores', to='pagina.PaletaColores')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('Marca', models.CharField(max_length=100)),
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pantalla',
            fields=[
                ('num_pantalla', models.FloatField()),
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Procesador',
            fields=[
                ('num_procesador', models.CharField(max_length=100)),
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('num_ram', models.CharField(max_length=100)),
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subtarifa',
            fields=[
                ('subtarifa_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('subtarifa_datos_internet', models.FloatField(blank=True, null=True, verbose_name='Importe Datos')),
                ('subtarifa_cent_minuto', models.FloatField(blank=True, null=True, verbose_name='Importe minutos (cent/min)')),
                ('subtarifa_est_llamada', models.FloatField(blank=True, null=True)),
                ('subtarifa_precio_sms', models.FloatField(blank=True, null=True, verbose_name='Importe sms')),
                ('subtarifa_velocidad_conexion_subida', models.FloatField(blank=True, null=True, verbose_name='Velocidad de conexión subida')),
                ('subtarifa_velocidad_conexion_bajada', models.FloatField(blank=True, null=True, verbose_name='Velocidad de conexión bajada')),
                ('subtarifa_num_canales', models.IntegerField(blank=True, null=True)),
                ('subtarifa_minutos_gratis', models.IntegerField(blank=True, null=True, verbose_name='Minutos gratis')),
                ('subtarifa_minutos_ilimitados', models.BooleanField(default=False)),
                ('subtarifa_siglas_omv', models.CharField(blank=True, max_length=100, null=True, verbose_name='Siglas de la tarifa')),
                ('tipo_tarifa', models.IntegerField(choices=[(1, 'Móvil'), (2, 'Fijo'), (3, 'Fibra'), (4, 'Wifi'), (5, 'TV')], default=0)),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('subtarifa_omv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='omv.Omv', verbose_name='Omv asociado a Tarifa')),
            ],
            options={
                'verbose_name': 'Paquete Tarifa',
                'verbose_name_plural': 'Paquetes Tarifa',
            },
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('codtarifa', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('nombretarifa', models.CharField(max_length=100, verbose_name='Nombre tarifa')),
                ('slug', models.SlugField(editable=False)),
                ('pretitulo', models.CharField(max_length=100, verbose_name='Pretitulo [ES]')),
                ('pretitulo_va', models.CharField(blank=True, max_length=100, verbose_name='Pretitulo [VA]')),
                ('logo', models.FileField(upload_to='Logo')),
                ('precio', models.FloatField(verbose_name='Importe tarifa ')),
                ('activo', models.BooleanField(default=0, verbose_name='Activo')),
                ('destacado', models.BooleanField(default=False)),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Tarifa_PaletaColores', to='pagina.PaletaColores')),
            ],
        ),
        migrations.CreateModel(
            name='Template1',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('pretitulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='pretitulo')),
                ('caja_1_titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='caja_1_titulo')),
                ('caja_1_texto', tinymce.models.HTMLField(blank=True, null=True)),
                ('caja_2_titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='caja_2_titulo')),
                ('caja_2_texto', tinymce.models.HTMLField(blank=True, null=True)),
                ('caja_3_titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='caja_3_titulo')),
                ('caja_3_texto', tinymce.models.HTMLField(blank=True, null=True)),
                ('caja_4_titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='caja_4_titulo')),
                ('caja_4_texto', tinymce.models.HTMLField(blank=True, null=True)),
                ('imagen1', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='Imagen1')),
                ('imagen2', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='Imagen2')),
                ('imagen3', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='Imagen3')),
                ('imagen_fondo_cabecera', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='imagen_fondo_cabecera')),
                ('imagen_fondo_cuerpo', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='imagen_fondo_cuerpo')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='template1_articulo', to='catalogo.Articulo')),
                ('idioma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='internationalization.Idioma')),
            ],
        ),
        migrations.CreateModel(
            name='Template2',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('pretitulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='pretitulo')),
                ('caja_1_titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='caja_1_titulo')),
                ('caja_1_texto', tinymce.models.HTMLField(blank=True, null=True)),
                ('caja_2_titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='caja_2_titulo')),
                ('caja_2_texto', tinymce.models.HTMLField(blank=True, null=True)),
                ('caja_3_titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='caja_3_titulo')),
                ('caja_3_texto', tinymce.models.HTMLField(blank=True, null=True)),
                ('caja_4_titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='caja_4_titulo')),
                ('caja_4_texto', tinymce.models.HTMLField(blank=True, null=True)),
                ('imagen1', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='Imagen1')),
                ('imagen2', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='Imagen2')),
                ('imagen3', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='Imagen3')),
                ('imagen4', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='Imagen4')),
                ('imagen_fondo_cabecera', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='imagen_fondo_cabecera')),
                ('imagen_fondo_cuerpo', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='imagen_fondo_cuerpo')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='template2_articulo', to='catalogo.Articulo')),
                ('idioma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='internationalization.Idioma')),
            ],
        ),
        migrations.CreateModel(
            name='Template3',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('pretitulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='pretitulo')),
                ('franja_1_texto', tinymce.models.HTMLField(blank=True, null=True)),
                ('franja_1_fondo', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='imagen_fondo_cabecera')),
                ('caja_1_titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='caja_1_titulo')),
                ('caja_1_texto', tinymce.models.HTMLField(blank=True, null=True)),
                ('caja_2_titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='caja_2_titulo')),
                ('caja_2_texto', tinymce.models.HTMLField(blank=True, null=True)),
                ('franja_2_texto', tinymce.models.HTMLField(blank=True, null=True)),
                ('franja_2_fondo', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='imagen_fondo_cabecera')),
                ('imagen1', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='Imagen1')),
                ('imagen2', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='Imagen2')),
                ('imagen3', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='Imagen3')),
                ('imagen4', models.FileField(blank=True, null=True, upload_to='Templates', verbose_name='Imagen4')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='template3_articulo', to='catalogo.Articulo')),
                ('idioma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='internationalization.Idioma')),
            ],
        ),
        migrations.AddField(
            model_name='subtarifa',
            name='subtarifa_tarifa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subtarifa_tarifa', to='catalogo.Tarifa', verbose_name='Tarifa'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='camara',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Articulo_Camara', to='catalogo.Camara'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='codfamilia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='familia_codfamilia', to='catalogo.Familia'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Articulo_Marca', to='catalogo.Marca'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='pantalla',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Articulo_Pantalla', to='catalogo.Pantalla'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='procesador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Articulo_Procesador', to='catalogo.Procesador'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='ram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Articulo_Ram', to='catalogo.Ram'),
        ),
        migrations.AlterIndexTogether(
            name='familia',
            index_together={('codfamilia', 'nombre')},
        ),
    ]
