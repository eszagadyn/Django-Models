from os import path

BASE_DIR = path.dirname(path.dirname(__file__))
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
	'default': {
	'ENGINE' : 'django.db.backends.sqlite3',
	'NAME' : path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F821
	}

}

STATIC_ROOT = None
