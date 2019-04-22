import os
import dj_database_url
from backend.settings import load_config_files
from backend.settings.base import *

load_config_files(use_secrets=True)


DEBUG = False

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}
