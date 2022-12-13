SHORTENER_DOMAIN = "http://short.est/"


def with_domain(shortened_hash: str) -> str:
    return f"{SHORTENER_DOMAIN}{shortened_hash}"


def without_domain(url: str) -> str:
    return url.replace(SHORTENER_DOMAIN, "")
