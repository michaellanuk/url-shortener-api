from fastapi import HTTPException

from store.store import Store
from helpers.generic_helpers import without_domain


def decode_url(url: str, store: Store) -> str:
    long_url = store.get(without_domain(url))
    if long_url is None:
        raise HTTPException(status_code=404,
                            detail=f"No URL found for short URL: {url}")

    return long_url
