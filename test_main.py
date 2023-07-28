import pytest

from main import app

@pytest.fixture()
def client():
    app.config.update({
        "TESTING": True,
    })
    client = app.test_client()
    return client

def test_get_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

