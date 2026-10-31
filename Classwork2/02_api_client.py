# Phase 2 D + Phase 3 C - Python API client with GET, POST, PUT, DELETE
# API used: https://jsonplaceholder.typicode.com (free fake REST API)

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# ---------- GET one post ----------
response = requests.get(f"{BASE_URL}/posts/1", timeout=10)
print("GET /posts/1 ->", response.status_code)

if response.status_code == 200:
    post = response.json()  # JSON -> dict
    print("  Title:", post["title"])
    print("  User ID:", post["userId"])
    print("  Content-Type header:", response.headers["Content-Type"])

# ---------- GET posts 1, 2, 3 (same as changing the id in the browser) ----------
print()
for post_id in [1, 2, 3]:
    r = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=10)
    print(f"GET /posts/{post_id} -> {r.status_code}: {r.json()['title'][:40]}")

# ---------- GET a list and loop through it ----------
r = requests.get(f"{BASE_URL}/posts", params={"userId": 1}, timeout=10)
posts = r.json()  # JSON array -> list of dicts
print(f"\nGET /posts?userId=1 -> {r.status_code}, got {len(posts)} posts")
for p in posts[:3]:
    print("  -", p["id"], p["title"][:40])

# ---------- POST (create) ----------
new_post = {"title": "My first post", "body": "Hello from Python", "userId": 1}
r = requests.post(f"{BASE_URL}/posts", json=new_post, timeout=10)
print("\nPOST /posts ->", r.status_code, r.json())  # 201 Created

# ---------- PUT (update) ----------
updated_post = {"id": 1, "title": "Updated title", "body": "Updated body", "userId": 1}
r = requests.put(f"{BASE_URL}/posts/1", json=updated_post, timeout=10)
print("PUT /posts/1 ->", r.status_code, r.json())

# ---------- DELETE ----------
r = requests.delete(f"{BASE_URL}/posts/1", timeout=10)
print("DELETE /posts/1 ->", r.status_code)

# note: jsonplaceholder is fake so POST/PUT/DELETE don't really change anything on the server
