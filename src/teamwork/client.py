"""Client stuff"""

from .exceptions import CredentialsError  # pylint: disable=import-error


class BaseTeamwork:  # pylint: disable=too-few-public-methods
    """Base Teamwork class that includes the most used methods"""
    def __init__(self, username, password):
        if not username or not password:
            raise CredentialsError

        self._credentials = (username, password)


class Teamwork(BaseTeamwork):  # pylint: disable=too-few-public-methods
    """Main class"""
    def __init__(self, username=None, password=None):  # pylint: disable=useless-super-delegation
        super().__init__(username, password)
