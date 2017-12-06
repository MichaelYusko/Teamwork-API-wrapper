"""Utils stuff"""

from src.teamwork.utils import make_error, make_url

my_url = 'https://team.teamwork.com/action.json'
my_error = {'error': 'My error', 'code': 400}


def test_make_url_function():
    """Test if url is correct"""
    url = make_url('action', 'team')
    assert my_url == url


def test_make_error():
    """Test the make_error function"""
    error = make_error('My error', 400)
    assert my_error == error
