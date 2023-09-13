#!/usr/bin/env python3
""" Auth Module
"""


from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register User

        Args:
            email (str): user's email
            password (str): user's password

        Returns:
            User: registered user

        Raises:
            ValueError: if User exists
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """Check if password is correct to validate login

        Args:
            email (str): User email
            password (str): User password
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        password = password.encode('utf-8')
        if checkpw(password, user.hashed_password):
            return True
        return False


def _hash_password(password: str) -> bytes:
    """ Hash Pasword

    Args:
        password (str): password to be hashed

    Returns:
        bytes: hashed result
    """
    passwd = password.encode('utf-8')
    return hashpw(passwd, gensalt())
