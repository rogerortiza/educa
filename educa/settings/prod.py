from .base import *

DEBUG = False

ADMINS = (
    ('Roger Ortiz', 'rogerortiz4@gmail.com'),
)

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'educa',
       'USER': 'educa_user',
       'PASSWORD': 'educa123'
   }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
