# URL Shortener API

Built with FastAPI, hosted on https://url-shortener-api.fly.dev/

## Project structure

- `main.py`
  - Main entry point for app. Contains routes for `/encode` and `/decode` endpoints.
- `schemas.py`
  - Contains URL class for request bodies.
- `tests/`
  - API tests for both endpoints. See below for instructions on how to run tests.
- `store/`
  - Contains key-value, in-memory store for mapping encoded/shortened URLs to their original, long URLs. Implemented
  as a LRU-cache with a max capacity.
- `helpers/`
  - Helper functions for handler methods e.g., validating data.
- `handlers/`
  - Main logic and algorithm behind `/encode` and `/decode` endpoints.


## Installing and running the application

### With Python

1. Create a virtual environment
```
$ python -m venv venv
$ source venv/bin/activate
```

2. Install packages
```
$ python -m pip install -r requirements.txt
```

3. Run the app with uvicorn:
```
$ uvicorn main:app
```
Use the `--reload` flag to enable hot reloading

### With Docker
1. Build docker image
```
$ docker build docker build -t url-shortener-image .
```

2. Run docker container
```
$ docker run -d --name url-shortener-container -p 80:80 url-shortener-image
```

## Example usage

* `/` - POST - encode a URL, returns an encoded, shortened URL
  * Example cURL request (can be imported into Postman or run from command line):
    ```
    curl --location --request POST 'localhost:8000/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "url": "https://www.google.com"
    }'
    ```
  * Expected response body
    ```
    {
      "long_url": "https://www.facebook.com",
      "short_url": "http://localhost:8000/BQRvJs"
    }
    ```

* `/:url` - GET - decode a shortened URL and redirect to original URL
  * Example URL to request in browser: `localhost:8000/BQRvJs`

Visit `/docs` or `/redoc` to view interactive API docs

## Testing

In the project root, run
```
$ python -m pytest
```
to run tests
