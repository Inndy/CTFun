import importlib
from ..common import *

__all__ = []

for filename in glob(os.path.dirname(__file__) + '/*.py'):
    filename = os.path.basename(filename)
    if filename[0] == '_':
        continue
    module_name = filename[:-3]
    importlib.import_module('.' + module_name, 'ctfun.controller')
    __all__.append(module_name)
