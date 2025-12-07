import environ
import os

from pathlib import Path
from dotenv import load_dotenv
from decouple import config
DEBUG = True
# dj_database_url is optional; DATABASES will be constructed from environment variables directly.
import pymysql

pymysql.install_as_MySQLdb()

load_dotenv()

# Fallback config() to read environment variables if python-decouple is not available.
# Usage: config('KEY', default='value', cast=bool/int/str/...)
def config(key, default=None, cast=None):
    val = os.environ.get(key, default)
    if val is None:
        return val
    if cast:
        if cast is bool:
            v = str(val).lower()
            if v in ('1', 'true', 'yes', 'on'):
                return True
            if v in ('0', 'false', 'no', 'off'):
                return False
            raise ValueError(f"Cannot cast environment variable {key!r} to bool")
        try:
            return cast(val)
        except Exception as e:
            raise ValueError(f"Cannot cast environment variable {key!r}: {e}")
    return val



# ========================
# Core Django Configuration
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
# ALLOWED_HOSTS = ['www.eunccu.org', 'https://www.eunccu.org', 'eunccu.org']
ALLOWED_HOSTS = ['*']  # For development, change in production
ROOT_URLCONF = 'union.urls'
WSGI_APPLICATION = 'union.wsgi.application'

#Login redirect URL
LOGIN_REDIRECT_URL = '/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_SITE_NAME = "Egerton University Njoro Campus Christian Union"

# =============
# Applications
# =============
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
    # 'website',
#     # 'bookstore',
    'Bstudy',
    'auth_utils.apps.AuthUtilsConfig',
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

# Security settings (development safe version)
SECURE_HSTS_SECONDS = 0  # disable HSTS for local dev
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

# Session settings
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_DOMAIN = None  # None for local
SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True

# Security headers
X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'same-origin'

# =============
# Databases
# =============
# Initialize environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': env('DATABASE_ENGINE'),
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD', default=''),
        'HOST': env('DATABASE_HOST', default='localhost'),
        'PORT': env('DATABASE_PORT', default='3306'),
    }
}





# CSP
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", "cdnjs.cloudflare.com", "ajax.googleapis.com")

# =============
# Templates
# =============
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # or your templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # ✅ needed for 'request'
                'django.contrib.auth.context_processors.auth', # ✅ needed for 'user'
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,  # Make sure DEBUG = True in development
        },
    },
]

# For development only
if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)

# ====================
# Password Validation
# ====================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


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
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # for development
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # for collectstatic in production

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# =============
# Email Settings
# =============
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'eunccu.org'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = f'Egerton University Njoro Campus Christian Union <{EMAIL_HOST_USER}>'
SUPPORT_EMAIL = EMAIL_HOST_USER

# =============
# Custom User Model
# =============
# AUTH_USER_MODEL = 'Bstudy.Member'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'Bstudy.auth_backend.MemberBackend',
]

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

# =============
# File Uploads
# =============
FILE_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024  # 50MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024  # 50MB
PROFILE_PICTURE_MAX_SIZE = 2 * 1024 * 1024  # 2MB
ALLOWED_PROFILE_PICTURE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']

import os

# Add this to your LOGGING configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/error.log'),
            'encoding': 'utf8',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Add this to create the directory automatically
if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))
