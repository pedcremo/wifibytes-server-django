# encoding:utf-8
from django.contrib import admin
from datos_empresa.models import (
    DatosEmpresa, InfoEmpresa, TextosContrato, Texto, DatosEmail
)
from datetime import datetime


class InfoEmpresaInLine(admin.StackedInline):
    model = InfoEmpresa
    suit_classes = 'suit-tab suit-tab-infoEmpresa'
    extra = 0


class DatosEmailInLine(admin.StackedInline):
    model = DatosEmail
    suit_classes = 'suit-tab suit-tab-datosEmail'
    extra = 0


class DatosEmpresaAdmin(admin.ModelAdmin):
    inlines = [InfoEmpresaInLine, DatosEmailInLine]

    ordering = ('-created_at',)

    def creation_date(self, obj):
        if obj.created_at:
            return datetime.fromtimestamp(obj.created_at).strftime('%Y-%m-%d')
        return None
    creation_date.short_description = 'Fecha Creación'

    search_fields = ('datos_empresa_id',)
    readonly_fields = ('creation_date','logo_thumb','icon_logo_thumb','mapa_cobertura_thumb')

    suit_form_tabs = (
        ('general', 'General'),
        ('infoEmpresa', 'Textos'),
        ('datosEmail', 'Configuración Email'),
    )
    list_display = (
        'name',
        'cifnif',
        'phone',
        'city',
        'province',
        'country',
        'datos_empresa_default',
    )
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'name', 'cifnif', 'phone',
                'city', 'province', 'country', 'zipcode',
                'address', 'location_lat', 'location_long',
                'logo','logo_thumb','icon_logo','icon_logo_thumb','mapa_cobertura','mapa_cobertura_thumb',
                'social_facebook', 'social_twitter',
                'datos_empresa_default', 'creation_date',
            ]
        }),
    ]


class TextoContratoInLine(admin.StackedInline):
    model = Texto
    suit_classes = 'suit-tab suit-tab-textoContrato'
    extra = 0


class TextosContratoAdmin(admin.ModelAdmin):
    inlines = [TextoContratoInLine, ]

    ordering = ('-created_at',)

    def creation_date(self, obj):
        if obj.created_at:
            return datetime.fromtimestamp(obj.created_at).strftime('%Y-%m-%d')
        return None
    creation_date.short_description = 'Fecha Creación'

    search_fields = ('textos_contrato_id',)
    readonly_fields = ('creation_date',)

    suit_form_tabs = (
        ('textoContrato', 'Textos'),
    )
    list_display = (
        'creation_date',
        'textos_contrato_default'
    )


admin.site.register(DatosEmpresa, DatosEmpresaAdmin)
admin.site.register(TextosContrato, TextosContratoAdmin)
