from fastapi.testclient import TestClient

from main import app
from helpers.encode_helpers import SHORTENER_DOMAINS, MAX_URL_LENGTH
from helpers.generic_helpers import SHORTENER_DOMAIN

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from URL shortener API"}


def test_encode_success():
    response = client.post("/encode", json={"url": "http://example.com"})
    assert response.status_code == 200
    assert response.json()["long_url"] == "http://example.com"
    assert isinstance(response.json()["short_url"], str)
    assert response.json()["short_url"].startswith(SHORTENER_DOMAIN)

def test_encode_empty_input():
    response = client.post("/encode", json={"url": ""})
    assert response.status_code == 422
    assert "URL must be specified" in str(response.content)


def test_encode_too_long_url():
    response = client.post("/encode", json={"url": "e" * (MAX_URL_LENGTH + 1)})
    assert response.status_code == 422
    assert "URL is too long" in str(response.content)


def test_encode_already_shortened_url():
    response = client.post(
        "/encode",
        json={
            "url": f"http://{SHORTENER_DOMAINS[0]}"})
    assert response.status_code == 422
    assert "URL is already shortened" in str(response.content)
