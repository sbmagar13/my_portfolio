"""
Django settings for personal project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url

import cloudinary
import cloudinary_storage

from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIAFILES_DIRS = (os.path.join(BASE_DIR, "media"),)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'f^v0$q1l)3e*36&f$ctpu_lki)ou2v(54d&ir3d3ac3^yfq0r9'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'f^v0$q1l)3e*36&f$ctpu_lki)ou2v(54d&ir3d3ac3^yfq0r9')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True


DEBUG = int(os.environ.get("DEBUG", default=1))

# ALLOWED_HOSTS = ['https://sbmagar.herokuapp.com/', '127.0.0.1', 'localhost']
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(' ')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'portfolio',
    'psycopg2',
    'blogs',
    'works',
    'experiences',
    'django_summernote',
    'cloudinary',
    'cloudinary_storage',
    'taggit',
    'django.contrib.sitemaps',
    'mdeditor',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'personal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'experiences.context_processors.experience_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'personal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        'NAME': os.environ.get("POSTGRES_DB", os.path.join(BASE_DIR, "db.sqlite3")),
        'USER': os.environ.get("POSTGRES_USER", "sagar"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", "password"),
        'HOST': os.environ.get("POSTGRES_HOST", "localhost"),
        # 'HOST': os.environ.get("localhost"),
        'PORT': os.environ.get("POSTGRES_PORT", "5432"),

    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# Cloudinary stuff
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUD_NAME', default=""),
    'API_KEY': config('API_KEY', default=""),
    'API_SECRET': config('API_SECRET', default=""),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# STATIC_ROOT = '/vol/web/static'

# Location of static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = '/vol/web/media'

# Activate Django-Heroku.
django_heroku.settings(locals())

# prod_db = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)

X_FRAME_OPTIONS = 'SAMEORIGIN'
SUMMERNOTE_THEME = 'bs4'
