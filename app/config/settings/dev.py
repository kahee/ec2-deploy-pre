from .base import *

secrets = json.loads(open(SECRET_DEV, 'rt').read())

DEBUG = True
ALLOWED_HOSTS = []
DATABASES = secrets['DATABASES']

WSGI_APPLICATION = 'config.wsgi.dev.application'

# Media(user-uploaded file)을 위한 스토리지
DEFAULT_FILE_STORAGE = 'config.storage.DefaultFileStorage'
# Static files(collectstatic) 을 위한 스토리지
STATICFILES_STORAGE = 'config.storage.StaticFileStorage'
