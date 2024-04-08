# Stack: Python 3.11, Requests, PyTest, Pydantic, Jsonschema, Allure

## Configuration:

Place your API token in __.env__ file before running tests

```BEARER_TOKEN=' '```

## Running tests:

**Run tests:** python -m pytest --alluredir=./allure-results

**Generate allure report:** allure serve