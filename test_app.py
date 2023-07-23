import pytest

from app import app

@pytest.fixture()
def client():
    app.config.update({
        "TESTING": True,
    })
    print("Testing")
    client = app.test_client()
    yield client

    print("All done")

def test_get_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

