#!/usr/bin/env python3
""" Auth Module
"""

from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """ Hash Pasword

    Args:
        password (str): password to be hashed

    Returns:
        bytes: hashed result
    """
    passwd = password.encode('utf-8')
    return hashpw(passwd, gensalt())
