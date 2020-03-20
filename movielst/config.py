from pathlib import Path
import configparser
import os

APP_NAME = 'movielst'

XDG_CACHE_HOME = Path(os.environ.get('XDG_CACHE_HOME') or '~/.cache').expanduser()
XDG_CONFIG_HOME = Path(os.environ.get('XDG_CONFIG_HOME') or '~/.config').expanduser()
XDG_DATA_HOME = Path(os.environ.get('XDG_DATA_HOME') or '~/.local/share').expanduser()

# Support legacy locations.
LEGACY_PATH = Path('~/.movielst').expanduser()
if LEGACY_PATH.is_dir():
    CACHE_DIR = CONFIG_DIR = DATA_DIR = LEGACY_PATH
else:
    CACHE_DIR = XDG_CACHE_HOME / APP_NAME
    CONFIG_DIR = XDG_CONFIG_HOME / APP_NAME
    DATA_DIR = XDG_DATA_HOME / APP_NAME

CONFIG_PATH = CONFIG_DIR / 'config.ini'


def create_config():
    for path in CACHE_DIR, CONFIG_DIR, DATA_DIR:
        try:
            path.mkdir(parents=True)
        except FileExistsError:
            pass

    if not CONFIG_PATH.exists():
        config = configparser.ConfigParser()

        config.add_section('General')
        config.add_section('Index')
        config.add_section('API')
        config.add_section('Web')

        config.set('General', 'log_level', 'INFO')
        config.set('General', 'log_location', str(CACHE_DIR) + '/')
        config.set('Index', 'location', str(DATA_DIR) + '/')
        config.set('Index', 'min_size_to_index', '25')
        config.set('API', 'use_external_api', 'omdb')
        config.set('API', 'OMDb_API_key', '37835d63')
        config.set('API', 'TMdb_API_key', '')
        config.set('Web', 'host', 'localhost')
        config.set('Web', 'port', '5000')
        config.set('Web', 'require_login', "False")

        with CONFIG_PATH.open('w') as config_file:
            config.write(config_file)


def get_config():
    config = configparser.ConfigParser()
    config.read(str(CONFIG_PATH))
    return config


def get_setting(section, setting, fallback=None):
    config = get_config()
    return config.get(section, setting, fallback=fallback)


def update_config(section, setting, value):
    config = get_config()
    config.set(section, setting, value)
    with CONFIG_PATH.open('w') as config_file:
        config.write(config_file)
