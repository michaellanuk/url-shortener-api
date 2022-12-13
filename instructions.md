## URL Shortener API

Built with FastAPI

### Project structure

- `main.py`
  - Main entry point for app. Contains routes for `/encode` and `/decode` endpoints.
- `schemas.py`
  - Contains URL class for request bodies.
- `tests/`
  - API tests for both endpoints. See below for instructions on how to run tests.
- `store/`
  - Contains key-value, in-memory store for mapping encoded/shortened URLs to their original, long URLs. Could be replaced in production by NoSQL database e.g., DynamoDB, MongoDB, or act as caching layer in front of database.
- `helpers/`
  - Helper functions for handler methods e.g., validating data.
- `handlers/`
  - Main logic and algorithm behind `/encode` and `/decode` endpoints.


### Installation

1. Create a virtual environment
```
$ python -m venv venv
$ source venv/bin/activate
```

2. Install packages
```
$ python -m pip install -r requirements.txt
```

### Running the app

Run the app with uvicorn:
```
$ uvicorn main:app
```
Use the `--reload` flag to enable hot reloading

App will run on http://127.0.0.1:8000

### Example usage

* `/encode` - POST - encode a URL, returns an encoded, shortened URL
  * Example cURL request (can be imported into Postman or run from command line):
    ```
    curl --location --request POST 'localhost:8000/encode' \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "url": "https://www.google.com"
    }'
    ```
  * Expected response body
    ```
    {
      "long_url": "https://www.google.com",
      "short_url": "http://short.est/wEFUol"
    }
    ```
* `/decode` - POST - decode a shortened URL, returns original and shortened URL
  * Example cURL request:
    ```
    curl --location --request POST 'localhost:8000/decode' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "url": "http://short.est/wEFUol"
    }'
    ```
  * Expected response body
    ```
    {
      "long_url": "https://www.google.com",
      "short_url": "http://short.est/wEFUol"
    }
    ```

### Testing

In the project root, run
```
$ python -m pytest
```
to run tests
