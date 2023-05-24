import django
import os
from pathlib import Path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xps7655r@c8u%s34t(79rs_!rdbidh(02imf&+-rh#@o=t@u0&'
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
    #installed apps
    'bootstrap5',
    'corsheaders',
    "graphene_django",
    'django_filters',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #installed middleware
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES_DIRS = os.path.join(BASE_DIR,'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIRS],
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

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# Sqlite3 database
DATABASES_DIR = str(os.path.join(BASE_DIR, "db.sqlite3_test"))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASES_DIR
    }
}
# postgresql database
# DATABASES = {
#   "default": {
#       "ENGINE": "django.db.backends.postgresql",
#       "NAME": "books",
#       "HOST": "localhost,
#       "PORT": "5432",
#       "USER": "postgres",
#       "ATOMIC_MUTATIONS": True,
#       "PASSWORD": os.getenv('POSTGRES_PASSWORD') # Your local DB password
#       }
# }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Base url to serve media files
STATIC_URL = '/static/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GRAPHENE = {
    'SCHEMA': 'backend.schema.schema',
}

# Cors headers settings
CORS_ALLOW_ALL_ORIGINS: True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]


# LOGIN_URL = 'vendor:login'
# LOGIN_REDIRECT_URL = 'vendor:vendor-admin'
# LOGOUT_REDIRECT_URL = 'core:home'

# SESSION_COOKIE_AGE = 86400 # Day in Seconds
# CART_SESSION_ID = 'cart'


# # STRIPE PAYMENT
# STRIPE_PUB_KEY = 'pk_test_OKdhbDNME5KHtnpzYRBfNmEZ00mjM6DVsJ' # For JavaScript
# STRIPE_SECRET_KEY = 'sk_test_jaIdMJOlkcUG6QpXV5wAJxXT005aZAJVM1' # For Django Backend

# # For Email Notification
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'YOUR-EMAIL'
# EMAIL_HOST_PASSWORD = 'YOUR-EMAIL-PASSWORD'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_EMAIL_FROM = 'Multi Vendor Site <YOUR-EMAIL>'