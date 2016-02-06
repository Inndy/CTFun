from ..common import *

@route('/static/<filename:path>')
def static(filename):
    return bottle.static_file(filename, root=os.path.join(config.PATH, 'static'))
