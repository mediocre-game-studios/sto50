import re
from pathlib import Path
import yaml


SETTINGS = {}


def config(key, default=KeyError, cast=None):
    keys = key.split('.')

    for i, key in enumerate(keys, start=1):
        print(key)


def load_config_files(use_secrets=True):
    """Load configuration file and secrets file for backend"""
    global SETTINGS

    project_root = Path(__file__).absolute().parent.parent.parent

    try:
        with open(project_root / 'settings.yaml', 'r') as f:
            settings = yaml.load(f)
    except IOError:
        raise EnvironmentError('Could not load settings.yaml file! Aborting!')

    if use_secrets:
        try:
            with open(project_root / 'secrets.yaml', 'r') as f:
                secrets = yaml.load(f)
        except IOError:
            raise EnvironmentError('Could not load secrets.yaml file! Aborting!')

        settings.update(secrets)

    SETTINGS = settings
