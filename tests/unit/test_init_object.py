
def test_init_obj(client):
    """Test if client was setup correctly"""
    key, password = client._credentials[0], client._credentials[1]
    assert ('MY_KEY', 'MY_PASS') == (key, password)
