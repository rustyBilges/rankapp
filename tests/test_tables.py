import pytest 

## need to tests the following WITH user logged in also..
@pytest.mark.parametrize('path', (
    '/',
    '/table2'
))
def test_login_required(client, path):
    response = client.get(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'
    

def test_submit_table1():
    ## test that it redirects to table 2 AND 
    ##              saves table 1 data correctly 
    assert True
    
