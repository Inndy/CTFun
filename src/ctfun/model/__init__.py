import importlib
from ..common import *

__all__ = []

for filename in glob(os.path.dirname(__file__) + '/*.py'):
    filename = os.path.basename(filename)
    if filename[0] == '_':
        continue
    module_name = filename[:-3]
    importlib.import_module('.' + module_name, 'ctfun.model')
    __all__.append(module_name)

DATABASE_MODELS = list(__all__)
__all__.append('create_tables')

def create_tables():
    tables = [ globals()[i] for i in DATABASE_MODELS ]
    base.get_db().create_tables(tables, safe=True)
