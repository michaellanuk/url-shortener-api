from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_decode_success():
    encode_response = client.post(
        "/encode", json={"url": "http://example.com"})
    short_url = encode_response.json()["short_url"]

    decode_response = client.post("/decode", json={"url": short_url})
    assert decode_response.json()["long_url"] == "http://example.com"


def test_decode_no_entry_found():
    response = client.post("/decode", json={"url": "AAA1234"})
    assert response.status_code == 404
    assert "No URL found for short URL: AAA1234" in str(response.content)
