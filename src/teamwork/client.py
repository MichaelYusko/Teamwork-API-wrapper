"""Client stuff"""

from requests import Session

from .constants import AUTHENTICATE_URL
from .exceptions import CredentialsError  # pylint: disable=import-error


class BaseTeamwork:  # pylint: disable=too-few-public-methods
    """Base Teamwork class that includes the most used methods"""
    def __init__(self, username, password):
        if not username or not password:
            raise CredentialsError

        self._credentials = (username, password)
        self.session = Session()
        self._auth()

    def _auth(self):
        """Auth via Basic authentication"""
        self.session.auth = self._credentials
        self.session.get(AUTHENTICATE_URL)

    def _get(self, url, **kwargs):
        """ Custom get method
        :param url: An endpoint, which we need to call.
        :param kwargs: Another keys
        :return: An dictionary object
        """
        return self.session.get(url, **kwargs).json()


class Auth(BaseTeamwork):  # pylint: disable=too-few-public-methods
    """Authentication stuff"""

    def __init__(self, username, password):  # pylint: disable=useless-super-delegation
        super().__init__(username, password)

    @property
    def my_account(self):
        """ Get own account details
        :return: An dictionary with information
        """
        return self._get(AUTHENTICATE_URL)


class Teamwork(BaseTeamwork):  # pylint: disable=too-few-public-methods
    """Main class"""
    def __init__(self, username=None, password=None):  # pylint: disable=useless-super-delegation
        super().__init__(username, password)
        self.auth = Auth(username, password)
