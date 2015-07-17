import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# TODO deployment checklist
#   https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
DEBUG = True
ALLOWED_HOSTS = []
LOGIN_URL = '/login'
SITE_ID = 1

# TODO: read secret key from filesystem:
#   https://docs.djangoproject.com/en/1.8/topics/settings/
SECRET_KEY = 'PUT SOMETHING MEANINGFUL (and secret) HERE'

# TODO: update skeleton values
ROOT_URLCONF = 'skeleton.urls'
WSGI_APPLICATION = 'skeleton.wsgi.application'

# TODO staticfiles handling via nginx
STATIC_URL = '/global_static/'

#auth
AUTH_USER_MODEL = 'emailauth.MyUser'

AUTHENTICATION_METHOD = 'email'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "required"
ACCOUNT_PASSWORD_MIN_LENGTH = 4

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

THIRD_PARTY_APPS = (
    'bootstrap3',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
)

LOCAL_APPS = (
    'emailauth',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# If you are running Django 1.8+, specify the context processors
# as follows:
#TEMPLATE_CONTEXT_PROCESSORS = (
#    "django.core.context_processors.request",
#    "allauth.account.context_processors.account",
#    "allauth.socialaccount.context_processors.socialaccount",
#)

# If you are running Django 1.8+, specify the context processors
# as follows:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates", "layouts"), 
                 os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Already defined Django-related contexts here
                'django.template.context_processors.debug',
                'django.contrib.messages.context_processors.messages',
                
                # `allauth` needs this from django
                'django.template.context_processors.request',

                # `allauth` specific context processors
                'allauth.account.context_processors.account',
                'django.contrib.auth.context_processors.auth',
                'allauth.socialaccount.context_processors.socialaccount',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        },
        #TODO update logger name
        'SKELETON': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

#TODO production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "global_static"),
)

#TODO production email settings
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, "tempemail")
    DEFAULT_FROM_EMAIL = 'password@SITENAME'
#    EMAIL_HOST = 'localhost'
#    EMAIL_PORT = 1025
#    EMAIL_HOST_USER = ''
#    EMAIL_HOST_PASSWORD = ''
#    EMAIL_USE_TLS = False
#    DEFAULT_FROM_EMAIL = 'test@email.com'


# TODO internationalize?
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True