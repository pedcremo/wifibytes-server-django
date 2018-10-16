# encoding:utf-8
from django.contrib import admin
from .models import RangoICC
from datetime import datetime


class RangoICCAdmin(admin.ModelAdmin):

    ordering = ('-created_at',)

    def creation_date(self, obj):
        if obj.created_at:
            return datetime.fromtimestamp(obj.created_at).strftime('%Y-%m-%d')
        return None
    creation_date.short_description = 'Fecha Creación'

    def count_icc_disponibles(self, obj):
        return len(obj.icc_disponibles)
    count_icc_disponibles.short_description = 'Numero de ICC disponibles'

    def icc_disponibles(self, obj):
        return obj.icc_disponibles
    icc_disponibles.short_description = 'ICC disponibles'

    def count_icc_registrados(self, obj):
        return len(obj.icc_registrados)
    count_icc_registrados.short_description = 'Numero de ICC registrados'

    def icc_registrados(self, obj):
        return obj.icc_registrados
    icc_registrados.short_description = 'ICC registrados'

    def nuevo_icc(self, obj):
        return obj.nuevo_icc_a_registrar
    nuevo_icc.short_description = 'Nuevo ICC'

    search_fields = ('rango_icc_id',)

    readonly_fields = (
        'creation_date',
        'count_icc_disponibles', 'icc_disponibles',
        'count_icc_registrados', 'icc_registrados',
        'nuevo_icc'
    )

    list_display = (
        'rango_icc_init', 'rango_icc_end',
        'creation_date', 'rango_icc_activo'
    )

    fieldsets = (
        ('Informacion ICC', {
            'fields': (
                'rango_icc_init',
                'rango_icc_end',
                'rango_icc_activo',
            ),
        }),
        ('ICC Disponibles', {
            'fields': (
                'count_icc_disponibles',
                'icc_disponibles',
            ),
        }),
        ('ICC Registrados', {
            'fields': (
                'count_icc_registrados',
                'icc_registrados',
            ),
        }),
        ('Nuevo ICC a Registrar', {
            'fields': (
                'nuevo_icc',
            ),
        }),
    )


admin.site.register(RangoICC, RangoICCAdmin)
