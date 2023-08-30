#!/usr/bin/python3
""" filter datum module """

from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """filter datum function obfuscate sensitive information
    Args:
        fields (List[str]): fields to obfuscate
        redaction (str): content to obfuscate with
        message (str): the message to obfuscate
        separator (str): line separator

    Returns:
        str: obfuscated str
    """
    for field in fields:
        pattern: str = r'({}=).*?;'.format(field)
        replace: str = r'\1{}{}'.format(redaction, separator)
        message = re.sub(pattern, replace, message)
    return message
