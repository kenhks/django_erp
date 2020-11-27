# pylint: skip-file
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1:8000']
TMP_DIR = BASE_DIR / 'tmp'
Path.mkdir(TMP_DIR, exist_ok=True)
MEDIA_ROOT = TMP_DIR / 'media'
Path.mkdir(MEDIA_ROOT, exist_ok=True)
