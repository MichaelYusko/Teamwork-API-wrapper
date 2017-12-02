"""Utils stuff"""

from src.teamwork.utils import make_url

my_url = 'https://team.teamwork.com/action.json'


def test_make_url_functiom():
    """Test if url is correct"""
    url = make_url('team', 'action')
    assert my_url == url
