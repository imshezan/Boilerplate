DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    ...
}

SHARE_URL = "http://127.0.0.1:8000"

# Static assets
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static_dirs'),
)

# User uploads
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')