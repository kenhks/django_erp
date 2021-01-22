# pylint: skip-file
from .base import *

DEBUG = True
ALLOWED_HOSTS = [
    '127.0.0.1',
]
INSTALLED_APPS = [
    'simpleui',
] + INSTALLED_APPS + [
    'debug_toolbar',
]
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

INTERNAL_IPS = [
    '127.0.0.1',
]

TMP_DIR = BASE_DIR / 'tmp'
Path.mkdir(TMP_DIR, exist_ok=True)
MEDIA_ROOT = TMP_DIR / 'media'
Path.mkdir(MEDIA_ROOT, exist_ok=True)
