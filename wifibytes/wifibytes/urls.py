# -*- coding: utf-8 -*-
#from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from django.urls import include, path,re_path
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView
from rest_framework import routers, viewsets, permissions
from .hybridrouter import HybridRouter #PERE commented
#from rest_framework.routers import DefaultRouter #PERE added

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

#from datos_empresa.views import DatosEmpresaViewSet
from datos_empresa.views import *
from datos_empresa.models import *

from administracion.views import SitemapView, DocOmvView, TestDocOmvView

#PERE CHANGE
from rest_framework_jwt.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


router = HybridRouter()
#router = DefaultRouter()

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
        'activar_linea/', activarLinea.as_view(), name='activarLinea'))



# Facturas
#router.add_api_view("[FACTURACION] Listado de facturas", path(r'^facturascli/$', FacturascliAPIListView.as_view(), name='facturascli-list'))
router.add_api_view("[FRONTEND] TEXTOS_CONTRATOS", path(
    'textos_contratos/', TextosContratoListView.as_view(), name='TextosContratoListView'))

router.add_api_view(
    "[SIGNATURIT] GET CONTRACTS ", path(
        'get_contracts/', getContracts.as_view(), name='getContracts'))
router.add_api_view(
    "[CLIENTE] GET ALL - POST PARAM MULTIPLEs ", path(
        'clientes/', ClienteAPIView.as_view(), name='clientes'))
router.add_api_view("[CLIENTE] GET Refresh password No Registrado", path(
    'clientenoreg/', ClienteNoRegistradoView.as_view(), name='cliente-no-registrado'))
router.add_api_view("[CLIENTE] MobilsClients", path(
    'mobilscli/', mobils_clientsAPIListView.as_view(), name='mobile-registrado'))
# router.add_api_view("[CLIENTE] DirClientes_Cliente", path(r'^dirscli/$', dirclientesAPIListView.as_view(), name='dir-registrado'))
router.add_api_view("[CLIENTE] CuentasbcoCli", path(
    'cuentascli/', cuentasbcocliAPIListView.as_view(), name='cliente-registrado'))
router.add_api_view(
    "[CLIENTE] obtenerConsumoCliente", path(
        'consumo_datos/', obtenerConsumoCliente.as_view(),
        name='obtenerConsumoCliente'))
router.add_api_view(
    "[CLIENTE] nuevaAlta", path(
        'nueva_alta/', nuevaAlta.as_view(),
        name='nuevaAlta'))

router.add_api_view(
    "[OMV] setServicios", path(
        'setServicios/', SetServiciosView.as_view(),
        name='setServicios'))


#router.add_api_view("[FACTURACION] Formas de pago", path(r'^formaspago/$', FormasPagoAPIListView.as_view(), name='formaspago-list'))
router.add_api_view("[FACTURACION] Lineas pedidos cliente", path(
    'lineaspedidoscli/', LineaspedidoscliAPIListView.as_view(), name='lineaspedidoscli-list'))
router.add_api_view("[FACTURACION] Listado de pedidos", path(
    'pedidoscli/', PedidoscliAPIListView.as_view(), name='pedidoscli-list'))
router.add_api_view("[FACTURACION] Pedidos de pago", path(
    'pedidos/', PedidoscliAPIView.as_view(), name='pedidoscli'))
router.add_api_view("[FACTURACION] Impuestos de pago", path(
    'impuestos/', ImpuestosAPIListView.as_view(), name='impuestos-list'))

# End points terminados
router.add_api_view("[FRONTEND] Home Elements ", path(
    'home/', HomeAPIListView.as_view(), name='homeAPIListView'))

# webhook github. We detect push and call this endpoint for continous integration 
router.add_api_view("[BACKEND] Capture git push",path(
   'pushFromGitRepo/',PushFromGitRepoAPI.as_view(),name='pushFromGitRepoAPI'))

router.add_api_view("[FRONTEND] Tarifa Descripción Elements", path(
    'tarifa_descriptor/', TarifaDescriptorAPIListView.as_view(), name='tarifaDescriptorAPIListView'))
router.add_api_view("[FRONTEND] Txt Contacto", path(
    'txtcontacto/',TxtContactoAPIListView.as_view(), name='TxtContactoAPIListView'))

router.add_api_view("[CAUSA] GET Causa List", path(
    'causa/', CausaAPIListView.as_view(), name='causa-list'))
router.add_api_view("[CONTACTO] Contacto", path('contacto/', Contacto.as_view(), name='contacto'))

router.add_api_view("[EMPRESA]", path(
    'empresa/', EmpresaAPIListView.as_view(), name='empresa-list'))
router.add_api_view("[OMV]Omv", path('omv/', OmvAPIListView.as_view(), name='omv-list'))
router.add_api_view("[OMV] Numeros Disponibles", path('numeros_disponibles/',
                                                     omvDisponibleNumbers.as_view(), name='omvDisponibleNumbers'))


# endpoints
# router.add_api_view("[CATALOGO] tarifa", path(r'^tarifa/$', TarifaView.as_view(), name='Tarifa'))
# router.register("[CATALOGO] familia", path(r'^familia/$', FamiliaViewSet, name='familia'))
router.add_api_view("[CATALOGO] paleta de colores", path(
    'paletacolores/', PaletaColoresView.as_view(), name='paletacolores'))
# router.add_api_view("[CATALOGO] articulo", path(r'^articulo/$', ArticuloView.as_view(), name='articulo'))
router.add_api_view("[CATALOGO] filtros", path('filtros/', FiltrosView.as_view(), name='filtros'))
router.add_api_view("[CAUSA] POST causa", path(
    'newcausa/', NewCausaAPIView.as_view(), name='newcausa'))
router.add_api_view("[PAYMENT] MAKEPAYMENT", path(
    'makepayment/', MakePayment.as_view(), name='makepayment'))

router.add_api_view(
    "[SITEMAP]", path(
        'api/sitemap/', SitemapView.as_view(), name='SitemapView')) 

#urlpatterns = patterns(
urlpatterns = [
   
    # para traer por id
    path('causa/(?P<id>[0-9]+)', CausaAPIView.as_view(), name='causa'),
    # path(r'^tarifa/(?P<pk>[0-9]+)/$', TarifaDetailView.as_view()),
    path('paletacolores/(?P<pk>[0-9]+)/', PaletaColoresDetailView.as_view()),
    # path(r'^articulo/(?P<pk>[\w|\W]+)/$', ArticuloDetailView.as_view()),
    
    path('facturapdf/(?P<pk>[0-9]+)/',FormasPagoViewSet.as_view('factura_pdf'), name="facturapdf"),
    path('contratopdf/(?P<linea>[0-9]+)/', FormasPagoViewSet.as_view('contrato_pdf'), name="contratopdf"),
    # path(r'^admin/activar_linea/(?P<id_linea>\d+)$', 'cliente.admin_views.activar_linea', name="activar_linea"),

    path('', include(router.urls)), #PERE CHANGED
    re_path(r'^$', TemplateView.as_view(template_name='base.html')), #PERE CHANGED

    # Uncomment the next line to enable the admin:
    #path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),

    # grappelli URLS
    #path(r'^docs/', include('rest_framework_swagger.urls')),

    re_path(r'^tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls), #PERE CHANGED

    re_path(r'pedidosdashboard/$', FormasPagoViewSet.as_view('ultimospedidosdashboard'), name="pedidosdashboard"),
    re_path(r'lineasdashboard/$', nuevaAlta.as_view(), name="lineasdashboard"), #PERE MODIFIED
    re_path(r'clientesdashboard/$', nuevaAlta.as_view(), name="clientesdashboard"), #PERE MODIFIED
    #re_path(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}), #PERE CHANGED
    re_path(r'^documentacion-omv/$', DocOmvView, name='documentacion_omv'),
    re_path(r'^documentacion-omv/test/(?P<call>\w+)/', TestDocOmvView, name='documentacionOmvTest'),


    #path(r"^payments/", include("pinax.stripe.urls")),
    # sermepa
    #path(r'^sermepa/', include('sermepa.urls')),
    # path(regex = r'^pago/',view = 'facturacion.views.form',name = 'pago'),
    # path(regex = r'^end/',view = 'facturacion.views.end',name = 'end'),
    #)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #PERE added

AdminSite.index_template = 'index.html'

if settings.DEBUG:
    import debug_toolbar
    """ urlpatterns += patterns(
        '',
        path(r'^__debug__/', include(debug_toolbar.urls)),
    )
    PERE COMMENTED """
    urlpatterns += [       
        path('__debug__/', include(debug_toolbar.urls)),
    ]
