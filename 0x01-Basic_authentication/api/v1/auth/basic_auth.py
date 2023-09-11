#!/usr/bin/env python3
"""Basic Auth module
"""
import auth
import base64
from typing import Tuple


class BasicAuth(auth.Auth):
    """Basic auth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Base 64 extraction module

        Args:
            authorization_header (str): Authorization header

        Returns:
            str: Description
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        # extract last token after space
        token = authorization_header.split(" ")[-1]
        return token

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode base64

        Args:
            base64_authorization_header (str): _description_

        Returns:
            str: _description_
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(decoded)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extract user credentials

        Args:
            decode_base64_authorization_header (str): Description
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        email = decoded_base64_authorization_header.split(':')[0]
        password = decoded_base64_authorization_header[len(email) + 1:]
        return (email, password)


a = BasicAuth()

print(a.extract_user_credentials(None))
print(a.extract_user_credentials(89))
print(a.extract_user_credentials("Holberton School"))
print(a.extract_user_credentials("Holberton:School"))
print(a.extract_user_credentials("bob@gmail.com:toto1234"))
