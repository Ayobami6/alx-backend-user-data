#!/usr/bin/env python3
""" Basic Auth module
"""
from .auth import Auth


class BasicAuth(Auth):
    """Basic auth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Base 64 extraction module

        Args:
            authorization_header (str): Authorization header
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
