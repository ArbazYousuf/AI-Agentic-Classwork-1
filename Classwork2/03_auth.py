# Phase 4 - Authentication with a Bearer token loaded from .env
# httpbin.org/bearer is a test endpoint: it returns 200 if a Bearer token is sent, 401 if not

import os

import requests
from dotenv import load_dotenv

load_dotenv()  # reads the .env file
API_TOKEN = os.getenv("API_TOKEN")

if not API_TOKEN:
    print("API_TOKEN not found, copy .env.example to .env and add your token")
    raise SystemExit(1)

URL = "https://httpbin.org/bearer"

# without token -> should be 401
r = requests.get(URL, timeout=10)
print("Without token ->", r.status_code)

# with token in the Authorization header
headers = {"Authorization": f"Bearer {API_TOKEN}", "Accept": "application/json"}
r = requests.get(URL, headers=headers, timeout=10)
print("With token ->", r.status_code)
if r.status_code == 200:
    data = r.json()
    print("Authenticated:", data["authenticated"])
    # don't print the full token
    print("Token used:", data["token"][:4] + "****")
