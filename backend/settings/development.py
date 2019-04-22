from debug_toolbar.settings import PANELS_DEFAULTS

from backend.settings import load_config_files
from backend.settings.base import *

load_config_files(use_secrets=False)


INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


DEBUG_TOOLBAR_PANELS = PANELS_DEFAULTS + [
   'debug_toolbar.panels.profiling.ProfilingPanel',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# turn off validators in debug mode, it's easier to create simple test passwords
AUTH_PASSWORD_VALIDATORS = [
]
