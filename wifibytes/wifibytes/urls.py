# -*- coding: utf-8 -*-
#from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *

from django.conf import settings
from django.views.generic import TemplateView
from rest_framework import routers, viewsets, permissions
from .hybridrouter import HybridRouter
from django.contrib.admin.sites import AdminSite

from cliente.views import *
from cliente.models import *

from empresa.views import *
from empresa.models import *

from facturacion.views import *
from facturacion.models import *

from omv.views import *
from omv.models import *

from catalogo.views import *
from catalogo.models import *

from causa.views import *
from causa.models import *

from pagina.views import *
from pagina.models import *

from geo.views import ProvinciaViewSet

from datos_empresa.views import DatosEmpresaViewSet

from administracion.views import SitemapView, DocOmvView, TestDocOmvView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


router = HybridRouter()
router.register(r"formasenvio", FormasEnvioViewSet)
router.register(r"formaspago", FormasPagoViewSet)
router.register(r"facturascli", FacturascliViewSet)
router.register(r"provincias", ProvinciaViewSet)
router.register(r"direcciones", DireccionesViewSet)
router.register(r"cliente", ClienteViewSet)
router.register(r"linea", LineaViewSet)
router.register(r"cuentas", CuentaViewSet)
router.register(r"articulo", ArticuloViewSet)
router.register(r"servicio", ServicioViewSet)
router.register(r"tarifa", TarifaViewSet, 'Tarifa')
router.register(r"familia", FamiliaViewSet, 'familia')
router.register(r"datos_empresa", DatosEmpresaViewSet, 'datos_empresa')


router.add_api_view(
    "[OMV] ACTIVAR LINEA ", url(
        r'^activar_linea/$', activarLinea.as_view(), name='activarLinea'))

# Facturas
#router.add_api_view("[FACTURACION] Listado de facturas", url(r'^facturascli/$', FacturascliAPIListView.as_view(), name='facturascli-list'))


router.add_api_view(
    "[SIGNATURIT] GET CONTRACTS ", url(
        r'^get_contracts/$', getContracts.as_view(), name='getContracts'))
router.add_api_view(
    "[CLIENTE] GET ALL - POST PARAM MULTIPLEs ", url(
        r'^clientes/$', ClienteAPIView.as_view(), name='clientes'))
router.add_api_view("[CLIENTE] GET Refresh password No Registrado", url(
    r'^clientenoreg/$', ClienteNoRegistradoView.as_view(), name='cliente-no-registrado'))
router.add_api_view("[CLIENTE] MobilsClients", url(
    r'^mobilscli/$', mobils_clientsAPIListView.as_view(), name='mobile-registrado'))
# router.add_api_view("[CLIENTE] DirClientes_Cliente", url(r'^dirscli/$', dirclientesAPIListView.as_view(), name='dir-registrado'))
router.add_api_view("[CLIENTE] CuentasbcoCli", url(
    r'^cuentascli/$', cuentasbcocliAPIListView.as_view(), name='cliente-registrado'))
router.add_api_view(
    "[CLIENTE] obtenerConsumoCliente", url(
        r'^consumo_datos/$', obtenerConsumoCliente.as_view(),
        name='obtenerConsumoCliente'))
router.add_api_view(
    "[CLIENTE] nuevaAlta", url(
        r'^nueva_alta/$', nuevaAlta.as_view(),
        name='nuevaAlta'))

router.add_api_view(
    "[OMV] setServicios", url(
        r'^setServicios/$', SetServiciosView.as_view(),
        name='setServicios'))


#router.add_api_view("[FACTURACION] Formas de pago", url(r'^formaspago/$', FormasPagoAPIListView.as_view(), name='formaspago-list'))
router.add_api_view("[FACTURACION] Lineas pedidos cliente", url(
    r'^lineaspedidoscli/$', LineaspedidoscliAPIListView.as_view(), name='lineaspedidoscli-list'))
router.add_api_view("[FACTURACION] Listado de pedidos", url(
    r'^pedidoscli/$', PedidoscliAPIListView.as_view(), name='pedidoscli-list'))
router.add_api_view("[FACTURACION] Pedidos de pago", url(
    r'^pedidos/$', PedidoscliAPIView.as_view(), name='pedidoscli'))
router.add_api_view("[FACTURACION] Impuestos de pago", url(
    r'^impuestos/$', ImpuestosAPIListView.as_view(), name='impuestos-list'))

# End points terminados
router.add_api_view("[FRONTEND] Home Elements ", url(
    r'^home/$', HomeAPIListView.as_view(), name='homeAPIListView'))
router.add_api_view("[FRONTEND] Tarifa Descripción Elements", url(
    r'^tarifa_descriptor/$', TarifaDescriptorAPIListView.as_view(), name='tarifaDescriptorAPIListView'))
router.add_api_view("[FRONTEND] Txt Contacto", url(r'^txtcontacto/$',
                                                   TxtContactoAPIListView.as_view(), name='TxtContactoAPIListView'))

router.add_api_view("[CAUSA] GET Causa List", url(
    r'^causa/$', CausaAPIListView.as_view(), name='causa-list'))
router.add_api_view("[CONTACTO] Contacto", url(r'^contacto/$', Contacto.as_view(), name='contacto'))

router.add_api_view("[EMPRESA]", url(
    r'^empresa/$', EmpresaAPIListView.as_view(), name='empresa-list'))
router.add_api_view("[OMV]Omv", url(r'^omv/$', OmvAPIListView.as_view(), name='omv-list'))
router.add_api_view("[OMV] Numeros Disponibles", url(r'^numeros_disponibles/$',
                                                     omvDisponibleNumbers.as_view(), name='omvDisponibleNumbers'))


# endpoints
# router.add_api_view("[CATALOGO] tarifa", url(r'^tarifa/$', TarifaView.as_view(), name='Tarifa'))
# router.register("[CATALOGO] familia", url(r'^familia/$', FamiliaViewSet, name='familia'))
router.add_api_view("[CATALOGO] paleta de colores", url(
    r'^paletacolores/$', PaletaColoresView.as_view(), name='paletacolores'))
# router.add_api_view("[CATALOGO] articulo", url(r'^articulo/$', ArticuloView.as_view(), name='articulo'))
router.add_api_view("[CATALOGO] filtros", url(r'^filtros/$', FiltrosView.as_view(), name='filtros'))
router.add_api_view("[CAUSA] POST causa", url(
    r'^newcausa/$', NewCausaAPIView.as_view(), name='newcausa'))
router.add_api_view("[PAYMENT] MAKEPAYMENT", url(
    r'^makepayment/$', MakePayment.as_view(), name='makepayment'))

router.add_api_view(
    "[SITEMAP]", url(
        r'^api/sitemap/$', SitemapView.as_view(), name='SitemapView'))

#urlpatterns = patterns(
urlpatterns = [
    '',
    # para traer por id
    url(r'^causa/(?P<id>[0-9]+)$', CausaAPIView.as_view(), name='causa'),
    # url(r'^tarifa/(?P<pk>[0-9]+)/$', TarifaDetailView.as_view()),
    url(r'^paletacolores/(?P<pk>[0-9]+)/$', PaletaColoresDetailView.as_view()),
    # url(r'^articulo/(?P<pk>[\w|\W]+)/$', ArticuloDetailView.as_view()),
    url(r'^facturapdf/(?P<pk>[0-9]+)/$', 'facturacion.views.factura_pdf', name="facturapdf"),
    url(r'^contratopdf/(?P<linea>[0-9]+)/$', 'facturacion.views.contrato_pdf', name="contratopdf"),
    # url(r'^admin/activar_linea/(?P<id_linea>\d+)$', 'cliente.admin_views.activar_linea', name="activar_linea"),

    url(r'^', include(router.urls)),
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    # Uncomment the next line to enable the admin:
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),
    # grappelli URLS
    #url(r'^docs/', include('rest_framework_swagger.urls')),

    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'pedidosdashboard/$', 'facturacion.views.ultimospedidosdashboard', name="pedidosdashboard"),
    url(r'lineasdashboard/$', 'cliente.views.ultimaslineasdashboard', name="lineasdashboard"),
    url(r'clientesdashboard/$', 'cliente.views.ultimosclientesdashboard', name="clientesdashboard"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^documentacion-omv/$', DocOmvView, name='documentacion_omv'),
    url(r'^documentacion-omv/test/(?P<call>\w+)/', TestDocOmvView, name='documentacionOmvTest'),


    #url(r"^payments/", include("pinax.stripe.urls")),
    # sermepa
    #url(r'^sermepa/', include('sermepa.urls')),
    # url(regex = r'^pago/',view = 'facturacion.views.form',name = 'pago'),
    # url(regex = r'^end/',view = 'facturacion.views.end',name = 'end'),
#)
]

AdminSite.index_template = 'index.html'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
