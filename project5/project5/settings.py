"""
Django settings for project5 project
Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2(!0rof#pqkr%q4^gjhm(rk4o)^v_tge3%u5pota_3l!0)r0y&'
=======
Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@#f-)kf8s!_xcb*k22@2d(x3zhp6kl(u9+qjp!xkt$ph9+va%+'
>>>>>>> e01526900fb7b26f31a5b9d957298f9b577a70e4

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'app5',
=======
    'app5.apps.App5Config',

>>>>>>> e01526900fb7b26f31a5b9d957298f9b577a70e4
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

ROOT_URLCONF = 'project5.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': ['templates'],
=======
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
>>>>>>> e01526900fb7b26f31a5b9d957298f9b577a70e4
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

WSGI_APPLICATION = 'project5.wsgi.application'


# Database
<<<<<<< HEAD
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
=======
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
>>>>>>> e01526900fb7b26f31a5b9d957298f9b577a70e4

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
<<<<<<< HEAD
        'NAME': BASE_DIR / 'db.sqlite3',
=======
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
>>>>>>> e01526900fb7b26f31a5b9d957298f9b577a70e4
    }
}


# Password validation
<<<<<<< HEAD
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
=======
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
>>>>>>> e01526900fb7b26f31a5b9d957298f9b577a70e4

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
<<<<<<< HEAD
# https://docs.djangoproject.com/en/3.2/topics/i18n/
=======
# https://docs.djangoproject.com/en/2.2/topics/i18n/
>>>>>>> e01526900fb7b26f31a5b9d957298f9b577a70e4

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
<<<<<<< HEAD
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
=======
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
>>>>>>> e01526900fb7b26f31a5b9d957298f9b577a70e4
