# -*- coding: utf-8 -*-
#from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from django.urls import include, path,re_path
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

#PERE CHANGE
from rest_framework_jwt.views import *

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
    "[OMV] ACTIVAR LINEA ", path(
        r'^activar_linea/$', activarLinea.as_view(), name='activarLinea'))

# Facturas
#router.add_api_view("[FACTURACION] Listado de facturas", path(r'^facturascli/$', FacturascliAPIListView.as_view(), name='facturascli-list'))


router.add_api_view(
    "[SIGNATURIT] GET CONTRACTS ", path(
        r'^get_contracts/$', getContracts.as_view(), name='getContracts'))
router.add_api_view(
    "[CLIENTE] GET ALL - POST PARAM MULTIPLEs ", path(
        r'^clientes/$', ClienteAPIView.as_view(), name='clientes'))
router.add_api_view("[CLIENTE] GET Refresh password No Registrado", path(
    r'^clientenoreg/$', ClienteNoRegistradoView.as_view(), name='cliente-no-registrado'))
router.add_api_view("[CLIENTE] MobilsClients", path(
    r'^mobilscli/$', mobils_clientsAPIListView.as_view(), name='mobile-registrado'))
# router.add_api_view("[CLIENTE] DirClientes_Cliente", path(r'^dirscli/$', dirclientesAPIListView.as_view(), name='dir-registrado'))
router.add_api_view("[CLIENTE] CuentasbcoCli", path(
    r'^cuentascli/$', cuentasbcocliAPIListView.as_view(), name='cliente-registrado'))
router.add_api_view(
    "[CLIENTE] obtenerConsumoCliente", path(
        r'^consumo_datos/$', obtenerConsumoCliente.as_view(),
        name='obtenerConsumoCliente'))
router.add_api_view(
    "[CLIENTE] nuevaAlta", path(
        r'^nueva_alta/$', nuevaAlta.as_view(),
        name='nuevaAlta'))

router.add_api_view(
    "[OMV] setServicios", path(
        r'^setServicios/$', SetServiciosView.as_view(),
        name='setServicios'))


#router.add_api_view("[FACTURACION] Formas de pago", path(r'^formaspago/$', FormasPagoAPIListView.as_view(), name='formaspago-list'))
router.add_api_view("[FACTURACION] Lineas pedidos cliente", path(
    r'^lineaspedidoscli/$', LineaspedidoscliAPIListView.as_view(), name='lineaspedidoscli-list'))
router.add_api_view("[FACTURACION] Listado de pedidos", path(
    r'^pedidoscli/$', PedidoscliAPIListView.as_view(), name='pedidoscli-list'))
router.add_api_view("[FACTURACION] Pedidos de pago", path(
    r'^pedidos/$', PedidoscliAPIView.as_view(), name='pedidoscli'))
router.add_api_view("[FACTURACION] Impuestos de pago", path(
    r'^impuestos/$', ImpuestosAPIListView.as_view(), name='impuestos-list'))

# End points terminados
router.add_api_view("[FRONTEND] Home Elements ", path(
    r'^home/$', HomeAPIListView.as_view(), name='homeAPIListView'))
router.add_api_view("[FRONTEND] Tarifa Descripción Elements", path(
    r'^tarifa_descriptor/$', TarifaDescriptorAPIListView.as_view(), name='tarifaDescriptorAPIListView'))
router.add_api_view("[FRONTEND] Txt Contacto", path(r'^txtcontacto/$',
                                                   TxtContactoAPIListView.as_view(), name='TxtContactoAPIListView'))

router.add_api_view("[CAUSA] GET Causa List", path(
    r'^causa/$', CausaAPIListView.as_view(), name='causa-list'))
router.add_api_view("[CONTACTO] Contacto", path(r'^contacto/$', Contacto.as_view(), name='contacto'))

router.add_api_view("[EMPRESA]", path(
    r'^empresa/$', EmpresaAPIListView.as_view(), name='empresa-list'))
router.add_api_view("[OMV]Omv", path(r'^omv/$', OmvAPIListView.as_view(), name='omv-list'))
router.add_api_view("[OMV] Numeros Disponibles", path(r'^numeros_disponibles/$',
                                                     omvDisponibleNumbers.as_view(), name='omvDisponibleNumbers'))


# endpoints
# router.add_api_view("[CATALOGO] tarifa", path(r'^tarifa/$', TarifaView.as_view(), name='Tarifa'))
# router.register("[CATALOGO] familia", path(r'^familia/$', FamiliaViewSet, name='familia'))
router.add_api_view("[CATALOGO] paleta de colores", path(
    r'^paletacolores/$', PaletaColoresView.as_view(), name='paletacolores'))
# router.add_api_view("[CATALOGO] articulo", path(r'^articulo/$', ArticuloView.as_view(), name='articulo'))
router.add_api_view("[CATALOGO] filtros", path(r'^filtros/$', FiltrosView.as_view(), name='filtros'))
router.add_api_view("[CAUSA] POST causa", path(
    r'^newcausa/$', NewCausaAPIView.as_view(), name='newcausa'))
router.add_api_view("[PAYMENT] MAKEPAYMENT", path(
    r'^makepayment/$', MakePayment.as_view(), name='makepayment'))

router.add_api_view(
    "[SITEMAP]", path(
        r'^api/sitemap/$', SitemapView.as_view(), name='SitemapView'))

#urlpatterns = patterns(
urlpatterns = [
   
    # para traer por id
    re_path(r'^causa/(?P<id>[0-9]+)$', CausaAPIView.as_view(), name='causa'),
    # path(r'^tarifa/(?P<pk>[0-9]+)/$', TarifaDetailView.as_view()),
    re_path(r'^paletacolores/(?P<pk>[0-9]+)/$', PaletaColoresDetailView.as_view()),
    # path(r'^articulo/(?P<pk>[\w|\W]+)/$', ArticuloDetailView.as_view()),
    
    re_path(r'^facturapdf/(?P<pk>[0-9]+)/$',FormasPagoViewSet.as_view('factura_pdf'), name="facturapdf"),
    re_path(r'^contratopdf/(?P<linea>[0-9]+)/$', FormasPagoViewSet.as_view('contrato_pdf'), name="contratopdf"),
    # path(r'^admin/activar_linea/(?P<id_linea>\d+)$', 'cliente.admin_views.activar_linea', name="activar_linea"),

    re_path('', include(router.urls)), #PERE CHANGED
    re_path('', TemplateView.as_view(template_name='base.html')), #PERE CHANGED

    # Uncomment the next line to enable the admin:
    #path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api-token-auth/', obtain_jwt_token),
    re_path(r'^api-token-verify/', verify_jwt_token),
    # grappelli URLS
    #path(r'^docs/', include('rest_framework_swagger.urls')),

    re_path(r'^tinymce/', include('tinymce.urls')),
    #re_path(r'^admin/', include(admin.site.urls)), #PERE COMMENTED

    re_path(r'^admin/', admin.site.urls),
    re_path(r'pedidosdashboard/$', FormasPagoViewSet.as_view('ultimospedidosdashboard'), name="pedidosdashboard"),
    re_path(r'lineasdashboard/$', nuevaAlta.as_view(), name="lineasdashboard"), #PERE MODIFIED
    re_path(r'clientesdashboard/$', nuevaAlta.as_view(), name="clientesdashboard"), #PERE MODIFIED
    #re_path(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}), PERE COMMENTED
    re_path(r'^documentacion-omv/$', DocOmvView, name='documentacion_omv'),
    re_path(r'^documentacion-omv/test/(?P<call>\w+)/', TestDocOmvView, name='documentacionOmvTest'),


    #path(r"^payments/", include("pinax.stripe.urls")),
    # sermepa
    #path(r'^sermepa/', include('sermepa.urls')),
    # path(regex = r'^pago/',view = 'facturacion.views.form',name = 'pago'),
    # path(regex = r'^end/',view = 'facturacion.views.end',name = 'end'),
    #)
]

AdminSite.index_template = 'index.html'

if settings.DEBUG:
    import debug_toolbar
    """ urlpatterns += patterns(
        '',
        path(r'^__debug__/', include(debug_toolbar.urls)),
    )
    PERE COMMENTED """
    urlpatterns += [       
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ]