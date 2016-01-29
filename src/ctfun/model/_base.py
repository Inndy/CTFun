from ..common import *
config.load('database', globals())

import peewee
from peewee import *

__all__ = [ 'BaseModel' ]
__all__.extend(peewee.__all__)

_db = None

def get_db():
    """
    return peewee.Database connection object
    """
    global _db
    if _db: return _db

    if DATABASE_TYPE == 'sqlite':
        return SqliteDatabase(os.path.join(config.BASEPATH, DATABASE_PATH))
    elif DATABASE_TYPE == 'mysql':
        return MySQLDatabase(DATABASE_CONNECT_STRING)
    else:
        raise NotImplementedError('Not supported database `%s`' % DATABASE_TYPE)

class BaseModel(Model):
    class Meta: db = get_db()
