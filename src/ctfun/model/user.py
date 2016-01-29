from ..utils import password
from ._base import *

__all__ = [ 'User' ]

class User(BaseModel):
    username = TextField()
    password = CharField(255)
    email = CharField(255)

    def check_password(self, plain, check_update=True):
        ret = password.verify(plain, self.password)
        if ret and check_update and password.needs_update(self.password):
            self.password = password.hash(plain)
            self.save()
        return ret
