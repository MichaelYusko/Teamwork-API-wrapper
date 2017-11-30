import pytest

from src.teamwork.client import Teamwork
from src.teamwork.exceptions import CREDENTIALS_MESSAGE, CredentialsError


def test_credential_raises():
    """Test for credentials, if not provided raise the Error"""
    with pytest.raises(CredentialsError) as error:
        Teamwork()
    assert str(error.value) == CREDENTIALS_MESSAGE
