# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from os.path import join, normpath

from .base import *


# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END DEBUG CONFIGURATION


# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# END EMAIL CONFIGURATION

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'altrebit',
        'USER': 'altrebitusr',
        'PASSWORD': '12345',
        # Empty for localhost through domain sockets or           '127.0.0.1'
        # for localhost through TCP.
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': '',
    #     'PORT': '',
    # }
}
# END DATABASE CONFIGURATION


# CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# END CACHE CONFIGURATION


# TOOLBAR CONFIGURATION
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

SERMEPA_URL_PRO = 'https://sis.redsys.es/sis/realizarPago'
SERMEPA_URL_TEST = 'https://sis-t.redsys.es:25443/sis/realizarPago'
SERMEPA_MERCHANT_CODE = '327234688'  # comercio de test
SERMEPA_TERMINAL = '002'
SERMEPA_SECRET_KEY = 'qwertyasdf0123456789'
SERMEPA_BUTTON_IMG = '/site_media/_img/targets.jpg'
SERMEPA_CURRENCY = '978'  # Euros

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
# END TOOLBAR CONFIGURATION

CORS_ORIGIN_ALLOW_ALL = True

PINAX_STRIPE_PUBLIC_KEY = 'pk_test_gW0J741BYjsfYWHhpg9xUGaY'
PINAX_STRIPE_SECRET_KEY = 'sk_test_e3vI9fCQ1C3HiHxqTETcteFj'

SIGNATURIT_ACCESS_TOKEN = 'fqHrSbpgSaFKvksMiujLScXLUXIpsKWdKLeguPOxsaOPSMJvmkdIBJXSLZSVIruJpnePcmDaFFzdLSdMhptBSs'

OMV_SERVER_ADDR = "optel.airenetworks.es:6547"
OMV_USER = "B98137078"
OMV_PASSWORD = "xGhbuwzPeD"

URL_WEB_FRONT = 'http://localhost:9000/'
URL_WEB_BACK = 'http://localhost:8000/'
