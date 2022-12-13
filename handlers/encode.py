from fastapi import HTTPException
from hashlib import sha256
from base64 import urlsafe_b64encode

from store.store import Store
from helpers.encode_helpers import exceeds_length, is_shortened_url
from helpers.generic_helpers import with_domain

MAX_SHORTENED_LENGTH = 6


def encode(url: str) -> str:
    sha256_digest = sha256(url.encode("utf8")).digest()
    return urlsafe_b64encode(sha256_digest).decode("utf8")[:MAX_SHORTENED_LENGTH]


def encode_url(long_url: str, store: Store) -> str:
    if not long_url:
        raise HTTPException(status_code=422, detail="URL must be specified")

    if exceeds_length(long_url):
        raise HTTPException(status_code=422, detail="URL is too long")

    if is_shortened_url(long_url):
        raise HTTPException(status_code=422, detail="URL is already shortened")

    short_url = encode(long_url)
    if store.get(short_url) == long_url:
        return with_domain(short_url)

    store.set(short_url, long_url)
    return with_domain(short_url)
