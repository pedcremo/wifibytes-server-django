from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render_to_response
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from catalogo.models import Tarifa, Articulo
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponse
import json
import random


class SitemapView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        prefix = '#/'
        domain = settings.URL_WEB_FRONT + prefix
        sitemap = []
        sitemap.append(domain)

        sitemap.append(domain + 'productos/smartphones')
        sitemap.append(domain + 'productos/tarjeta')
        sitemap.append(domain + 'tarifas')
        sitemap.append(domain + 'nosotros')
        sitemap.append(domain + 'login')
        sitemap.append(domain + 'cuenta')
        sitemap.append(domain + 'cuenta/pedidos')
        sitemap.append(domain + 'cuenta/tarifa')
        sitemap.append(domain + 'cuenta/ajustes')
        sitemap.append(domain + 'cuenta/facturas')

        tarifas = Tarifa.objects.filter(activo=True)
        for tarifa in tarifas:
            sitemap.append(domain + 'tarifa/' + str(tarifa.codtarifa))

        articulos = Articulo.objects.filter(activo=True)
        for articulo in articulos:
            url = str(str(domain) + str(articulo.codfamilia) + '/' + str(articulo.slug) +
                      '/' + str(articulo.referencia)).lower()
            sitemap.append(url)

        return render_to_response(
            'sitemap/sitemap.xml', {'routes': sitemap},
            content_type="text/xml; charset=utf-8"
        )


def DocOmvView(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()

    return render(request, 'admin/docOmv.html', {})


def TestDocOmvView(request, call):
    if not request.user.is_superuser:
        return HttpResponseForbidden()

    print(('[CALL] => ', call))

    response = {}

    if call == 'getPoolMsisdn':
        response = {
            'n1': random.randint(600000000, 699999999),
            'n2': random.randint(600000000, 699999999),
            'n3': random.randint(600000000, 699999999),
            'n4': random.randint(600000000, 699999999),
            'n5': random.randint(600000000, 699999999),
            'n6': random.randint(600000000, 699999999),
            'codigo_reserva': random.randint(0000000000, 9999999999)
        }

    if call == 'getPoolSIM':
        response = {
            '0': {
                'icc': random.randint(000000000000000000, 999999999999999999),
                'dc': random.randint(0, 9)
            },
            '1': {
                'icc': random.randint(000000000000000000, 999999999999999999),
                'dc': random.randint(0, 9)
            },
            '2': {
                'icc': random.randint(000000000000000000, 999999999999999999),
                'dc': random.randint(0, 9)
            },
            '3': {
                'icc': random.randint(000000000000000000, 999999999999999999),
                'dc': random.randint(0, 9)
            },
            '4': {
                'icc': random.randint(000000000000000000, 999999999999999999),
                'dc': random.randint(0, 9)
            },
            '5': {
                'icc': random.randint(000000000000000000, 999999999999999999),
                'dc': random.randint(0, 9)
            },
            '6': {
                'icc': random.randint(000000000000000000, 999999999999999999),
                'dc': random.randint(0, 9)
            },
            '7': {
                'icc': random.randint(000000000000000000, 999999999999999999),
                'dc': random.randint(0, 9)
            },
            '8': {
                'icc': random.randint(000000000000000000, 999999999999999999),
                'dc': random.randint(0, 9)
            },
            '9': {
                'icc': random.randint(000000000000000000, 999999999999999999),
                'dc': random.randint(0, 9)
            }
        }

    if "getCliente" in call:
        print('get cliente')
        response = {
            '0': {
                "cod": 146587,
                "fecha": "2017-08-14",
                "hora": "15:05:22",
                "subscriberType": 0,
                "marketingConsent": 0,
                "documentType": 0,
                "fiscalId": "25627768B",
                "nationality": None,
                "name": "VICENTE",
                "contactName": "VICENTE",
                "contactFamilyName1": "TORMO",
                "contactFamilyName2": None,
                "birthday": "1991-11-21",
                "contactDocumentType": 0,
                "contactFiscalId": None,
                "emailAddress": "test@outlook.es",
                "contactPhone": 681286611,
                "addressRegion": "Valencia",
                "addressProvince": "Valencia/Val&egrave;ncia",
                "addressCity": "albaida",
                "addressPostalCode": 46860,
                "addressStreet": "sant carlos 12",
                "addressNumber": "-",
                "shippingAddressRegion": None,
                "shippingAddressProvince": None,
                "shippingAddressCity": None,
                "shippingAddressPostalCode": None,
                "shippingAddressStreet": None,
                "shippingAddressNumber": None,
                "shippingAddressDescription": None,
                "entidad": None,
                "agencia": None,
                "dc": None,
                "cuenta": None,
                "editable": "S",
                "tratamiento": None
            },
            "1": {
                "cod": 146588,
                "fecha": "2017-09-16",
                "hora": "16:15:38",
                "subscriberType": 0,
                "marketingConsent": 0,
                "documentType": 0,
                "fiscalId": "25688768B",
                "nationality": None,
                "name": "MANUEL",
                "contactName": "MANUEL",
                "contactFamilyName1": "NAVARRO",
                "contactFamilyName2": None,
                "birthday": "1996-12-15",
                "contactDocumentType": 0,
                "contactFiscalId": None,
                "emailAddress": "test2@outlook.es",
                "contactPhone": 600323449,
                "addressRegion": "Valencia",
                "addressProvince": "Valencia/Val&egrave;ncia",
                "addressCity": "primado reig 12",
                "addressPostalCode": 46870,
                "addressStreet": "primado reig 12",
                "addressNumber": "-",
                "shippingAddressRegion": None,
                "shippingAddressProvince": None,
                "shippingAddressCity": None,
                "shippingAddressPostalCode": None,
                "shippingAddressStreet": None,
                "shippingAddressNumber": None,
                "shippingAddressDescription": None,
                "entidad": None,
                "agencia": None,
                "dc": None,
                "cuenta": None,
                "editable": "S",
                "tratamiento": None
            }
        }

    if "setAltaClienteFinal" == call:
        if random.randint(0, 10) > 5:
            response = {
                'codigo': 0o001,
            }
        else:
            response = {
                'codigo': random.randint(0o011, 0o023),
            }

    if "setAltaLineaNueva" == call:
        response = {
            'n1': random.randint(600000000, 699999999),
            'n2': random.randint(600000000, 699999999),
            'n3': random.randint(600000000, 699999999),
            'n4': random.randint(600000000, 699999999),
            'n5': random.randint(600000000, 699999999),
            'n6': random.randint(600000000, 699999999),
            'codigo_reserva': random.randint(00000, 99999)
        }
    if "setAltaLineaPortabilidad" == call:
        if random.randint(0, 10) > 5:
            response = {
                'codigo': 0o001,
            }
        else:
            response = {
                'codigo': random.randint(7, 39),
            }
    if "subirDocumento" == call:
        if random.randint(0, 10) > 5:
            response = {
                'codigo': 0o001,
            }
        else:
            response = {
                'codigo': random.randint(7, 15),
            }
    if "cancelLineasSolicitud" == call:
        if random.randint(0, 10) > 5:
            response = {
                'codigo': 0o001,
            }
        else:
            response = {
                'codigo': random.randint(7, 15),
            }

    if "setServicios" == call:
        if random.randint(0, 10) > 5:
            response = {
                'codigo': 0o001,
            }
        else:
            response = {
                'codigo': random.randint(7, 10),
            }

    if "getCDR" == call:
        if random.randint(0, 10) < 0:
            response = {
                'codigo': 0o001,
            }
        else:
            response = {
                'codigo': random.randint(7, 9),
            }

    return HttpResponse(json.dumps(response), content_type="application/json")
