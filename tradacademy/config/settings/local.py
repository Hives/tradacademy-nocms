from .common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '85^gxcjoq*a*ac6tgv9pctm@n^^-_0*+$p9cm(b-jyqlh=@tnj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tradacademy_nocms',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Media files (user uploads)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

MEDIA_ROOT = BASE_DIR.child("media")
MEDIA_URL = '/media/'

THUMBNAIL_DEBUG = True