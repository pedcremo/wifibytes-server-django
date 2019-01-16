# -*- coding: utf-8 -*-


from django.db import models, migrations
import django.db.models.deletion
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codcliente', models.CharField(default=False, max_length=100, serialize=False, editable=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name=b'Apellido')),
                ('segundo_apellido', models.CharField(max_length=100, null=True, verbose_name=b'Segundo Apellido', blank=True)),
                ('email', models.CharField(max_length=50, null=True, verbose_name=b'Email')),
                ('genero', models.CharField(blank=True, max_length=1, null=True, choices=[(b'H', b'Hombre'), (b'M', b'Mujer')])),
                ('nombrecomercial', models.CharField(max_length=100, null=True, verbose_name=b'Nombre Comercial', blank=True)),
                ('cifnif', models.CharField(max_length=12, verbose_name=b'Cif Nif')),
                ('cifnif_imageA', models.FileField(upload_to=b'cliente_data', null=True, verbose_name=b'CIFNIF CARA A', blank=True)),
                ('cifnif_imageB', models.FileField(upload_to=b'cliente_data', null=True, verbose_name=b'CIFNIF CARA B', blank=True)),
                ('dni_apoderado', models.CharField(max_length=50, null=True, blank=True)),
                ('fecha_registro', models.DateTimeField(verbose_name=b'Suscripci\xc3\xb3n', editable=False)),
                ('telefono', models.CharField(max_length=30, null=True, verbose_name=b'Telefono', blank=True)),
                ('tipo_cliente', models.IntegerField(default=0, choices=[(0, b'RESIDENCIAL'), (1, b'EMPRESA'), (5, b'AUTONOMO'), (2, b'EXTRANJERO')])),
                ('tipo_documento', models.IntegerField(default=0, choices=[(0, b'DNI'), (1, b'NIE'), (4, b'CIF'), (2, b'PASAPORTE')])),
                ('password', models.CharField(max_length=70, null=True, verbose_name=b'Password', blank=True)),
                ('debaja', models.NullBooleanField(default=None, editable=False)),
                ('observaciones', tinymce.models.HTMLField(null=True, blank=True)),
                ('tipoidfiscal_type', models.IntegerField(blank=True, null=True, verbose_name=b'Tipo Identificaci\xc3\xb3n Fiscal', choices=[(0, b'NIF'), (1, b'NIF/IVA'), (2, b'Pasaporte'), (3, b'Doc. Oficial Pa\xc3\xads'), (4, b'Cert.Residencia'), (5, b'Otro')])),
                ('token', models.CharField(max_length=300, null=True, blank=True)),
                ('is_active', models.BooleanField(default=False)),
                ('newsletter', models.BooleanField(default=False)),
                ('subscriberType_omv', models.IntegerField(null=True, blank=True)),
                ('marketingConsent_omv', models.IntegerField(null=True, blank=True)),
                ('documentType_omv', models.IntegerField(null=True, blank=True)),
                ('fiscalId_omv', models.IntegerField(null=True, blank=True)),
                ('birthday_omv', models.DateField(null=True, verbose_name=b'Fecha de nacimiento', blank=True)),
                ('consumerContract', models.FileField(verbose_name=b'Contrato Cliente', upload_to=b'client_contract', null=True, editable=False)),
                ('consumerSigned', models.IntegerField(default=0, verbose_name=b'Info revisada, \xc2\xbfSe puede proceder con la firma?', choices=[(0, b'No'), (1, b'Si')])),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='CuentasbcoCli',
            fields=[
                ('ctaentidad', models.CharField(max_length=4, verbose_name=b'Cuenta Entidad')),
                ('iban', models.CharField(max_length=34, verbose_name=b'IBAN')),
                ('codiban', models.CharField(max_length=4, null=True, blank=True)),
                ('horaalta', models.DateField(null=True, verbose_name=b'Fecha Creaci\xc3\xb3n', blank=True)),
                ('entidad', models.CharField(max_length=100, null=True, verbose_name=b'Entidad')),
                ('direntidad', models.CharField(max_length=150, null=True, verbose_name=b'Entidad')),
                ('horamod', models.DateTimeField(null=True, verbose_name=b'Fecha Modificaci\xc3\xb3n', blank=True)),
                ('codigocuenta', models.CharField(max_length=30, null=True, verbose_name=b'Codigo Cuenta')),
                ('codpais', models.CharField(max_length=20, null=True, verbose_name=b'Codigo Pais', blank=True)),
                ('ctaagencia', models.CharField(max_length=4)),
                ('bic', models.CharField(max_length=11, null=True, verbose_name=b'BIC')),
                ('titular', models.CharField(max_length=200, null=True, blank=True)),
                ('codcuenta', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('idusuariomod', models.CharField(max_length=50, null=True, verbose_name=b'Id usuario ')),
                ('cuenta', models.CharField(max_length=10, null=True, verbose_name=b'Cuenta')),
                ('fechaalta', models.DateField(null=True, verbose_name=b'Fecha Alta', blank=True)),
                ('fechamod', models.DateField(null=True, verbose_name=b'Fecha Mod', blank=True)),
                ('idusuarioalta', models.CharField(max_length=50, null=True, verbose_name=b'Id Usuario Alta')),
                ('ctadc', models.CharField(max_length=2, null=True, verbose_name=b'CTADC')),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('codcliente', models.ForeignKey(related_name='cuentasbco_cliente', to='cliente.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='DirClientes',
            fields=[
                ('id', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('domenvio', models.BooleanField(default=False, verbose_name=b'Domicilio de Envio')),
                ('domfacturacion', models.BooleanField(default=False, verbose_name=b'Datos de Facturaci\xc3\xb3n')),
                ('nombre', models.CharField(default=None, max_length=250, null=True, verbose_name=b'Nombre / Empresa', blank=True)),
                ('cifnif', models.CharField(default=None, max_length=10, null=True, verbose_name=b'DNI/CIF/NIE', blank=True)),
                ('direccion', models.CharField(max_length=350, verbose_name=b'Direcci\xc3\xb3n')),
                ('numero', models.CharField(max_length=350, blank=True)),
                ('codpais', models.CharField(default=b'ES', max_length=100, null=True, verbose_name=b'Codigo de Pais', blank=True)),
                ('ciudad', models.CharField(max_length=100, verbose_name=b'Ciudad')),
                ('provincia', models.CharField(max_length=100, null=True, verbose_name=b'Provincia', blank=True)),
                ('apartado', models.CharField(max_length=10, null=True, verbose_name=b'Apartado', blank=True)),
                ('codpostal', models.CharField(max_length=10, null=True, verbose_name=b'Codigo Postal')),
                ('telefono', models.IntegerField(null=True, verbose_name=b'Tel\xc3\xa9fono de contacto')),
                ('default', models.BooleanField(default=False)),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('codcliente', models.ForeignKey(related_name='DirClientes_Cliente', verbose_name=b'Codigo Cliente', to='cliente.Cliente')),
                ('idprovincia', models.ForeignKey(related_name='dir_prov', verbose_name=b'Id Provincia', to='geo.Provincia', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GruposCliente',
            fields=[
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('codgrupo', models.IntegerField(verbose_name=b'Codigo Grupo', serialize=False, editable=False, primary_key=True)),
                ('codtarifa', models.ForeignKey(related_name='GruposClientes_Tarifa', verbose_name=b'Codigo tarifa', to='catalogo.Tarifa')),
            ],
        ),
        migrations.CreateModel(
            name='MobilsClients',
            fields=[
                ('id_mobilsclients', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('mobil', models.CharField(max_length=20, null=True, verbose_name='M\xf3vil', blank=True)),
                ('nuevoicc', models.CharField(max_length=50, null=True, blank=True)),
                ('fechaContrato', models.DateField(null=True, verbose_name=b'Fecha Contrato', blank=True)),
                ('imageContrato', models.FileField(upload_to=b'cliente_data', null=True, verbose_name=b'Image Contrato', blank=True)),
                ('roaming', models.BooleanField(default=False)),
                ('buzon_voz', models.BooleanField(default=False)),
                ('origen', models.IntegerField(default=0, choices=[(0, b'Alta'), (1, b'Portabilidad')])),
                ('tipoTarifaAntigua', models.IntegerField(blank=True, null=True, verbose_name=b'Tipo de tarifa anterior', choices=[(0, b'Contrato'), (1, b'Tarjeta')])),
                ('tipoSim', models.IntegerField(blank=True, null=True, verbose_name=b'Tipo de Sim', choices=[(0, b'Sim'), (1, b'Microsim'), (2, b'Nanosim')])),
                ('companiaAnterior', models.IntegerField(blank=True, null=True, verbose_name=b'Compa\xc3\xb1\xc3\xada anterior', choices=[(0, b'Movistar'), (1, b'Vodafone'), (2, b'Orange'), (3, b'Yoigo'), (4, b'Pepephone'), (5, b'Simyo')])),
                ('icc_anterior', models.IntegerField(null=True, blank=True)),
                ('dc_icc_anterior', models.IntegerField(null=True, blank=True)),
                ('activa', models.BooleanField(default=False, verbose_name=b'L\xc3\xadnea activa')),
                ('alta', models.BooleanField(default=False, verbose_name=b'L\xc3\xadnea dada de alta')),
                ('omv_solicitud', models.CharField(max_length=100, null=True, verbose_name=b'N. de solicitud', blank=True)),
                ('signature_id', models.CharField(max_length=500, null=True, blank=True)),
                ('document_id', models.CharField(max_length=500, null=True, blank=True)),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('draft', models.BooleanField(default=True, verbose_name=b'Borrador')),
                ('codcliente', models.ForeignKey(related_name='MobilsClients_Cliente', verbose_name=b'Codigo Cliente', to='cliente.Cliente')),
                ('codcuenta', models.ForeignKey(related_name='MobilsClients_CuentasbcoCli', verbose_name=b'Cuenta Cliente', blank=True, to='cliente.CuentasbcoCli', null=True)),
                ('coddir', models.ForeignKey(related_name='MobilsClients_DirClientes', verbose_name=b'Datos de Facturaci\xc3\xb3n', blank=True, to='cliente.DirClientes', null=True)),
                ('codtarifa', models.ForeignKey(related_name='MobilsClients_Tarifa', verbose_name=b'Codigo Tarifa', to='catalogo.Tarifa')),
            ],
            options={
                'verbose_name': 'L\xednea',
                'verbose_name_plural': 'L\xedneas',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('servicio_id', models.IntegerField(serialize=False, editable=False, primary_key=True)),
                ('servicio_compania_anterior', models.CharField(max_length=250, null=True, verbose_name=b'Compa\xc3\xb1ia anterior')),
                ('servicio_telefono_anterior', models.IntegerField(null=True, verbose_name=b'Tel\xc3\xa9fono anterior')),
                ('servicio_draft', models.BooleanField(default=False, verbose_name=b'Borrador')),
                ('created_at', models.IntegerField(default=0, editable=False)),
                ('updated_at', models.IntegerField(default=0, editable=False)),
                ('servicio_activo', models.BooleanField(default=False, verbose_name=b'Activo')),
                ('servicio_consumer', models.ForeignKey(verbose_name=b'Cliente', to='cliente.Cliente')),
                ('servicio_cuenta', models.ForeignKey(to='cliente.CuentasbcoCli', null=True)),
                ('servicio_direccion', models.ForeignKey(verbose_name=b'Direcci\xc3\xb3n', to='cliente.DirClientes', null=True)),
                ('servicio_tarifa', models.ForeignKey(verbose_name=b'Tarifa', to='catalogo.Tarifa')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='codcuentadom',
            field=models.ForeignKey(verbose_name=b'Cuenta Domiciliacion', to='cliente.CuentasbcoCli', null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='consumer_user',
            field=models.OneToOneField(related_name='rel_Codcliente', null=True, on_delete=django.db.models.deletion.SET_NULL, editable=False, to=settings.AUTH_USER_MODEL, verbose_name=b'Consumer User'),
        ),
    ]
