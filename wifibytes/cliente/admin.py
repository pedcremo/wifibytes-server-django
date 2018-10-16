# encoding:utf-8
from django.contrib import admin
from .models import *
from django import forms
from django.conf import settings
from django.contrib import messages
from wifibytes.omv_functions import cancelarSolicitud


class CuentasbcoCliInline(admin.StackedInline):
    model = CuentasbcoCli

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-cuentas',),
            'fields': ['ctaentidad', 'iban', 'horaalta', 'entidad', 'horamod',
                       'codigocuenta', 'codpais', 'bic', 'idusuariomod',
                       'cuenta', 'fechaalta', 'fechamod', 'idusuarioalta',
                       'ctadc', 'titular', 'codiban'
                       ]
        }),
    ]

    suit_classes = 'suit-tab suit-tab-cuentas'
    classes = ('collapse closed',)
    list_display = ('entidad', 'iban')
    # fields = ('entidad', 'iban')
    max_num = 1


class MobilsClientsInline(admin.StackedInline):
    model = MobilsClients

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-lineas',),
            'fields': ['draft', 'mobil', 'codtarifa', 'fechaContrato',
                       'roaming', 'roaming_procesing',
                       'buzon_voz', 'buzon_voz_procesing',
                       'coddir', 'tipoTarifaAntigua',
                       'tipoSim', 'companiaAnterior', 'activa', 'alta',
                       'icc_anterior', 'dc_icc_anterior', 'codcuenta', 'nuevoicc']
        }),
    ]
    classes = ('collapse closed',)
    suit_classes = 'suit-tab suit-tab-lineas'
    list_display = ('mobil', 'nombretarifa')
    extra = 1


class DirClientesInline(admin.StackedInline):
    model = DirClientes
    classes = ('collapse closed',)
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-dirclientes',),
            'fields': ['domenvio', 'domfacturacion', 'nombre', 'cifnif',
                       'telefono', 'direccion', 'numero', 'ciudad',
                       'codpostal', 'provincia', 'codpais', 'idprovincia',
                       'default']
        }),
    ]
    suit_classes = 'suit-tab suit-tab-dirclientes'
    list_display = ('domenvio', 'domfacturacion', 'nombre', 'cifnif',
                    'direccion', 'ciudad', 'provincia', 'apartado',
                    'codpostal', 'codpais')
    # fields = ('codcliente', 'domenvio', 'domfacturacion', 'nombre', 'cifnif',
    #           'telefono','direccion', 'ciudad', 'provincia', 'codpostal',
    #           'apartado', 'codpais')
    extra = 1


class ClienteAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-cliente',),
            'fields': ['nombre', 'apellido', 'segundo_apellido',
                       'password', 'birthday_omv', 'nombrecomercial',
                       'cifnif', 'cifnif_imageA', 'cifnif_imageB', 'email',
                       'telefono', 'is_active', 'newsletter']
        }),
        ('Omv', {
            'classes': ('suit-tab', 'suit-tab-omv',),
            'fields': ['tipoidfiscal_type', 'subscriberType_omv',
                       'marketingConsent_omv', 'documentType_omv',
                       'fiscalId_omv']
        })
    ]

    inlines = [
        DirClientesInline, CuentasbcoCliInline, MobilsClientsInline
    ]
    suit_form_tabs = (
        ('cliente', u'Información del cliente'),
        ('dirclientes', 'Direcciones'), ('lineas', 'Lineas'),
        ('cuentas', 'Cuentas Bancarias'), ('omv', u'Campos Eneboo y OMV'))

    list_display = ('codcliente', 'nombre', 'apellido', 'email',
                    'fecha_registro', 'telefono', 'is_active', 'listar_servicios')

    search_fields = ('codcliente', 'nombre', 'apellido', 'email', 'cifnif')

    list_filter = ('fecha_registro', 'is_active')

    def listar_servicios(self, obj):
        return '<a href="/admin/cliente/servicio/?servicio_consumer__codcliente__exact=%s">Servicios</a>' % obj.codcliente
    listar_servicios.allow_tags = True

    if settings.DEBUG is False:
        def get_actions(self, request):
            actions = super(ClienteAdmin, self).get_actions(request)
            del actions['delete_selected']
            return actions

        def has_delete_permission(self, request, obj=None):
            return False


class MobilsClientsAdmin(admin.ModelAdmin):

    def tarifa(self, obj):
        id = obj.codtarifa.codtarifa
        tarifa = obj.codtarifa.nombretarifa
        return '<a href="/admin/catalogo/tarifa/%s">%s</a>' % (id, tarifa)

    tarifa.short_description = 'Tarifa'
    tarifa.allow_tags = True

    def cliente(self, obj):
        id = obj.codcliente.codcliente
        nombre = obj.codcliente.nombre
        apellido = obj.codcliente.apellido
        return '<a href="/admin/cliente/cliente/%s">%s</a>' % (
            id, nombre + ' ' + apellido)

    cliente.short_description = 'Cliente'
    cliente.allow_tags = True

    # def activar_linea(self, obj):
    #     if not obj.activa:
    #         return '<a href="/admin/activar_linea/%s">Activar línea</a>' % (
    #             obj.id_mobilsclients)
    #     else:
    #         return ''
    #
    # activar_linea.short_description = 'Activar Línea'
    # activar_linea.allow_tags = True

    list_display = ('id_mobilsclients', 'mobil', 'tarifa', 'cliente', 'fechaContrato', 'activa')
    search_fields = ('mobil', 'codcliente')
    list_filter = ('codtarifa', 'fechaContrato', 'activa')

    def get_actions(self, request):
        actions = super(MobilsClientsAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        if obj.omv_solicitud:
            try:
                cancelar = cancelarSolicitud(obj.omv_solicitud)
                if cancelar['status_code'] == 200:
                    if cancelar['response_code'] == '0001':
                        obj.delete()
                    else:
                        messages.set_level(request, messages.ERROR)
                        messages.add_message(
                            request, messages.ERROR, cancelar['message'])
                else:
                    messages.set_level(request, messages.ERROR)
                    messages.add_message(
                        request, messages.ERROR, cancelar['message'])
            except Exception as msg:
                messages.set_level(request, messages.ERROR)
                messages.add_message(
                    request, messages.ERROR, msg)
        else:
            obj.delete()

    delete_model.short_description = u'Borrar selección'


class ServicioAdmin(admin.ModelAdmin):
    model = Servicio
    ordering = ('-created_at',)
    list_display = ('servicio_consumer', 'servicio_tarifa',
                    'servicio_direccion', 'servicio_compania_anterior',
                    'servicio_telefono_anterior', 'servicio_draft',
                    'servicio_activo')

    fields = ('servicio_consumer', 'servicio_tarifa',
              'servicio_direccion', 'servicio_compania_anterior',
              'servicio_telefono_anterior', 'servicio_draft',
              'servicio_activo')

    list_filter = ('servicio_consumer', 'servicio_activo',
                   'servicio_draft', 'servicio_tarifa')

    def changelist_view(self, request, extra_context=None):
        # default filter by draft=false
        if 'servicio_draft__exact' not in request.GET:
            q = request.GET.copy()
            q['servicio_draft__exact'] = '0'
            request.GET = q
            request.META['QUERY_STRING'] = request.GET.urlencode()
        return super(ServicioAdmin, self).changelist_view(request, extra_context=extra_context)


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(MobilsClients, MobilsClientsAdmin)
admin.site.register(GruposCliente)
admin.site.register(Servicio, ServicioAdmin)
