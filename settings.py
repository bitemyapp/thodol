# Django settings for thodol project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Chris Allen', 'cma@bitemyapp.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'thodol.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

USE_L10N = False

MEDIA_ROOT = 'static'

MEDIA_URL = '/static'

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'oz4$%_v@6eyfo71co_piz*t^mtgxf7)0$5hmbth97=ssl=uth1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'thodol.urls'

TEMPLATE_DIRS = (
    'templates',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "thodol.context.notification",
    "thodol.context.site_title",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'wiki',
    #'south', # maybe later
    'django_bcrypt',
)

#SITE_TITLE = "WOOT"
SITE_TITLE = None
