import pytest 

@pytest.mark.parametrize('path', (
    '/'
))
def test_login_required(client, path):
    response = client.get(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'
