from .common import *
from . import controller  # load routes

__all__ = [ 'start' ]

def start(host='127.0.0.1', port=7122, server='gevent'):
    """
    start service

    host    ip address to bind
    port    port number to listen
    server  which backend to use, ex: 'gunicorn', 'gevent', 'cherrypy'
    """
    bottle.debug('DEBUG' in os.environ)
    if server == 'gevent':
        from gevent import monkey; monkey.patch_all()
    bottle.run(server=server, host=host, port=port)
