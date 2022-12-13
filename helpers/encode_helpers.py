MAX_URL_LENGTH = 2048

SHORTENER_DOMAINS = [
    "polr.me",
    "bit.ly",
    "is.gd",
    "tiny.cc",
    "adf.ly",
    "ur1.ca",
    "goo.gl",
    "ow.ly",
    "j.mp",
    "t.co"
]


def is_shortened_url(url: str) -> bool:
    for domain in SHORTENER_DOMAINS:
        if f"://{domain}" in url:
            return True

    return False


def exceeds_length(url: str) -> bool:
    return len(url) > MAX_URL_LENGTH
