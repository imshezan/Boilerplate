""" 

https://thinkster.io/tutorials/configuring-django-settings-for-production
https://learn.microsoft.com/en-us/azure/developer/python/configure-python-web-app-local-environment#tabpanel_1_terminal-powershell
https://djangostars.com/blog/configuring-django-settings-best-practices/

https://www.gollahalli.com/blog/splitting-django-settings-for-local-and-production-development/

https://terencelucasyap.com/using-sass-django/
"""
DEBUG = False

ALLOWED_HOSTS = ['******']

# Database connection to Azure URL
DATABASES = settings.DATABASES
DATABASES['default'] = dj_database_url.parse('******', conn_max_age=500,
                                             ssl_require=True)
# For django storages
AZURE_ACCOUNT_NAME = "******"
AZURE_ACCOUNT_KEY = "******"
AZURE_CONTAINER = "******"

SHARE_URL = "******"

AZURE_BLOB_CUSTOM_DOMAIN = '******'

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = '******'
STATIC_URL = "https://%s/%s/" % (AZURE_BLOB_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = '******'
MEDIA_URL = "https://%s/%s/" % (AZURE_BLOB_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)