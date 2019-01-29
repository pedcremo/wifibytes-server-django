# -*- coding: utf-8 -*-


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
        'NAME': 'wifibytes',
        #'USER': 'postgressql',
        'USER': 'wifibytes',
        'PASSWORD': 'sQX-Ve2-F3',
        #'HOST': 'postrgessql-db-instance.cedx16kwp0io.eu-west-2.rds.amazonaws.com',
        'HOST': 'wifibytes.cedx16kwp0io.eu-west-2.rds.amazonaws.com',        
        'PORT': '5432',                      # Set to empty string for default.
    }
}

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

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False


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

URL_WEB_FRONT = 'https://nueva.wifibytes.com/'
URL_WEB_BACK = 'https://backend.wifibytes.com/'
