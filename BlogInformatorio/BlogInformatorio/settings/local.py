from .base import *

DEBUG = True
SECRET_KEY = 'django-insecure-(ms(=v05=6x%&xvg(67(6=xih8#b3hf*pjh5jg_pj%(sp&x$ez'
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

