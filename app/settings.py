"""
Django settings for app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DEVELOPMENT = False
STAGING = False
if 'DEV_ENV' in os.environ:
    if os.environ['DEV_ENV'] == 'heroku':
        STAGING = True
        ENVIRONMENT = 'staging'
else:
    DEVELOPMENT = True
    ENVIRONMENT = 'dev'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bn-20yak-8uz==*oeg=4c+ciw#ufrwhaev8j$t6@hb(j$)b+_='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'core'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'


# Custom User Class
AUTH_USER_MODEL = 'core.AppUser'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if DEVELOPMENT:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'news',                      
            'USER': 'admin',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': 5432
        }
    }
elif STAGING:
    import dj_database_url
    # This automatically retrieves the Heroku PostgreSQL URL!?
    DATABASES = {}
    DATABASES['default'] =  dj_database_url.config()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Templates
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates')
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
