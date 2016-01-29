# Notice that this file will be included by common.py,
# NEVER EVER DO `from . import common`

import json
import os
import sys

from glob import glob

# bottle.py
import bottle
from bottle import route, request, response

def view(tpl_name, **kwargs):
    if tpl_name[0] not in './':  # relative or absolute path
        tpl_name = os.path.join(os.path.dirname(__file__), 'pages', tpl_name)
    return bottle.view(tpl_name, **kwargs)

from . import config

__all__ = [
    'json', 'os', 'sys', 'glob',  # stdlib
    'grab',
    'config',
    'bottle', 'route', 'request', 'response', 'view'  # bottle.py basics
]

def grab(dict_, scope, *keys):
    """
    grab variables from a dictionary-like object to specific scope.

    >>> d = { "username": "inndy", "password": "********" }
    >>> grab(d, locals(), "username", "password")
    >>> print(username, password)  # "inndy ********"

    >>> grab(requests.forms, locals(), "username", "password")
    """
    for k in keys:
        if type(k) is str:
            scope[k] = dict_.get(k)
        elif type(k) in (list, tuple):
            grab(dict_, scope, *k)
