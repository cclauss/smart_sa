# flake8: noqa
from settings_shared import *
from ccnmtlsettings.staging import common

locals().update(
    common(
        project=project,
        base=base,
        STATIC_ROOT=STATIC_ROOT,
        INSTALLED_APPS=INSTALLED_APPS,
        cloudfront="d3bl3pmxkh3k0q",
    ))

MEDIA_ROOT = '/var/www/masivukeni/uploads/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'masivukeni2',
        'HOST': '',
        'PORT': 6432,
        'USER': '',
        'PASSWORD': '',
        }
}

AWS_STORAGE_BUCKET_NAME = "ccnmtl-masivukeni-static-stage"

INTERVENTION_BACKUP_HEXKEY = "d37fb81dff7672c76f4881a8f57c002403ba2ce5155dc4ac6b68a2d9caa51d88"
INTERVENTION_BACKUP_IV = "899f6762313185a9593480e6f015b0d5053464daa5ecadd00dc4e7e2984f028f"

SENTRY_SITE = 'masivukeni-staging'
STATSD_PREFIX = 'masivukeni-staging'

try:
    from local_settings import *
except ImportError:
    pass
