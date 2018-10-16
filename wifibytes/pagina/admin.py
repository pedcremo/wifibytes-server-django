from django.contrib import admin
from .models import *
from django.conf import settings


class HomeAdmin(admin.ModelAdmin):

    model = Home

    def get_actions(self, request):
        actions = super(HomeAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    list_display = ('titulo', 'activo', 'idioma')
    list_filter = ['idioma', 'activo']


class TarifaDescriptorAdmin(admin.ModelAdmin):

    model = TarifaDescriptorGenerico

    def get_actions(self, request):
        actions = super(TarifaDescriptorAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    list_display = ('pretitulo', 'titulo', 'activo', 'idioma')
    list_filter = ['idioma', 'activo']


class TxtContactoAdmin(admin.ModelAdmin):

    model = TxtContacto

    def get_actions(self, request):
        actions = super(TxtContactoAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False


admin.site.register(Home, HomeAdmin)
admin.site.register(TxtContacto, TxtContactoAdmin)
admin.site.register(TarifaDescriptorGenerico, TarifaDescriptorAdmin)
#admin.site.register(FamiliaDescriptor, FamiliaDescriptorAdmin)
admin.site.register(PaletaColores)
