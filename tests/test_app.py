import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_app_is_running(client):
    response = client.get('/')
    assert response.status_code == 200