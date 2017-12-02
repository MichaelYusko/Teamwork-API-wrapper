import pytest

from src.teamwork.client import Teamwork


@pytest.fixture(name='client')
def init_client():
    client = Teamwork('MY_KEY', 'MY_PASS', 'MY_TEAM')
    return client
