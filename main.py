from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from schemas import URL
from store.store import Store
from handlers.encode import encode_url
from handlers.decode import decode_url

app = FastAPI()

store = Store()


@app.get("/")
def read_root():
    return {"message": "Hello from URL shortener API"}


@app.post("/encode")
def encode(url: URL):
    json_compatible_item_data = jsonable_encoder(
        {"long_url": url.url, "short_url": encode_url(url.url, store)})
    return JSONResponse(content=json_compatible_item_data)


@app.post("/decode")
def decode(url: URL):
    json_compatible_item_data = jsonable_encoder(
        {"long_url": decode_url(url.url, store), "short_url": url.url})
    return JSONResponse(content=json_compatible_item_data)
