# encoding:utf-8
from django.contrib import admin
from .models import *
from django import forms
from django.conf import settings
from django.forms import ModelForm
from suit.widgets import EnclosedInput


class LineaPedidoForm(ModelForm):
    class Meta:
        widgets = {
            'pvptotal': EnclosedInput(append='&euro;'),
            'pvpsindto': EnclosedInput(append='&euro;'),
            'pvpunitario': EnclosedInput(append='&euro;')
        }


class LineaPedidoCliInline(admin.StackedInline):

    form = LineaPedidoForm
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-lineapedido',),
            'fields': ['referencia', 'pvpunitario', 'cantidad', 'pvptotal',
                       'pvpsindto', 'descripcion']
        }),
    ]
    model = LineaPedidoCli
    suit_classes = 'suit-tab suit-tab-lineapedido'
    classes = ('collapse closed',)
    list_display = ('idlinea', 'cantidad')
    extra = 1


class PedidoForm(ModelForm):
    class Meta:
        widgets = {
            'totaleuros': EnclosedInput(append='&euro;'),
            'total': EnclosedInput(append='&euro;'),
            'totaliva': EnclosedInput(append='&euro;'),
            'neto': EnclosedInput(append='&euro;')
        }


class PedidoCliAdmin(admin.ModelAdmin):

    form = PedidoForm

    fieldsets = [
            (None, {
                'classes': ('suit-tab', 'suit-tab-pedidocli',),
                'fields': ['fecha', 'estado', 'formaPago', 'formaEnvio',
                           'neto', 'totaliva', 'total', 'fechasalida',
                           'observaciones', 'generar_factura']
            }),
            ('Cliente', {
                'classes': ('suit-tab', 'suit-tab-infocliente',),
                'fields': ['codcliente', 'nombrecliente', 'cifnif', 'coddir',
                           'direccion', 'provincia', 'ciudad', 'codpostal',
                           'nombreclienteFacturacion', 'cifnifFacturacion',
                           'coddirEnvio', 'direccionEnvio', 'ciudadEnvio',
                           'provinciaEnvio', 'codpostalEnvio']
            }),
            ('Eneboo', {
                'classes': ('suit-tab', 'suit-tab-infoeneboo',),
                'fields': ['codpais', 'codpago', 'codigo', 'tasaconv',
                           'codejercicio', 'irpf', 'porcomision',
                           'idpresupuesto', 'servido', 'codalmacen', 'numero']
            }),
     ]

    def get_nombreUsuario(self, obj):
        nombre = obj.codcliente.nombre
        apellidos = obj.codcliente.apellido
        return nombre + ' ' + apellidos

    get_nombreUsuario.short_description = 'Nombre y Apellidos'

    def get_email(self, obj):
        return obj.codcliente.email

    get_email.short_description = 'Email'

    def formatted_amount(self, obj):
        return '%.2f€' % obj.totaleuros

    formatted_amount.short_description = 'Total Pedido'
    formatted_amount.admin_order_field = 'totaleuros'
    suit_form_tabs = (
        ('pedidocli', u'Información del pedido'),
        ('infocliente', u'Información del cliente'),
        ('lineapedido', u'Líneas del pedido'),
        ('infoeneboo', u'Campos eneboo'))

    inlines = [
        LineaPedidoCliInline
    ]
    model = PedidoCli
    list_display = ('idpedido', 'get_nombreUsuario', 'get_email',
                    'formatted_amount', 'estado', 'fecha', 'formaPago',
                    'pagado')
    classes = ('collapse closed',)
    readonly = ('idpedido')


class FormasEnvioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    search_fields = ('nombre', 'precio')


class FormasPagoAdmin(admin.ModelAdmin):
    list_display = ('cod_eneboo', 'nombre', 'descripcion', 'activa')
    search_fields = ('nombre', 'cod_eneboo')
    list_filter = ('activa',)


class LineasFacturasCliInline(admin.TabularInline):

    def linea_url(self, obj):
        if obj.pk:
            return '<a href="%s%s">Editar</a>' % (
                '/admin/facturacion/lineasfacturascli/', obj.pk)
        return ''

    linea_url.allow_tags = True
    linea_url.short_description = "Link"
    readonly_fields = ('linea_url',)
    fields = ('referencia', 'pvpunitario', 'cantidad', 'pvptotal',
              'iva', 'linea_url')
    model = lineasfacturascli
    fk_name = "idfactura"
    extra = 0


class FacturaClienteAdmin(admin.ModelAdmin):

    def factura_pdf(self, obj):
        if obj.pk:
            return '<a href="%s%s">Descargar</a>' % ('/facturapdf/', obj.pk)
        return ''
    factura_pdf.allow_tags = True
    factura_pdf.short_description = "Factura en PDF"
    readonly_fields = ('factura_pdf',)
    fields = ('codigo', 'numero', 'totaleuros', 'direccion', 'total', 'ciudad',
              'codpostal', 'nombrecliente', 'observaciones', 'codcliente',
              'totaliva', 'fecha', 'hora', 'neto', 'cifnif', 'provincia',
              'factura_pdf', 'coddir', 'recfinanciero', 'totalirpf', 'irpf',
              'tasaconv', 'codpago', 'idpedido')

    inlines = [
        LineasFacturasCliInline,
    ]


admin.site.register(PedidoCli, PedidoCliAdmin)
admin.site.register(FormasPago, FormasPagoAdmin)
admin.site.register(Impuesto)
admin.site.register(FormasEnvio, FormasEnvioAdmin)
admin.site.register(facturasCli, FacturaClienteAdmin)
admin.site.register(lineasfacturascli)
