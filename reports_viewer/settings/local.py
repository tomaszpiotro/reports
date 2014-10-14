from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'tpiotrowski', # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': 'qwerty1asd',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                    # Set to empty string for default. Not used with sqlite3.
    },
    'miner': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'miner_copy', # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': 'qwerty1asd',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

STATICFILES_DIRS = (
    ('assets', '/home/sloth/studia/inz/django/reports/reports_viewer/static'),
)


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/sloth/studia/inz/django/reports/reports_viewer/templates',
    '/home/sloth/studia/inz/django/reports/lib/python2.7/site-packages/graphos/templates',

)

