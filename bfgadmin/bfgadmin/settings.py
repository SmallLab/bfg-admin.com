"""
Django settings for bfgadmin project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jyy+2kz^y)i^%#x8m1!77bed5w^0rb+_olww8ewwf0k_h20$#$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainadmin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bfgadmin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mainadmin.mainhelpers.customcp.newsentences',
            ],
        },
    },
]

WSGI_APPLICATION = 'bfgadmin.wsgi.application'
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_DB = os.getenv('POSSTGRES_DB', 'bfgmain')
POSTGRES_PASSWORD = os.getenv('POSSTGRES_PASSWORD', '1234567')
POSTGRES_USER = os.getenv('POSSTGRES_USER', 'bfg_user')

POSTGRES_HOST_ADMIN = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_DB_ADMIN = os.getenv('POSSTGRES_DB', 'bfgmainadmin')
POSTGRES_PASSWORD_ADMIN = os.getenv('POSSTGRES_PASSWORD', '1234567')
POSTGRES_USER_ADMIN = os.getenv('POSSTGRES_USER', 'bfg_user')

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'mainbfg': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': POSTGRES_DB,
            'USER': POSTGRES_USER,
            'PASSWORD': POSTGRES_PASSWORD,
            'HOST': POSTGRES_HOST,
        },
    'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': POSTGRES_DB_ADMIN,
            'USER': POSTGRES_USER_ADMIN,
            'PASSWORD': POSTGRES_PASSWORD_ADMIN,
            'HOST': POSTGRES_HOST_ADMIN,
        },
}

DATABASE_ROUTERS = ['mainadmin.mainhelpers.routesdbmain.MainBfgRouter']
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
#For project files
STATICFILES_DIRS = ( os.path.join('static'), )
#For fire server
#STATIC_ROOT = 'bfg-admin.com/static'

REDIS_HOST = os.getenv('REDIS', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
    "redis": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://"+REDIS_HOST+":"+str(REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

MAIN_HOST_SITE = 'http://localhost:8001'
