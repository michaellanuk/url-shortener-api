from fastapi.testclient import TestClient

from handlers.encode import MAX_SHORTENED_LENGTH
from main import app

client = TestClient(app)


def test_decode_success():
    encode_response = client.post(
        "/", json={"url": "http://example.com"})
    short_url = encode_response.json()["short_url"]

    decode_response = client.get(f"/{short_url[-MAX_SHORTENED_LENGTH:]}")
    assert decode_response.status_code == 200


def test_decode_no_entry_found():
    response = client.get("/AAA1234")
    assert response.status_code == 404
    assert "No URL found for short URL: AAA1234" in str(response.content)
