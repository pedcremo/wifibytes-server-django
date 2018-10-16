from django.contrib import admin
from .models import Provincia, Pais, Comunidad
# Register your models here.


class ProvinciaAdmin(admin.ModelAdmin):

    list_filter = ('codpais__codpais', 'codcomunidad')
    search_fields = ('idprovincia', 'provincia', 'codpais', 'codcomunidad')
    list_display = ('provincia', 'codpais', 'codcomunidad',
                    'codigo')


admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Comunidad)
admin.site.register(Pais)
