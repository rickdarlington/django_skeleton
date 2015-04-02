import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# TODO deployment checklist
#   https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
DEBUG = True
ALLOWED_HOSTS = []
LOGIN_URL = '/login'

# TODO: read secret key from filesystem:
#   https://docs.djangoproject.com/en/1.8/topics/settings/
SECRET_KEY = '8bg^v)1t%e6&#74hn)yu(1i7v=kjyh((20s*xem1-6y_&-hr*h'

# TODO: update skeleton values
ROOT_URLCONF = 'skeleton.urls'
WSGI_APPLICATION = 'skeleton.wsgi.application'

# TODO staticfiles handling via nginx
STATIC_URL = '/global_static/'

#TODO usernameless user model
AUTH_USER_MODEL = 'emailauth.MyUser'

REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/' 


DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'bootstrap3',
    'registration',
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "global_static", "templates", "layouts"), 
                 os.path.join(BASE_DIR, "global_static", "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

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

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "global_static", "templates", "layouts"),
    os.path.join(BASE_DIR, "global_static", "templates"),
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