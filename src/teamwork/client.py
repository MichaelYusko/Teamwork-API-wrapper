"""Client stuff"""

from requests import Session

from .constants import BASE_URL
from .exceptions import CredentialsError  # pylint: disable=import-error
from .utils import make_error, make_url


class BaseTeamwork:  # pylint: disable=too-few-public-methods
    """Base Teamwork class that includes the most used methods"""
    def __init__(self, username, password, team):
        if not username or not password:
            raise CredentialsError

        self._credentials = (username, password)
        self.session = Session()
        self._auth()
        self._team = team

    def _auth(self):
        """Auth via Basic authentication"""
        self.session.auth = self._credentials
        self.session.get(BASE_URL)

    def _get(self, url, **kwargs):
        """ Custom get method
        :param url: An endpoint, which we need to call.
        :param kwargs: Another keys
        :return: An dictionary object
        """
        response = self.session.get(url, **kwargs)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code


class Auth(BaseTeamwork):  # pylint: disable=too-few-public-methods
    """Authentication stuff"""

    def __init__(self, username, password, team):  # pylint: disable=useless-super-delegation
        super().__init__(username, password, team)

    @property
    def my_account(self):
        """ Get own account details
        :return: An dictionary with information
        """
        return self._get(BASE_URL)

    @property
    def admin_account(self):
        """
        :return: An dictionary with Administrator information
                 If an user doesn't have permission
                 Just return the dictionary with error and code.
        """
        url = make_url('account')
        response = self._get(url)

        if response == 401:
            response = make_error('User must be an Administrator', 401)
        return response


class Project(BaseTeamwork):
    """Project stuff"""
    def __init__(self, username, password, team):
        super().__init__(username, password, team)

    _action = 'projects'

    def all(self):
        """
        :return: Retrieves all accessible projects. Default returns your active projects.
        """
        url = make_url(self._action, self._team)
        return self._get(url)


class Activity(BaseTeamwork):
    def __init__(self, username, password, team):
        super().__init__(username, password, team)

    _action = 'latestActivity'

    def last(self, max_items=60, only_stared=False):
        """Lists the latest activity across all projects ordered chronologically
        :param max_items: Count of items
        :param only_stared: Return stared projects
        :return: an array with objects
        """
        url = make_url(self._action, self._team)
        params = {'maxItems': max_items, 'onlyStarred': only_stared}

        response = self._get(url, params=params)
        all_projects = response['activity']
        return all_projects


class Teamwork(BaseTeamwork):  # pylint: disable=too-few-public-methods
    """Main class"""
    def __init__(self, username=None, password=None, team=None):
        super().__init__(username, password, team)
        self.auth = Auth(username, password, team)
        self.activity = Activity(username, password, team)
        self.projects = Project(username, password, team)
