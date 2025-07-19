import os
from pathlib import Path
from decouple import config
import dj_database_url
import pymysql

pymysql.install_as_MySQLdb()

# ========================
# Core Django Configuration
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'union.urls'
WSGI_APPLICATION = 'union.wsgi.application'
LOGIN_URL = '/login/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

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
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'website/static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

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

# =============
# Custom User Model
# =============
AUTH_USER_MODEL = 'website.CustomUser'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'website.backends.EmailAuthBackend',
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
