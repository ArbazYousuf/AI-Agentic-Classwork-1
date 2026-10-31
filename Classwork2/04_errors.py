# Phase 5 - Errors, timeouts and rate limits

import time

import requests


def safe_get(url, timeout=5, retries=3):
    """GET with status checking, timeout and simple retry for 429/5xx"""
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, timeout=timeout)
        except requests.exceptions.Timeout:
            print(f"  Timeout after {timeout}s")
            return None
        except requests.exceptions.ConnectionError:
            print("  Network error, could not connect")
            return None

        if r.status_code == 200:
            return r.json()
        elif r.status_code == 404:
            print("  404 - server responded but resource not found")
            return None
        elif r.status_code in (401, 403):
            print(f"  {r.status_code} - not authorized")
            return None
        elif r.status_code == 429 or r.status_code >= 500:
            # wait before trying again, longer each time
            wait = int(r.headers.get("Retry-After", attempt))
            print(f"  {r.status_code} - attempt {attempt}, waiting {wait}s")
            time.sleep(wait)
        else:
            print(f"  Unexpected status {r.status_code}")
            return None
    print("  Gave up after", retries, "attempts")
    return None


print("1. Normal request:")
data = safe_get("https://jsonplaceholder.typicode.com/posts/1")
print("  OK:", data["title"] if data else None)

print("\n2. Missing resource:")
r = requests.get("https://jsonplaceholder.typicode.com/posts/99999", timeout=10)
print("  Server responded:", r is not None, "| status:", r.status_code, "| ok:", r.ok)
safe_get("https://jsonplaceholder.typicode.com/posts/99999")

print("\n3. Timeout (server waits 5s, we only wait 2s):")
safe_get("https://httpbin.org/delay/5", timeout=2)

print("\n4. Rate limit (429):")
safe_get("https://httpbin.org/status/429", retries=2)

print("\n5. Server error (500):")
safe_get("https://httpbin.org/status/500", retries=2)

print("\n6. Network error (domain doesn't exist):")
safe_get("https://this-domain-does-not-exist-12345.com")

print("\nProgram finished without crashing")
