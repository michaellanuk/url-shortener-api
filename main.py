from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, RedirectResponse

from schemas import URL
from store.store import Store
from handlers.encode import encode_url
from handlers.decode import decode_url

app = FastAPI()

store = Store()


@app.get("/")
def read_root():
    return {"message": "Hello from URL shortener API"}


@app.post("/")
def encode(url: URL, request: Request):
    json_compatible_item_data = jsonable_encoder(
        {"long_url": url.url, "short_url": encode_url(url.url, store, str(request.url))})
    return JSONResponse(content=json_compatible_item_data)


@app.get("/{url}", response_class=RedirectResponse)
def decode(url: str, request: Request):
    return decode_url(url, store, str(request.url))
