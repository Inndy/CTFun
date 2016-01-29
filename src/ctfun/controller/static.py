from ..common import *
from bottle import static_file

@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root=os.path.join(BASEPATH, 'static'))
