# -*- coding: utf-8 -*-

from os.path import abspath, basename, dirname, join, normpath
from sys import path
import datetime
#from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP


# PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
# END PATH CONFIGURATION


# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END DEBUG CONFIGURATION


# MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Your Name', 'your_email@example.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# END MANAGER CONFIGURATION


# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
# END DATABASE CONFIGURATION


# GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Europe/Madrid'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'es-es'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# END GENERAL CONFIGURATION


# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url

MEDIA_URL = 'media/'

# END MEDIA CONFIGURATION


# STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See:
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# See:
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# END STATIC FILE CONFIGURATION


# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = 'j7@l1$$#ycid@@7-len0j$sma*e7q$rr7ysg)5p$7oi0abg4*z'
# END SECRET CONFIGURATION


# SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
# END SITE CONFIGURATION


# FIXTURE CONFIGURATION

# See:
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS

FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
# END FIXTURE CONFIGURATION


# TEMPLATE CONFIGURATION

# See:
# https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
 
#PERE ADDED
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': normpath(join(SITE_ROOT, 'templates')),
        'DIRS': [
            'templates',
            'static'
        ],
        #'APP_DIRS': True,
        'OPTIONS': {
            # ... some options here ...
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'loaders':[
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

""" PERE COMMENTED TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)
 """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
""" PERE COMMENTED TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
) """

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
"""PERE COMMENTED TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
) """

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Altrebit Backend',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': False,  # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        {'app': 'cliente', 'icon': 'icon-user',
            'models': ('cliente', 'mobilsclients', 'servicio')},
        {'app': 'catalogo', 'icon': 'icon-book',
            'models': ('familia', 'articulo', 'tarifa')},
        {'app': 'facturacion', 'icon': 'icon-leaf', 'models': ('facturasCli')},
        {'label': 'Causas', 'icon': 'icon-thumbs-up', 'url': '/admin/causa/causa/'},
        {'label': 'Pedidos', 'icon': 'icon-shopping-cart',
            'url': '/admin/facturacion/pedidocli/'},
        {'label': 'Contenidos', 'icon': 'icon-pencil', 'models': (
            {'label': 'Textos Home', 'url': '/admin/pagina/home/'},
            {'label': 'Textos cajitas tarifas',
             'url': '/admin/pagina/tarifadescriptorgenerico/'},
            {'label': 'Textos contacto', 'url': '/admin/pagina/txtcontacto/1/'}
        )},
        {'app': 'geo', 'icon': 'icon-globe'},
        {'label': 'Configuración', 'icon': 'icon-cog', 'models': (
            {'model': 'facturacion.formaspago', 'label': 'Métodos de pago'},
            {'model': 'facturacion.formasenvio', 'label': 'Métodos de envío'},
            {'model': 'auth.user', 'label': 'Usuarios'})
         },
        {'label': 'Empresas', 'icon': 'icon-briefcase', 'models': (
            {'label': 'Datos Empresa', 'url': '/admin/datos_empresa/datosempresa/'},
        )},
        {'label': 'Textos Contrato', 'icon': 'icon-info-sign', 'models': (
            {'label': 'Textos', 'url': '/admin/datos_empresa/textoscontrato/'},
        )},
        {'label': 'Rangos ICC', 'icon': 'icon-info-sign', 'models': (
            {'label': 'Rangos ICC', 'url': '/admin/icc/rangoicc/'},
        )},
        {'label': 'Documentación OMV', 'icon': 'icon-info-sign', 'models': (
            {'label': 'Documentación', 'url': '/documentacion-omv/'},
        )},
    ),

    # misc
    'LIST_PER_PAGE': 15
}
# END TEMPLATE CONFIGURATION


# MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE = (
    # Default Django middleware.    
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# END MIDDLEWARE CONFIGURATION


# URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
# END URL CONFIGURATION


# APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'suit',
    'tinymce',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_jwt',
    # 'rest_framework_swagger',


    # Admin panel and documentation:
    'django.contrib.admin',
    'pinax.stripe'
    # 'django.contrib.admindocs',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'cliente',
    'catalogo',
    'empresa',
    'omv',
    'facturacion',
    'causa',
    'pagina',
    'geo',
    'internationalization',
    'datos_empresa',
    'icc'
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
# END APP CONFIGURATION


# LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# END LOGGING CONFIGURATION


# WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME
# END WSGI CONFIGURATION

# PIPELINE CONFIGURATION
INSTALLED_APPS += (
    'pipeline',
)

PIPELINE = {
    'PIPELINE_ENABLED': True,
    'STYLESHEETS': {
        'project_name': {
            'source_filenames': (
              'css/project_name.less',              
            ),
            'output_filename': 'css/project_name.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
    'JAVASCRIPT': {
        'vendor': {
            'source_filenames': (
              'vendor/bootstrap/dist/js/bootstrap.js',              
            ),
            'output_filename': 'js/vendor.js',
        }
        ,
        'project_name': {
            'source_filenames': (
                'js/*.coffee',
            ),
            'output_filename': 'js/project_name.js'
        }
    }
}

#OLD PIPELINE


PIPELINE['COMPILERS'] = (
    'pipeline.compilers.less.LessCompiler',
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
)

""" PERE COMMENT PIPELINE_CSS = {
    'project_name': {
        'source_filenames': (
            'css/project_name.less',
        ),
        'output_filename': 'css/project_name.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    }
}

PIPELINE_JS = {
    'vendor': {
        'source_filenames': (
            'vendor/bootstrap/dist/js/bootstrap.js',
        ),
        'output_filename': 'js/vendor.js',
    },
    'project_name': {
        'source_filenames': (
            'js/*.coffee',
        ),
        'output_filename': 'js/project_name.js'
    }
} """

PIPELINE['LESS_ARGUMENTS'] = '-x --yui-compress'

PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'

#PIPELINE_YUGLIFY_JS_ARGUMENTS = '--terminal'

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
# END PIPELINE CONFIGURATION

# TEST CONFIGURATION
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
# END TEST CONFIGURATION


# REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}
# END REST_FRAMEWORK

# django-rest-framework-jwt
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=60),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=60)
}
#########

GITHUB_WEBHOOK_KEY = 'XljuIcI5iBttpPebui'