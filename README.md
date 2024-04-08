# Stack: Python 3.11, Requests, PyTest, Pydantic, Jsonschema, Allure

## Configuration:
1. Install requirements: __pip install -r requirements.txt__

2. Place your API token in __.env__ file before running tests ```BEARER_TOKEN=''```

## Running tests:

**Run tests:** python -m pytest --alluredir=./allure-results

**Generate allure report:** allure serve