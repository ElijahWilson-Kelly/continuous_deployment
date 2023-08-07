import pytest

from main import app

@pytest.fixture()
def client():
    app.config.update({
        "TESTING": True,
    })
    client = app.test_client()
    return client

def test_get_home_returns_302(client):
    response = client.get("/")
    assert response.status_code == 302

def test_get_login_returns_200(client):
    response = client.get("/login")
    assert response.status_code == 200

def test_get_dashboard_returns_200(client):
    response = client.get("/dashboard")
    assert response.status_code == 200

def test_get_nonexistant_route_returns_404(client):
    response = client.get("/not-a-route")
    assert response.status_code == 404

