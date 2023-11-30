import pytest
from web_app import app

# creates a Flask test client (app.test_client())
# that can be used to simulate HTTP requests and
# interact with your Flask application during testing.
@pytest.fixture
def client():
    return app.test_client()


def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_index_page(client):
    response = client.get('/search')
    assert response.status_code == 200

def test_index_page(client):
    response = client.get('/search/results/<query>')
    assert response.status_code == 200
