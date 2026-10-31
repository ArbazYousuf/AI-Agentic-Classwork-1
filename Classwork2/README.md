# Classwork 2 - APIs, HTTP & Python API Integration

## Files

- `notes.md` - answers for all the theory parts (Phase 1 to 6)
- `01_json_basics.py` - JSON object/array to Python dict/list
- `02_api_client.py` - GET, POST, PUT, DELETE with jsonplaceholder
- `03_auth.py` - Bearer token from `.env`
- `04_errors.py` - 404, timeout, 429, 500 and network error handling
- `05_agent_tool.py` - API call written as an agent tool
- `.env.example` - template for the `.env` file (no real key)
- `evidence/` - terminal output and screenshots

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Then open `.env` and put a token. For `03_auth.py` any value works because httpbin.org just checks that a Bearer token is sent.

## Run

```
python 01_json_basics.py
python 02_api_client.py
python 03_auth.py
python 04_errors.py
python 05_agent_tool.py
```

## APIs used

- https://jsonplaceholder.typicode.com - free fake REST API
- https://httpbin.org - for testing auth, delays and status codes
