# Password hashing related
import passlib.hash

"""
privoding password hashing functions
"""

__all__ = [ 'hash_password', 'verify_password' ]

def hash(plain):
    return passlib.hash.sha256_crypt.encrypt(plain, rounds=7777, salt_size=16)

def verify(plain, hash):
    return passlib.hash.sha256_crypt.verify(plain, hash)

def needs_update(hash):
    return passlib.hash.sha256_crypt.needs_update(hash)
