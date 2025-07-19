<<<<<<< HEAD
import os
from pathlib import Path
=======
>>>>>>> fa15019bb9f376532ac5160a3fd8a0313134e48f
from decouple import config
import dj_database_url
import pymysql

pymysql.install_as_MySQLdb()

<<<<<<< HEAD
# ========================
# Core Django Configuration
# ========================
=======
# SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True


# Build paths inside the project like this: BASE_DIR / 'subdir'.
>>>>>>> fa15019bb9f376532ac5160a3fd8a0313134e48f
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'union.urls'
WSGI_APPLICATION = 'union.wsgi.application'
LOGIN_URL = '/login/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

<<<<<<< HEAD
# =============
# Applications
# =============
=======

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']






# Application definition

>>>>>>> fa15019bb9f376532ac5160a3fd8a0313134e48f
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party
    'bootstrap_modal_forms',
    'widget_tweaks',
    'bootstrap3',
    'django_forms_bootstrap',
    
    # Local
    'website',
    'bookstore',
    'Bstudy',
]

# =============
# Middleware
# =============
MIDDLEWARE = [
    # Security middleware
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
    # Core Django
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    # Security headers
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

<<<<<<< HEAD
# =================
# Security Settings
# =================
SECURE_HSTS_SECONDS = 31_536_000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_REFERRER_POLICY = 'same-origin'
=======
ROOT_URLCONF = 'union.urls'
LOGIN_URL = '/login/'
>>>>>>> fa15019bb9f376532ac5160a3fd8a0313134e48f

# =============
# Databases
# =============
DATABASES = {
    'default': dj_database_url.config(
        default=f"mysql://{config('DATABASE_USER')}:{config('DATABASE_PASSWORD')}@"
                f"{config('DATABASE_HOST', default='localhost')}:" 
                f"{config('DATABASE_PORT', default=3306, cast=int)}/"
                f"{config('DATABASE_NAME')}?charset=utf8mb4&init_command=SET%20NAMES%20utf8mb4"
    )
}


# =============
# Templates
# =============
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# ====================
# Password Validation
# ====================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


#Login URL
LOGIN_URL = 'website:login'
LOGIN_REDIRECT_URL = '/'

# =============
# Internationalization
# =============
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# =============
# Static & Media Files
# =============
STATIC_URL = 'static/'
STATICFILES_DIRS = [
<<<<<<< HEAD
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'website/static'),
=======
    os.path.join(BASE_DIR, 'static/'),
    os.path.join(BASE_DIR, 'website/static/'),
>>>>>>> fa15019bb9f376532ac5160a3fd8a0313134e48f
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# =============
# Email Settings
# =============
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
<<<<<<< HEAD
EMAIL_HOST = 'eunccu.org'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
=======
EMAIL_HOST = 'eunccu.org'  # Use the SMTP server of your email provider
EMAIL_PORT = 465  # Common port for SSL
EMAIL_USE_TLS = False  # Use TLS for secure communication
EMAIL_USE_SSL = True  # Set to True if using SSL instead of TLS
EMAIL_HOST_USER = config('EMAIL_HOST_USER')  # Your email address
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  # Your email password
>>>>>>> fa15019bb9f376532ac5160a3fd8a0313134e48f
DEFAULT_FROM_EMAIL = f'Egerton University Njoro Campus Christian Union <{EMAIL_HOST_USER}>'

# =============
# Custom User Model
# =============
AUTH_USER_MODEL = 'website.CustomUser'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'website.backends.EmailAuthBackend',
]

<<<<<<< HEAD
# =============
# Additional Settings
# =============
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 4 * 60 * 60,  # 4 hours
    }
}

YOUTUBE_API_KEY = config('YOUTUBE_API_KEY', default='')
YOUTUBE_PLAYLIST_ID = config('YOUTUBE_PLAYLIST_ID', default='')

# SESSIONS EXPIRATION
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# =============
# File Uploads
# =============
FILE_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024  # 50MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024  # 50MB
PROFILE_PICTURE_MAX_SIZE = 2 * 1024 * 1024  # 2MB
ALLOWED_PROFILE_PICTURE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']

# =============
# Session Settings
# =============
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 600  # 10 minutes
SESSION_SAVE_EVERY_REQUEST = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/error.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
=======
# YouTube API Settings
YOUTUBE_API_KEY = config('YOUTUBE_API_KEY', default='')
YOUTUBE_CHANNEL_ID = config('YOUTUBE_CHANNEL_ID', default='')

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Profile settings
PROFILE_PICTURE_MAX_SIZE = 2 * 1024 * 1024  # 2MB
ALLOWED_PROFILE_PICTURE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']

# File upload settings
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 5MB

# Session settings
SESSION_COOKIE_AGE = 60  # 1 in seconds
SESSION_SAVE_EVERY_REQUEST = True
>>>>>>> fa15019bb9f376532ac5160a3fd8a0313134e48f
