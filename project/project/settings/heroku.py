"""
Production Settings for Heroku
"""

import environ
import os
# If using in your own project, update the project namespace below
from project.settings.base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')

# False if not in os.environ
DEBUG = env('DEBUG')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}
