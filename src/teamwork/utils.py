"""Utils stuff"""


def make_url(team: str, action: str) -> str:
    """ Make an url based on team and action
    :param team: Name of team
    :param action: An Teamwork action
    :return: An url based on url and action
    """
    url = f'https://{team}.teamwork.com/{action}'
    return url
