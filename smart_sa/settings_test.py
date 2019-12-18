# flake8: noqa
from smart_sa.settings_shared import *
import os


DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'lettuce.db',
        'OPTIONS': {
            'timeout': 30
        }
    }
}

HEADLESS = True
BROWSER = 'Firefox'
# BROWSER = 'Chrome'


ALOE_DJANGO_APP = ['aloe_django']
INSTALLED_APPS = INSTALLED_APPS + ALOE_DJANGO_APP

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

MIDDLEWARE.remove(
    'django_statsd.middleware.GraphiteRequestTimingMiddleware')
MIDDLEWARE.remove(
    'django_statsd.middleware.GraphiteMiddleware')
MIDDLEWARE.remove(
    'impersonate.middleware.ImpersonateMiddleware')

SESSION_COOKIE_SECURE = False

ALLOWED_HOSTS.append('127.0.0.1')


# Running tests
# python manage.py --settings=settings_test harvest

if os.environ.get('SELENIUM_BROWSER', False):
    # it's handy to be able to set this from an
    # environment variable
    BROWSER = os.environ.get('SELENIUM_BROWSER')
