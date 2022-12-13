from fastapi import HTTPException

from store.store import Store


def decode_url(url: str, store: Store, domain: str) -> str:
    long_url = store.get(url.replace(domain, ""))
    if long_url is None:
        raise HTTPException(status_code=404,
                            detail=f"No URL found for short URL: {url}")

    return long_url
