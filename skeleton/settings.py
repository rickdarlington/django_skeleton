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
AUTH_USER_MODEL = 'emailauth.MyUser'
WSGI_APPLICATION = 'skeleton.wsgi.application'

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'emailauth',
    'registration',

)

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
        'DIRS': [],
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

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# TODO staticfiles handling via nginx
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "global_static"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "global_static", "templates", "layouts"),
    os.path.join(BASE_DIR, "global_static", "templates"),
)

# TODO internationalize?
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
