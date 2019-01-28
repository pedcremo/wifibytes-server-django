# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from os import environ

from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


# HOST CONFIGURATION
# See:
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = []
# END HOST CONFIGURATION

# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
# END EMAIL CONFIGURATION

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wifibyteDB',
        'USER': 'wifibytesuser',
        'PASSWORD': 'n0j$sma*e7q$rr7ysg)',
        # Empty for localhost through domain sockets or           '127.0.0.1'
        # for localhost through TCP.
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}

# END DATABASE CONFIGURATION

PINAX_STRIPE_PUBLIC_KEY = 'pk_test_gW0J741BYjsfYWHhpg9xUGaY'
PINAX_STRIPE_SECRET_KEY = 'sk_test_e3vI9fCQ1C3HiHxqTETcteFj'

SIGNATURIT_ACCESS_TOKEN = 'fqHrSbpgSaFKvksMiujLScXLUXIpsKWdKLeguPOxsaOPSMJvmkdIBJXSLZSVIruJpnePcmDaFFzdLSd'

# ########## CACHE CONFIGURATION
# # See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {}
# ########## END CACHE CONFIGURATION

OMV_SERVER_ADDR = "optel.airenetworks.es:6547"
OMV_USER = "B98137078"
OMV_PASSWORD = "xGhbuwzPeD"

URL_WEB_FRONT = 'http://wifibytes-front.wearecactus.com/'
URL_WEB_BACK = 'http://wifibytes.wearecactus.com/'
