# Password hashing related
import passlib.hash

"""
privoding password hashing functions
"""

__all__ = [ 'hash_password', 'verify_password' ]

def hash(plain):
    """
    hash plain password

    :param plain: plain password to be hashed
    :return: password hash
    :rtype: str
    """
    return passlib.hash.sha256_crypt.encrypt(plain, rounds=7777, salt_size=16)

def verify(plain, hash):
    """
    verify a hashed password

    :param plain: plain password to be checked
    :param hash: password hash digest
    :return: password is matched or not
    :rtype: bool
    """
    try:
        return passlib.hash.sha256_crypt.verify(plain, hash)
    except ValueError:  # invalid hash value
        return False
    except TypeError:  # invalid type of plain/hash
        return False

def needs_update(hash):
    """
    check if the hash needs to rehash

    :param hash: password has digest
    :return: password needs to rehash or not
    :rtype: bool
    """
    return passlib.hash.sha256_crypt.needs_update(hash)
