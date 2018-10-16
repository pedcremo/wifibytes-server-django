# encoding:utf-8

from django.contrib import admin
from django.forms import ModelForm
from .models import Articulo, Marca, Procesador, Pantalla, Camara, Tarifa
from .models import Ram, Familia, Template1, Template2, Template3, Subtarifa
from omv.models import *
from suit.widgets import EnclosedInput


class Template1line(admin.StackedInline):
    model = Template1
    suit_classes = 'suit-tab suit-tab-template1'
    classes = ('collapse closed',)
    list_display = ('id', 'titulo')
    extra = 2


class Template1line(admin.StackedInline):
    model = Template1
    suit_classes = 'suit-tab suit-tab-template1'
    classes = ('collapse closed',)
    list_display = ('id', 'titulo')
    extra = 2


class SubtarifasInline(admin.StackedInline):
    model = Subtarifa
    classes = ('collapse closed',)
    suit_classes = 'suit-tab suit-tab-subtarifas'
    fieldsets = [
        (None, {
            'classes': (
                'suit-tab', 'suit-tab-subtarifas'),
            'fields': [
                'subtarifa_datos_internet',
                'subtarifa_cent_minuto', 'subtarifa_est_llamada',
                'subtarifa_precio_sms', 'subtarifa_minutos_gratis',
                'subtarifa_minutos_ilimitados',
                'subtarifa_velocidad_conexion_subida',
                'subtarifa_velocidad_conexion_bajada',
                'subtarifa_num_canales', 'subtarifa_siglas_omv',
                'subtarifa_omv', 'tipo_tarifa', 'subtarifa_tarifa'],
        }),
    ]
    list_display = ('subtarifa_datos_internet',
                    'subtarifa_cent_minuto', 'subtarifa_est_llamada',
                    'subtarifa_precio_sms', 'subtarifa_minutos_gratis',
                    'subtarifa_velocidad_conexion_subida',
                    'subtarifa_velocidad_conexion_bajada',
                    'subtarifa_num_canales', 'subtarifa_siglas_omv',
                    'subtarifa_omv', 'tipo_tarifa')
    extra = 0


class Template2line(admin.StackedInline):
    model = Template2
    suit_classes = 'suit-tab suit-tab-template2'
    classes = ('collapse closed',)
    list_display = ('id', 'titulo')
    extra = 2


class Template3line(admin.StackedInline):
    model = Template3
    suit_classes = 'suit-tab suit-tab-template3'
    classes = ('collapse closed',)
    list_display = ('id', 'titulo')
    extra = 2


class ArticuloForm(ModelForm):
    class Meta:
        widgets = {
            'pvp': EnclosedInput(append='&euro;')
        }


class ArticuloAdmin(admin.ModelAdmin):

    form = ArticuloForm

    fieldsets = [
        (None, {
            'classes': (
                'suit-tab', 'suit-tab-articulo'),
            'fields': [
                'template', 'codfamilia', 'descripcion', 'descripcion_va',
                'descripcion_breve', 'descripcion_breve_va',
                'descripcion_larga', 'descripcion_larga_va',
                'imagen', 'thumbnail', 'pvp', 'marca', 'pantalla',
                'procesador', 'ram', 'camara', 'stockfis', 'visible',
                'activo', 'destacado'],
        }),
        ("Eneboo", {
            'classes': (
                'suit-tab', 'suit-tab-eneboo'),
            'fields': [
                'codimpuesto', 'codbarras', 'tipocodbarras',
                'observaciones', 'stockmax', 'stockmin', 'nostock',
                'controlstock', 'secompra', 'sevende', 'venta_online'],
        }),
    ]

    def get_marca(self, obj):
        if not obj.marca:
            return None
        return obj.marca.Marca

    def formatted_amount(self, obj):
        return '%.2f€' % obj.pvp

    formatted_amount.short_description = 'Precio'
    formatted_amount.admin_order_field = 'pvp'

    get_marca.short_description = 'Marca'

    suit_form_tabs = (('articulo', 'Articulo'), ('eneboo', 'Campos Eneboo'),
                      ('template1', 'Template1'), ('template2', 'Template2'),
                      ('template3', 'Template3'))

    inlines = [Template1line, Template2line, Template3line]

    list_display = ('referencia', 'descripcion', 'codfamilia',
                    'formatted_amount', 'visible', 'stockfis', 'get_marca')

    search_fields = ('referencia', 'descripcion', )

    list_filter = ('activo', 'destacado', 'marca', 'pantalla', 'procesador',
                   'ram', 'camara', 'codfamilia')


class TarifaForm(ModelForm):
    class Meta:
        widgets = {
            'precio': EnclosedInput(append='&euro;'),
        }


class TarifaAdmin(admin.ModelAdmin):

    form = TarifaForm
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-tarifa',),
            'fields': ('nombretarifa', 'pretitulo', 'pretitulo_va',
                       'logo', 'precio', 'activo', 'destacado', 'color')
        })]

    inlines = [
        SubtarifasInline,
    ]
    suit_form_tabs = (
        ('tarifa', u'Información de la Tarifa'),
        ('subtarifas', 'Paquetes Tarifa'))
    list_display = ('codtarifa', 'nombretarifa', 'slug', 'pretitulo',
                    'pretitulo_va', 'logo', 'precio', 'activo', 'destacado',
                    'color')
    # model = Tarifa


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Marca)
admin.site.register(Pantalla)
admin.site.register(Procesador)
admin.site.register(Ram)
admin.site.register(Camara)
admin.site.register(Familia)
admin.site.register(Tarifa, TarifaAdmin)
admin.site.register(Subtarifa)

admin.site.register(Template1)
