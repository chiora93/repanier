# -*- coding: utf-8 -*-
import codecs
import configparser
import logging
import os
import sys

from cmsplugin_cascade.extra_fields.config import PluginExtraFieldsConfig
from cmsplugin_cascade.utils import format_lazy
from django.urls import reverse_lazy
from django.utils.translation import get_language_info
from django.utils.translation import ugettext_lazy as _

from repanier.const import *
from .settings import *

gettext = lambda s: s
logger = logging.getLogger(__name__)


def get_allowed_mail_extension(site_name):
    try:
        component = site_name.split(".")
        if component[-1] == "local":
            allowed_mail_extension = "@repanier.be"
        else:
            allowed_mail_extension = "@{}.{}".format(component[-2], component[-1])
    except:
        allowed_mail_extension = "@repanier.be"
    return allowed_mail_extension


def get_group_name(site_name):
    try:
        return (site_name.split(".")[0]).capitalize()
    except:
        return "Repanier"


# os.path.realpath resolves symlinks and os.path.abspath doesn't.
PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))
PROJECT_PATH, DJANGO_SETTINGS_SITE_NAME = os.path.split(PROJECT_DIR)
os.sys.path.insert(0, PROJECT_PATH)
logger.info("Python path is : %s", sys.path)

config = configparser.RawConfigParser(allow_no_value=True)
conf_file_name = "{}{}{}.ini".format(
    PROJECT_DIR,
    os.sep,
    DJANGO_SETTINGS_SITE_NAME
)
try:
    # Open the file with the correct encoding
    with codecs.open(conf_file_name, 'r', encoding='utf-8') as f:
        # TODO : Use parser.read_file() instead of readfp()
        config.readfp(f)
except IOError:
    logger.exception("Unable to open %s settings", conf_file_name)
    raise SystemExit(-1)

DJANGO_SETTINGS_ADMIN_EMAIL = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_ADMIN_EMAIL')
DJANGO_SETTINGS_ADMIN_NAME = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_ADMIN_NAME')
DJANGO_SETTINGS_CACHE = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_CACHE', fallback="/var/tmp/django-cache")
DJANGO_SETTINGS_DATABASE_ENGINE = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_DATABASE_ENGINE',
                                             fallback="django.db.backends.postgresql")
DJANGO_SETTINGS_DATABASE_HOST = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_DATABASE_HOST', fallback="127.0.0.1")
DJANGO_SETTINGS_DATABASE_NAME = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_DATABASE_NAME')
DJANGO_SETTINGS_DATABASE_PASSWORD = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_DATABASE_PASSWORD')
DJANGO_SETTINGS_DATABASE_PORT = config.getint('DJANGO_SETTINGS', 'DJANGO_SETTINGS_DATABASE_PORT', fallback=5432)
DJANGO_SETTINGS_DATABASE_USER = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_DATABASE_USER')
DJANGO_SETTINGS_DEBUG = config.getboolean('DJANGO_SETTINGS', 'DJANGO_SETTINGS_DEBUG', fallback=False)
DJANGO_SETTINGS_DEBUG_TOOLBAR = config.getboolean('DJANGO_SETTINGS', 'DJANGO_SETTINGS_DEBUG_TOOLBAR', fallback=False)
DJANGO_SETTINGS_EMAIL_HOST = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_EMAIL_HOST')
DJANGO_SETTINGS_EMAIL_HOST_PASSWORD = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_EMAIL_HOST_PASSWORD')
DJANGO_SETTINGS_EMAIL_HOST_USER = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_EMAIL_HOST_USER')
DJANGO_SETTINGS_EMAIL_PORT = config.getint('DJANGO_SETTINGS', 'DJANGO_SETTINGS_EMAIL_PORT', fallback=587)
DJANGO_SETTINGS_EMAIL_USE_TLS = config.getboolean('DJANGO_SETTINGS', 'DJANGO_SETTINGS_EMAIL_USE_TLS', fallback=True)
DJANGO_SETTINGS_LANGUAGE = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_LANGUAGE', fallback="fr")
DJANGO_SETTINGS_LOGGING = config.getboolean('DJANGO_SETTINGS', 'DJANGO_SETTINGS_LOGGING',
                                            fallback=False) or DJANGO_SETTINGS_DEBUG
DJANGO_SETTINGS_SESSION = config.get('DJANGO_SETTINGS', 'DJANGO_SETTINGS_SESSION', fallback="/var/tmp/django-session")

REPANIER_SETTINGS_BOOTSTRAP_CSS = config.get('REPANIER_SETTINGS', 'REPANIER_SETTINGS_BOOTSTRAP_CSS',
                                             fallback="bootstrap.css")
REPANIER_SETTINGS_BOX = config.getboolean('REPANIER_SETTINGS', 'REPANIER_SETTINGS_BOX', fallback=False)
REPANIER_SETTINGS_CONTRACT = config.getboolean('REPANIER_SETTINGS', 'REPANIER_SETTINGS_CONTRACT', fallback=False)
REPANIER_SETTINGS_COORDINATOR_EMAIL = config.get('REPANIER_SETTINGS', 'REPANIER_SETTINGS_COORDINATOR_EMAIL',
                                                 fallback=DJANGO_SETTINGS_ADMIN_EMAIL)
REPANIER_SETTINGS_COORDINATOR_NAME = config.get('REPANIER_SETTINGS', 'REPANIER_SETTINGS_COORDINATOR_NAME',
                                                fallback=DJANGO_SETTINGS_ADMIN_NAME)
REPANIER_SETTINGS_COORDINATOR_PHONE = config.get('REPANIER_SETTINGS', 'REPANIER_SETTINGS_COORDINATOR_PHONE',
                                                 fallback="+32 499 96 64 32")
REPANIER_SETTINGS_COUNTRY = config.get('REPANIER_SETTINGS', 'REPANIER_SETTINGS_COUNTRY', fallback="be")
REPANIER_SETTINGS_BCC_ALL_EMAIL_TO = config.get('REPANIER_SETTINGS', 'REPANIER_SETTINGS_BCC_ALL_EMAIL_TO',
                                                fallback=EMPTY_STRING)
REPANIER_SETTINGS_CUSTOMER_MUST_CONFIRM_ORDER = config.getboolean('REPANIER_SETTINGS',
                                                                  'REPANIER_SETTINGS_CUSTOMER_MUST_CONFIRM_ORDER',
                                                                  fallback=False)
REPANIER_SETTINGS_CUSTOM_CUSTOMER_PRICE = config.getboolean('REPANIER_SETTINGS',
                                                            'REPANIER_SETTINGS_CUSTOM_CUSTOMER_PRICE', fallback=False)
REPANIER_SETTINGS_DELIVERY_POINT = config.getboolean('REPANIER_SETTINGS', 'REPANIER_SETTINGS_DELIVERY_POINT',
                                                     fallback=False)
REPANIER_SETTINGS_DEMO = config.getboolean('REPANIER_SETTINGS', 'REPANIER_SETTINGS_DEMO', fallback=False)
REPANIER_SETTINGS_GROUP = config.getboolean('REPANIER_SETTINGS', 'REPANIER_SETTINGS_GROUP', fallback=False)
REPANIER_SETTINGS_IS_MINIMALIST = config.getboolean('REPANIER_SETTINGS', 'REPANIER_SETTINGS_IS_MINIMALIST',
                                                    fallback=True)
REPANIER_SETTINGS_MANAGE_ACCOUNTING = config.getboolean('REPANIER_SETTINGS', 'REPANIER_SETTINGS_MANAGE_ACCOUNTING',
                                                        fallback=True)
REPANIER_SETTINGS_PRE_OPENING = config.getboolean('REPANIER_SETTINGS', 'REPANIER_SETTINGS_PRE_OPENING', fallback=False)
REPANIER_SETTINGS_PRODUCT_LABEL = config.getboolean('REPANIER_SETTINGS', 'REPANIER_SETTINGS_PRODUCT_LABEL',
                                                    fallback=False)
REPANIER_SETTINGS_PRODUCT_REFERENCE = config.getboolean('REPANIER_SETTINGS', 'REPANIER_SETTINGS_PRODUCT_REFERENCE',
                                                     fallback=False)
REPANIER_SETTINGS_ROUND_INVOICES = config.getboolean('REPANIER_SETTINGS', 'REPANIER_SETTINGS_ROUND_INVOICES',
                                                     fallback=False)

REPANIER_SETTINGS_SHOW_PRODUCER_ON_ORDER_FORM = config.getboolean('REPANIER_SETTINGS',
                                                                  'REPANIER_SETTINGS_SHOW_PRODUCER_ON_ORDER_FORM',
                                                                  fallback=True)
REPANIER_SETTINGS_STOCK = config.getboolean('REPANIER_SETTINGS', 'REPANIER_SETTINGS_STOCK', fallback=False)

DJANGO_SETTINGS_ALLOWED_HOSTS = []
for name in config.options('ALLOWED_HOSTS'):
    allowed_host = config.get('ALLOWED_HOSTS', name)
    if allowed_host.startswith("demo"):
        REPANIER_SETTINGS_DEMO = True
    DJANGO_SETTINGS_ALLOWED_HOSTS.append(allowed_host)
logger.info("Settings loaded from: %s", conf_file_name)
logger.info("Allowed hosts: %s", DJANGO_SETTINGS_ALLOWED_HOSTS)
REPANIER_SETTINGS_ALLOWED_MAIL_EXTENSION = get_allowed_mail_extension(DJANGO_SETTINGS_ALLOWED_HOSTS[0])
REPANIER_SETTINGS_GROUP_NAME = config.get('REPANIER_SETTINGS', 'REPANIER_SETTINGS_GROUP_NAME',
                                          fallback=get_group_name(DJANGO_SETTINGS_ALLOWED_HOSTS[0]))

DJANGO_SETTINGS_DATES_SEPARATOR = ","
DJANGO_SETTINGS_DAY_MONTH = "%d-%m"
DJANGO_SETTINGS_DATE = "%d-%m-%Y"
DJANGO_SETTINGS_DATETIME = "%d-%m-%Y %H:%M"

if DJANGO_SETTINGS_SITE_NAME == 'mysite':
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    STATICFILES_DIRS = (
        os.path.join(PROJECT_PATH, "collect-static"),
    )
else:
    # Activate ManifestStaticFilesStorage also when in debug mode
    STATICFILES_STORAGE = 'repanier.big_blind_static.BigBlindManifestStaticFilesStorage'

# Directory where working files, such as media and databases are kept
MEDIA_DIR = os.path.join(PROJECT_DIR, "media")
logger.debug("------- media dir : %s", MEDIA_DIR)

MEDIA_PUBLIC_DIR = os.path.join(MEDIA_DIR, "public")
logger.debug("------- media public dir : %s", MEDIA_PUBLIC_DIR)

STATIC_DIR = os.path.join(PROJECT_DIR, "collect-static")
logger.debug("------- static dir : %s", STATIC_DIR)

MEDIA_ROOT = MEDIA_PUBLIC_DIR
MEDIA_URL = "{}{}{}".format(os.sep, "media", os.sep)
STATIC_ROOT = STATIC_DIR
STATIC_URL = "{}{}{}".format(os.sep, "static", os.sep)

###################### LUT_CONFIRM
if REPANIER_SETTINGS_CUSTOMER_MUST_CONFIRM_ORDER:
    LOCK_UNICODE = "🔑"  # "✓"  # "✉"
else:
    LOCK_UNICODE = EMPTY_STRING

LUT_CONFIRM = (
    (True, LOCK_UNICODE), (False, EMPTY_STRING)
)


###################### DEBUG
DEBUG = DJANGO_SETTINGS_DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG
TEMPLATE_DEBUG = False

ADMINS = (
    (
        DJANGO_SETTINGS_ADMIN_NAME,
        DJANGO_SETTINGS_ADMIN_EMAIL
    ),
)
SERVER_EMAIL = "{}{}".format(DJANGO_SETTINGS_ADMIN_NAME, REPANIER_SETTINGS_ALLOWED_MAIL_EXTENSION)
######################

DATABASES = {
    'default': {
        'ENGINE': DJANGO_SETTINGS_DATABASE_ENGINE,
        'NAME': DJANGO_SETTINGS_DATABASE_NAME,  # Or path to database file if using sqlite3.
        'USER': DJANGO_SETTINGS_DATABASE_USER,
        'PASSWORD': DJANGO_SETTINGS_DATABASE_PASSWORD,
        'HOST': DJANGO_SETTINGS_DATABASE_HOST,
        'PORT': DJANGO_SETTINGS_DATABASE_PORT,  # Set to empty string for default.
    }
}
EMAIL_HOST = DJANGO_SETTINGS_EMAIL_HOST
EMAIL_HOST_USER = DJANGO_SETTINGS_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = DJANGO_SETTINGS_EMAIL_HOST_PASSWORD
EMAIL_PORT = DJANGO_SETTINGS_EMAIL_PORT
EMAIL_USE_TLS = DJANGO_SETTINGS_EMAIL_USE_TLS
EMAIL_USE_SSL = not DJANGO_SETTINGS_EMAIL_USE_TLS
###################### I18N

TIME_ZONE = 'Europe/Brussels'
USE_TZ = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR = '.'
NUMBER_GROUPING = 3
DECIMAL_SEPARATOR = ','

SITE_ID = 1
ALLOWED_HOSTS = DJANGO_SETTINGS_ALLOWED_HOSTS
ROOT_URLCONF = "{}.urls".format(DJANGO_SETTINGS_SITE_NAME)
WSGI_APPLICATION = "{}.wsgi.application".format(DJANGO_SETTINGS_SITE_NAME)
EMAIL_SUBJECT_PREFIX = '[' + DJANGO_SETTINGS_ALLOWED_HOSTS[0] + ']'
# DEFAULT_FROM_EMAIL Used by PASSWORD RESET
DEFAULT_FROM_EMAIL = "no-reply{}".format(REPANIER_SETTINGS_ALLOWED_MAIL_EXTENSION)

USE_X_FORWARDED_HOST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_COOKIE_HTTPONLY = True
SESSION_FILE_PATH = DJANGO_SETTINGS_SESSION

##################### Django & Django CMS
LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, "locale"),
)

INSTALLED_APPS = (
    'repanier',  # ! Important : for template precedence Repanier must be first INSTALLED_APPS after django.contrib
    'djangocms_admin_style',  # note this needs to be above the 'django.contrib.admin' entry
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    'djangocms_text_ckeditor',  # note this needs to be above the 'cms' entry
    # 'django_select2',
    'cmsplugin_filer_file',  # TODO : remove cmsplugin which is replaced by djangocms_file
    'cmsplugin_filer_folder',  # TODO : remove cmsplugin which is replaced by djangocms_file
    'cmsplugin_filer_link',  # TODO : remove cmsplugin which is replaced by djangocms_link
    'cmsplugin_filer_image',  # TODO : remove cmsplugin which is replaced by djangocms_picture
    'cmsplugin_filer_video',  # TODO : remove cmsplugin which is replaced by djangocms_video
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'cmsplugin_cascade',
    'cmsplugin_cascade.clipboard',  # optional
    'cmsplugin_cascade.extra_fields',  # optional
    'cmsplugin_cascade.icon',  # optional
    # 'cmsplugin_cascade.sharable',  # optional
    # 'cmsplugin_cascade.segmentation',  # optional
    'cms',
    # 'cms_bootstrap3',
    'menus',
    'treebeard',
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    'filer',
    'sekizai',
    'mptt',
    'django_mptt_admin',
    'reversion',
    # 'aldryn_reversion',
    'parler',
    'import_export',
    'rest_framework',
    'easy_select2',
    'djng',
    'recurrence',
)

# https://docs.djangoproject.com/fr/1.9/ref/middleware/
# http://docs.django-cms.org/en/develop/how_to/caching.html

MIDDLEWARE = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

if DJANGO_SETTINGS_DEBUG_TOOLBAR:
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    INTERNAL_IPS = ['10.0.2.2', ]
    MIDDLEWARE = (
                     'debug_toolbar.middleware.DebugToolbarMiddleware',
                 ) + MIDDLEWARE

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.csrf',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'repanier.context_processors.repanier_settings'
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    # 'django.template.loaders.eggs.Loader'
                ]),
            ],
        },
    },
]

# TODO : Investigate why jref has added this. This cause admin pblm : the checkbox appear above the description.
# FORM_RENDERER = 'djng.forms.renderers.DjangoAngularBootstrap3Templates'

CMS_PERMISSION = False  # When set to True, don't forget 'cms.middleware.user.CurrentUserMiddleware'
CMS_PUBLIC_FOR = 'all'
CMS_SHOW_START_DATE = False
CMS_SHOW_END_DATE = False
CMS_SEO_FIELDS = False
CMS_URL_OVERWRITE = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_REDIRECTS = True

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', ],
        ['TextColor', 'BGColor', 'Smiley', '-', 'PasteText'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
    'toolbar_HTMLField': [
        ['Format', 'Bold', 'Italic', 'TextColor', 'Smiley', '-', 'NumberedList', 'BulletedList', 'RemoveFormat'],
        ['Preview', 'Cut', 'Copy', 'PasteText', 'Link', '-', 'Undo', 'Redo'],
        ['Source']
    ],
    'forcePasteAsPlainText': 'true',
    # 'skin': 'moono',
    # 'format_tags'          : 'p;h4;h5;test',
    'format_tags': 'p;h2;h3;h4;h5',
    # format_test = { element : 'span', attributes : { 'class' : 'test' }, styles: { color: 'blue'}, 'name': 'Test Name' };
    'contentsCss': '{}bootstrap/css/{}'.format(STATIC_URL, REPANIER_SETTINGS_BOOTSTRAP_CSS),
    # NOTE: Some versions of CKEditor will pre-sanitize your text before
    # passing it to the web server, rendering the above settings useless.
    # To ensure this does not happen, you may need to add
    # the following parameters to CKEDITOR_SETTINGS:
    'basicEntities': False,
    'entities': False,
    'enterMode': 2,
    # Do not dispaly the HTML Path below the edit window
    'removePlugins': 'elementspath',
    # 'stylesSet' : 'my_styles:{}js/ckeditor-styles.js'.format(STATIC_URL),
    'stylesSet': format_lazy('default:{}', reverse_lazy('admin:cascade_texticon_wysiwig_config')),

}

CKEDITOR_SETTINGS_MODEL2 = {
    'language': '{{ language }}',
    'toolbar_HTMLField': [
        ['Bold', 'Italic', 'TextColor', 'Smiley', '-', 'NumberedList', 'BulletedList', 'RemoveFormat'],
        ['Preview', 'Cut', 'Copy', 'PasteText', 'Simplebox', 'Link', '-', 'Undo', 'Redo'],
        ['Source']
    ],
    # 'extraPlugins': 'simplebox',
    'forcePasteAsPlainText': 'true',
    # 'skin': 'moono',
    # 'contentsCss': '{}bootstrap/css/{}'.format(STATIC_URL, REPANIER_SETTINGS_BOOTSTRAP_CSS),
    'removeFormatTags': 'iframe,big,code,del,dfn,em,font,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,u,var',
    'basicEntities': False,
    'entities': False,
    'enterMode': 2,
    'removePlugins': 'elementspath',
}

# Drag & Drop Images
# TEXT_SAVE_IMAGE_FUNCTION = 'djangocms_text_ckeditor.picture_save.create_picture_plugin'

# djangocms-text-ckeditor uses html5lib to sanitize HTML
# to avoid security issues and to check for correct HTML code.
# Sanitisation may strip tags usesful for some use cases such as iframe;
# you may customize the tags and attributes allowed by overriding
# the TEXT_ADDITIONAL_TAGS and TEXT_ADDITIONAL_ATTRIBUTES settings:
TEXT_ADDITIONAL_TAGS = ('span', 'iframe',)
TEXT_ADDITIONAL_ATTRIBUTES = ('class', 'scrolling', 'allowfullscreen', 'frameborder')
TEXT_HTML_SANITIZE = True

FILER_ENABLE_LOGGING = False
FILER_IMAGE_USE_ICON = True
FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True
FILER_ENABLE_PERMISSIONS = False
FILER_IS_PUBLIC_DEFAULT = True
FILER_SUBJECT_LOCATION_IMAGE_DEBUG = True
FILER_DUMP_PAYLOAD = True
FILER_DEBUG = False

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROGRESSIVE = 100
THUMBNAIL_PRESERVE_EXTENSIONS = True

THUMBNAIL_OPTIMIZE_COMMAND = {
    'png': '/usr/bin/optipng {filename}',
    'gif': '/usr/bin/optipng {filename}',
    'jpeg': '/usr/bin/jpegoptim {filename}',
}
THUMBNAIL_DEBUG = FILER_DEBUG

##################### Repanier
# AUTH_USER_MODEL = 'auth.User'
AUTHENTICATION_BACKENDS = ('repanier.auth_backend.RepanierAuthBackend',)
# ADMIN_LOGIN = 'pi'
# ADMIN_PASSWORD = 'raspberry'
LOGIN_URL = "/repanier/go_repanier/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_URL = "/repanier/leave_repanier/"

##### From : django/conf/global_settings.py
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

################# Django_sass_compressor

# INSTALLED_APPS += (
#     'sass_processor',
# )

# STATICFILES_FINDERS += (
#     'sass_processor.finders.CssFinder',
# )

# SASS_PROCESSOR_AUTO_INCLUDE = False
# SASS_PRECISION = 8
# SASS_PROCESSOR_INCLUDE_DIRS = [
#     os.path.join(PROJECT_PATH, "bootstrap-sass-3.3.7", "assets", "stylesheets"),
# ]


################# Django_compressor

# INSTALLED_APPS += (
#     'compressor',
# )
#
# STATICFILES_FINDERS += (
#     'compressor.finders.CompressorFinder',
# )
#
# COMPRESS_ENABLED = True
# COMPRESS_OUTPUT_DIR = "compressor"
# COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
# COMPRESS_PARSER = "compressor.parser.HtmlParser"
# COMPRESS_OFFLINE = False

# COMPRESS_PRECOMPILERS = (
#     ('text/x-scss', 'django_libsass.SassCompiler'),
# )

##################### DJANGO REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

##################### DJANGO IMPORT EXPORT
IMPORT_EXPORT_USE_TRANSACTIONS = True

DATE_INPUT_FORMATS = (DJANGO_SETTINGS_DATE, "%d/%m/%Y", "%Y-%m-%d")
DATETIME_INPUT_FORMATS = (DJANGO_SETTINGS_DATETIME,)

##################### LOGGING
if DJANGO_SETTINGS_LOGGING:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                'format': '%(levelname)s %(name)s %(message)s',
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'console',
            },
        },
        'loggers': {
            'django.db.backends': {
                'level': 'INFO',
                'handlers': ['console'],
            },
            'repanier': {
                'level': 'DEBUG',
                'handlers': ['console'],
            },
        }
    }

####################### LANGUAGE
# if DJANGO_SETTINGS_LANGUAGE == 'fr':

LANGUAGE_CODE = 'fr'
LANGUAGES = [
    ('fr', get_language_info('fr')['name_local']),
]
CMS_LANGUAGES = {
    SITE_ID: [
        {
            'code': 'fr',
            'name': get_language_info('fr')['name'],
            'public': True,
            'hide_untranslated': False,
        },
    ]
}
PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE
PARLER_LANGUAGES = {
    SITE_ID: (
        {'code': LANGUAGE_CODE, },
    ),
    'default': {
        'fallbacks': [LANGUAGE_CODE],
        'hide_untranslated': False,
    },
}

if DJANGO_SETTINGS_LANGUAGE == 'es':

    LANGUAGE_CODE = 'es'
    LANGUAGES = [
        ('es', get_language_info('es')['name_local']),
    ]
    CMS_LANGUAGES = {
        SITE_ID: [
            {
                'code': 'es',
                'name': get_language_info('es')['name'],
                'public': True,
                'hide_untranslated': False,
            },
        ]
    }
    PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE
    PARLER_LANGUAGES = {
        SITE_ID: (
            {'code': LANGUAGE_CODE, },
        ),
        'default': {
            'fallbacks': [LANGUAGE_CODE],
            'hide_untranslated': False,
        },
    }

elif DJANGO_SETTINGS_LANGUAGE == 'fr-nl-en':

    LANGUAGE_CODE = 'fr'
    LANGUAGES = [
        ('fr', get_language_info('fr')['name_local']),
        ('nl', get_language_info('nl')['name_local']),
        ('en', get_language_info('en')['name_local']),
    ]
    CMS_LANGUAGES = {
        SITE_ID: [
            {
                'code': 'fr',
                'name': get_language_info('fr')['name'],
                'public': True,
                'redirect_on_fallback': False,
                'hide_untranslated': False,
            },
            {
                'code': 'nl',
                'name': get_language_info('nl')['name'],
                'fallbacks': ['en', 'fr'],
                'public': True,
            },
            {
                'code': 'en',
                'name': get_language_info('en')['name'],
                'fallbacks': [LANGUAGE_CODE],
                'public': True,
            },
        ]
    }
    PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE
    PARLER_LANGUAGES = {
        SITE_ID: (
            {'code': 'fr', },
            {'code': 'nl', },
            {'code': 'en', },
        ),
        'default': {
            'fallbacks': [LANGUAGE_CODE],
            'hide_untranslated': False,
        },
    }
elif DJANGO_SETTINGS_LANGUAGE == 'fr-en':

    LANGUAGE_CODE = 'fr'
    LANGUAGES = [
        ('fr', get_language_info('fr')['name_local']),
        ('en', get_language_info('en')['name_local']),
    ]
    CMS_LANGUAGES = {
        SITE_ID: [
            {
                'code': 'fr',
                'name': get_language_info('fr')['name'],
                'public': True,
                'redirect_on_fallback': False,
                'hide_untranslated': False,
            },
            {
                'code': 'en',
                'name': get_language_info('en')['name'],
                'fallbacks': [LANGUAGE_CODE],
                'public': True,
            },
        ]
    }
    PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE
    PARLER_LANGUAGES = {
        SITE_ID: (
            {'code': 'fr', },
            {'code': 'en', },
        ),
        'default': {
            'fallbacks': [LANGUAGE_CODE],
            'hide_untranslated': False,
        },
    }

DJANGO_SETTINGS_MULTIPLE_LANGUAGE = len(LANGUAGES) > 1

###################### Django : Cache setup (https://docs.djangoproject.com/en/dev/topics/cache/)

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 3600

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(DJANGO_SETTINGS_CACHE, ALLOWED_HOSTS[0]),
        'TIMEOUT': 3000,
        'OPTIONS': {
            'MAX_ENTRIES': 10000,
            'CULL_FREQUENCY': 3
        }
    }
}

##################### DJANGOCMS-CASCADE
CMSPLUGIN_CASCADE_PLUGINS = (
    # 'cmsplugin_cascade.segmentation',
    'cmsplugin_cascade.generic',
    'cmsplugin_cascade.leaflet',
    'cmsplugin_cascade.link',
    # 'cmsplugin_cascade.sharable',
    'cmsplugin_cascade.bootstrap3',

)

CMSPLUGIN_CASCADE = {
    'alien_plugins': ('TextPlugin', 'TextLinkPlugin',),
    'plugins_with_extra_fields': {
        'BootstrapRowPlugin': PluginExtraFieldsConfig(inline_styles={
            'extra_fields:Margins': ['margin-top', 'margin-bottom'],
            'extra_units:Margins': 'px,em'}),
        'BootstrapJumbotronPlugin': PluginExtraFieldsConfig(inline_styles={
            'extra_fields:Margins': ['padding-top', 'padding-bottom', 'margin-bottom'],
            'extra_units:Margins': 'px,em'}),
    },
    # 'bootstrap3'               : (
    #     ('xs', (768, 'mobile', _("mobile phones"), 750, 768)),
    #     ('sm', (768, 'tablet', _("tablets"), 750, 992)),
    #     ('md', (992, 'laptop', _("laptops"), 970, 1200)),
    #     ('lg', (1200, 'desktop', _("large desktops"), 1170, 2500)),
    # ),
    # 'segmentation_mixins'      : (
    #     (
    #         'cmsplugin_cascade.segmentation.mixins.EmulateUserModelMixin',
    #         'cmsplugin_cascade.segmentation.mixins.EmulateUserAdminMixin',
    #     ),
    # ),
    # 'plugins_with_sharables': {
    #     'BootstrapImagePlugin': ('image_shapes', 'image_width_responsive', 'image_width_fixed',
    #                              'image_height', 'resize_options',),
    #     'BootstrapPicturePlugin': ('image_shapes', 'responsive_heights', 'image_size', 'resize_options',),
    #     'BootstrapButtonPlugin': ('button_type', 'button_size', 'button_options', 'icon_font',),
    #     'TextLinkPlugin': ('link', 'target',),
    # },
    # 'exclude_hiding_plugin' : ('SegmentPlugin', 'Badge'),
    'exclude_hiding_plugin': ('Badge'),
    'allow_plugin_hiding': True,
    'leaflet': {'default_position': {'lat': 50.0, 'lng': 12.0, 'zoom': 6}},
}

CACSCADE_WORKAREA_GLOSSARY = {
    'breakpoints': ['xs', 'sm', 'md', 'lg'],
    'container_max_widths': {'xs': 750, 'sm': 750, 'md': 970, 'lg': 1170},
    'fluid': False,
    'media_queries': {
        'xs': ['(max-width: 768px)'],
        'sm': ['(min-width: 768px)', '(max-width: 992px)'],
        'md': ['(min-width: 992px)', '(max-width: 1200px)'],
        'lg': ['(min-width: 1200px)'],
    },
}

######################## CMS

CMS_CACHE_DURATIONS = {
    'content': 300,  # default 60
    'menus': 5,  # default 3600
    'permissions': 3600  # default: 3600
}

CMS_TEMPLATE_HOME = 'cms_home.html'
CMS_TEMPLATE_SUB_PAGE = 'cms_subpage.html'
CMS_TEMPLATES = (
    (CMS_TEMPLATE_SUB_PAGE, gettext("Internal page with menu on left")),
    ('cms_page.html', gettext("Internal page")),
    (CMS_TEMPLATE_HOME, gettext("Home page")),
    ('cms_bootstrap_page.html', gettext("Bootstrap page")),
    ('cms_bootstrap_subpage.html', gettext("Bootstrap page with menu on left"))
)
CMS_TEMPLATE_INHERITANCE = False

CMS_PAGE_CACHE = True
CMS_PLACEHOLDER_CACHE = True
CMS_PLUGIN_CACHE = True
CMS_TOOLBAR_ANONYMOUS_ON = False
CMS_PAGE_WIZARD_DEFAULT_TEMPLATE = CMS_TEMPLATE_SUB_PAGE
CMS_PAGE_WIZARD_CONTENT_PLACEHOLDER = 'subpage_content'

CMS_TEMPLATE_HOME_HERO = """
<h3>Lorem ipsum</h3>
<p>Lorem ipsum.</p>
<p class="text-muted"><span class="glyphicon glyphicon-pushpin"></span>&nbsp;Lorem ipsum.</p>
<h3>Lorem ipsum</h3>
<p class="text-muted">Lorem ipsum.</p>
"""

CMS_TEMPLATE_HOME_COL_1 = """
<div class="panel panel-info">
<div class="panel-heading"><h4>Lorem ipsum</h4></div>
<div class="panel-body">
<ul class="list-group">
<li class="list-group-item">Lorem ipsum.</li>
<li class="list-group-item">Lorem ipsum.</li>
</ul>
</div>
</div>
"""

CMS_TEMPLATE_HOME_COL_2 = """
<div class="panel panel-danger">
<div class="panel-heading"><h4>Lorem ipsum</h4></div>
<div class="panel-body">
<ul class="list-group">
<li class="list-group-item">Lorem ipsum.</li>
<li class="list-group-item">Lorem ipsum.</li>
</ul>
</div>
</div>
"""

CMS_TEMPLATE_HOME_COL_3 = """
<div class="panel panel-warning">
<div class="panel-heading"><h4>Lorem ipsum</h4></div>
<div class="panel-body">
<ul class="list-group">
<li class="list-group-item">Lorem ipsum.</li>
<li class="list-group-item">Lorem ipsum.</li>
</ul>
</div>
</div>
"""

CMS_TEMPLATE_FOOTER = """
Lorem ipsum dolor sit amet
"""

CMS_PLACEHOLDER_CONF = {
    'home-hero': {
        'name': gettext('Hero'),
        'plugins': [
            'TextPlugin',
        ],
        'text_only_plugins': [
            'LinkPlugin',
            'PicturePlugin',
            'FilePlugin',
            'FolderPlugin',
            'VideoPlayerPlugin'
        ],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': CMS_TEMPLATE_HOME_HERO
                },
            },
        ]
    },
    'home-col-1': {
        'name': gettext('Column 1'),
        'plugins': [
            'TextPlugin',
        ],
        'text_only_plugins': [
            'LinkPlugin',
            'PicturePlugin',
            'FilePlugin',
            'FolderPlugin',
            'VideoPlayerPlugin'
        ],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':
                        CMS_TEMPLATE_HOME_COL_1
                },
            },
        ]
    },
    'home-col-2': {
        'name': gettext('Column 2'),
        'plugins': [
            'TextPlugin',
        ],
        'text_only_plugins': [
            'LinkPlugin',
            'PicturePlugin',
            'FilePlugin',
            'FolderPlugin',
            'VideoPlayerPlugin'
        ],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':
                        CMS_TEMPLATE_HOME_COL_2
                },
            },
        ]
    },
    'home-col-3': {
        'name': gettext('Column 3'),
        'plugins': [
            'TextPlugin',
        ],
        'text_only_plugins': [
            'LinkPlugin',
            'PicturePlugin',
            'FilePlugin',
            'FolderPlugin',
            'VideoPlayerPlugin'
        ],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':
                        CMS_TEMPLATE_HOME_COL_3
                },
            },
        ]
    },
    'subpage_content': {
        'name': gettext('Content'),
        'plugins': [
            'TextPlugin',
        ],
        'text_only_plugins': [
            'LinkPlugin',
            'PicturePlugin',
            'FilePlugin',
            'FolderPlugin',
            'VideoPlayerPlugin'
        ],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':
                        """
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed luctus tortor quis imperdiet egestas. Proin mollis sem ipsum, nec facilisis nibh cursus eu. Sed convallis cursus venenatis. Maecenas rutrum, elit ut ornare lobortis, mi dolor placerat elit, at laoreet sapien urna vitae arcu. Phasellus consectetur tincidunt ullamcorper. Sed et enim at lacus cursus rhoncus. Vestibulum porttitor velit non ante ullamcorper, ut gravida ipsum vestibulum. Aenean sed condimentum nisi. Quisque sagittis mauris non leo tincidunt vulputate. Ut euismod ante purus, sed pulvinar nisl volutpat quis. Maecenas consequat mi vitae libero egestas varius. Nam in tempor augue, sit amet pulvinar purus.</p>
                        <p>Vestibulum sed elit mollis, dapibus ligula in, ultricies purus. Proin fermentum blandit ultrices. Suspendisse vitae nisi mollis, viverra ipsum vitae, adipiscing lorem. Curabitur vestibulum orci felis, nec pretium arcu elementum a. Curabitur blandit fermentum tellus at consequat. Sed eget tempor elit. Donec in elit purus.</p>
                        <p>Morbi vulputate dolor sed nibh ullamcorper, eget molestie justo adipiscing. Fusce faucibus vel quam eu ultrices. Sed aliquet fringilla tristique. Vestibulum sit amet nunc tincidunt turpis tristique ullamcorper. Nam tempor mi felis, ac vulputate quam varius eget. Nunc blandit nulla vel metus lacinia, sit amet posuere lectus viverra. Praesent vel tortor facilisis, imperdiet orci sed, auctor erat.</p>
                        """
                },
            },
        ]
    },
    'bootstrap_content': {
        'name': gettext('Bootstrap Content'),
        'plugins': ['BootstrapContainerPlugin', 'BootstrapJumbotronPlugin'],
        'parent_classes': {'BootstrapContainerPlugin': None, 'BootstrapJumbotronPlugin': None},
        'glossary': CACSCADE_WORKAREA_GLOSSARY,
        'text_only_plugins': [
            'LinkPlugin',
            'PicturePlugin',
            'FilePlugin',
            'FolderPlugin',
            'VideoPlayerPlugin'
        ],
    },

    'footer': {
        'name': gettext('Footer'),
        'plugins': ['TextPlugin'],
        'text_only_plugins': [
            'LinkPlugin',
            'PicturePlugin',
            'FilePlugin',
            'FolderPlugin',
            'VideoPlayerPlugin'
        ],
        'limits': {
            'TextPlugin': 1,
        },
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':
                        CMS_TEMPLATE_FOOTER

                },
            },
        ]
    },
}

##################### REPANIER VAT/RATE

if REPANIER_SETTINGS_COUNTRY == "ch":
    # Switzerland
    DICT_VAT_DEFAULT = VAT_325
    LUT_VAT = (
        (VAT_100, _('---------')),
        (VAT_325, _('VAT 2.5%')),
        (VAT_350, _('VAT 3.8%')),
        (VAT_430, _('VAT 8%')),
    )

    LUT_VAT_REVERSE = (
        (_('---------'), VAT_100),
        (_('VAT 2.5%'), VAT_325),
        (_('VAT 3.8%'), VAT_350),
        (_('VAT 8%'), VAT_430),
    )
elif REPANIER_SETTINGS_COUNTRY == "fr":
    # France
    DICT_VAT_DEFAULT = VAT_375
    LUT_VAT = (
        (VAT_100, _('---------')),
        (VAT_315, _('VAT 2.1%')),
        (VAT_375, _('VAT 5.5%')),
        (VAT_460, _('VAT 10%')),
        (VAT_590, _('VAT 20%')),
    )

    LUT_VAT_REVERSE = (
        (_('---------'), VAT_100),
        (_('VAT 2.1%'), VAT_315),
        (_('VAT 5.5%'), VAT_375),
        (_('VAT 10%'), VAT_460),
        (_('VAT 20%'), VAT_590),
    )
elif REPANIER_SETTINGS_COUNTRY == "es":
    # Espagne
    DICT_VAT_DEFAULT = VAT_460
    LUT_VAT = (
        (VAT_100, _('---------')),
        (VAT_360, _('VAT 4%')),
        (VAT_460, _('VAT 10%')),
        (VAT_600, _('VAT 21%')),
    )

    LUT_VAT_REVERSE = (
        (_('---------'), VAT_100),
        (_('VAT 4%'), VAT_360),
        (_('VAT 10%'), VAT_460),
        (_('VAT 21%'), VAT_600),
    )
else:
    # Belgium
    DICT_VAT_DEFAULT = VAT_400
    LUT_VAT = (
        (VAT_100, _('---------')),
        (VAT_400, _('VAT 6%')),
        (VAT_500, _('VAT 12%')),
        (VAT_600, _('VAT 21%')),
    )

    LUT_VAT_REVERSE = (
        (_('---------'), VAT_100),
        (_('VAT 6%'), VAT_400),
        (_('VAT 12%'), VAT_500),
        (_('VAT 21%'), VAT_600),
    )
