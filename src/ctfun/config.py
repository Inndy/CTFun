import os
import sys
import json

__all__ = [ 'load', 'BASEPATH', 'PATH', 'CONFIG', 'ENV' ]

PATH = os.path.dirname(__file__)
BASEPATH = os.path.join(PATH, '..')
CONFIG_FILE = os.path.join(BASEPATH, 'config.json')
if not os.path.isfile(CONFIG_FILE):
    raise FileNotFoundError('config file not found')
CONFIG = json.load(open(CONFIG_FILE))

def load(section, scope=None, prefix=None):
    """
    load configuration and flatten from config file to current scope or
    specific scope.

    section	configuration key / section name
    scope       globals() in config module by default, suggest use `locals()` or
                `globals()` or a `dict` object
    prefix      prefix for variable / key name

    >>> config.load('smtp', globals())
    >>> SMTP_HOST  # "smtp.example.com"

    >>> config.load('env')
    >>> config.ENV  # "development"

    >>> config.load('env', globals(), 'CFG_')
    >>> CFG_ENV  # "development"
    """
    def extract(prefix, items):
        for key, value in items.items():
            expand_name = '%s%s' % (prefix, key.upper())
            if type(value) is dict:
                extract(expand_name + '_', value)
            else:
                scope[expand_name] = value

    if prefix == None:
        prefix = section.upper()
    elif prefix == False:
        prefix = ''
    else:
        prefix += section.upper()

    if not scope:
        scope = globals()

    if section not in CONFIG:
        raise KeyError('configuration `%s` not found' % section)

    data = CONFIG[section]
    data_type = type(data)
    if data_type is dict:
        extract(prefix + '_', data)
    elif data_type in (str, bool, int, float):
        scope[section] = data
    else:
        raise TypeError(
            'configuration `%s` is `%s`, don\'t know how to load' %
                (section, data_type.__name__)
        )

load('env')
