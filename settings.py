from decouple import config
import dj_database_url

from pathlib import Path

import pymysql

pymysql.install_as_MySQLdb()

# SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']






# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_modal_forms',
    'widget_tweaks',
    'bootstrap3',
    'django_forms_bootstrap',
    'website',
    'bookstore',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'union.urls'
LOGIN_URL = '/login/'

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

WSGI_APPLICATION = 'union.wsgi.application'




# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': config('DATABASE_ENGINE'),
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST', default='localhost'),
        'PORT': config('DATABASE_PORT', default=3306, cast=int),
    }
}


# DATABASES['default'] = dj_database_url.config(default='mysql://eunccuor_adminuser:password@localhost:3306/eunccuor_uniondb')


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

import os

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
    os.path.join(BASE_DIR, 'website/static/'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'eunccu.org'  # Use the SMTP server of your email provider
EMAIL_PORT = 465  # Common port for SSL
EMAIL_USE_TLS = False  # Use TLS for secure communication
EMAIL_USE_SSL = True  # Set to True if using SSL instead of TLS
EMAIL_HOST_USER = config('EMAIL_HOST_USER')  # Your email address
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  # Your email password
DEFAULT_FROM_EMAIL = f'Egerton University Njoro Campus Christian Union <{EMAIL_HOST_USER}>'

AUTH_USER_MODEL = 'website.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default backend
    'website.backends.EmailAuthBackend',  # Custom email authentication backend
]

# Cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 4 * 60 * 60,  # 4 hours
    }
}

# YouTube API Settings
YOUTUBE_API_KEY = config('YOUTUBE_API_KEY', default='')
YOUTUBE_PLAYLIST_ID = config('YOUTUBE_PLAYLIST_ID', default='')


SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Profile settings
PROFILE_PICTURE_MAX_SIZE = 2 * 1024 * 1024  # 2MB
ALLOWED_PROFILE_PICTURE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']

# File upload settings
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 5MB
# Session settings
SESSION_COOKIE_AGE = 600  # 10 min in seconds
SESSION_SAVE_EVERY_REQUEST = True

# Add this to allow PDF embedding
X_FRAME_OPTIONS = 'SAMEORIGIN'
