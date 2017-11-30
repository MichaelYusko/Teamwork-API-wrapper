"""Exception stuff"""

CREDENTIALS_MESSAGE = "You need provide 'username' and 'password' " \
                      "credentials see https://developer.teamwork.com/account"


class BaseError(Exception):
    """Base error class"""


class CredentialsError(BaseError):
    """Credentials error class"""
    def __str__(self):
        return CREDENTIALS_MESSAGE
