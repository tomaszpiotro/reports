from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'tpiotrowski', # Or path to database file if using sqlite3.
        'USER': 'tpiotrowski',                      # Not used with sqlite3.
        'PASSWORD': 'tpiotrowski',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                    # Set to empty string for default. Not used with sqlite3.
    },
    'miner': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'miner', # Or path to database file if using sqlite3.
        'USER': 'testuser',                      # Not used with sqlite3.
        'PASSWORD': 'test-user-pass',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}


STATICFILES_DIRS = (
    ('assets', '/home/tpiotrowski/reports/reports/static'),
)


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/tpiotrowski/reports/reports/templates',
)
