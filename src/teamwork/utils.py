"""Utils stuff"""


def make_url(action: str, team: str = 'authenticate') -> str:
    """ Make an url based on team and action
    :param team: Name of team
    :param action: An Teamwork action
    :return: An url based on url and action
    """
    url = f'https://{team}.teamwork.com/{action}.json'
    return url


def make_error(error: str, code: int) -> dict:
    """
    :param error: An error message
    :param code: An HTTP status code of an response
    :return: An dictionary with information
    """
    return dict(error=error, code=code)
