# Phase 6 - Final task: an API operation that could be used as an agent tool
#
# Endpoint : GET https://jsonplaceholder.typicode.com/posts/{post_id}
# Input    : post_id (int, 1 to 100)
# Output   : {"id", "userId", "title", "body"}
# Errors   : 404 not found, 429 rate limit, 5xx server error, timeout, network error

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_post(post_id: int) -> dict:
    """Get a blog post by id. Always returns a dict so the agent can read the result."""
    try:
        r = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=5)
    except requests.exceptions.Timeout:
        return {"error": "timeout"}
    except requests.exceptions.ConnectionError:
        return {"error": "network error"}

    if r.status_code == 200:
        post = r.json()
        return {"id": post["id"], "title": post["title"], "body": post["body"]}
    if r.status_code == 404:
        return {"error": f"post {post_id} not found"}
    return {"error": f"API returned status {r.status_code}"}


# this is how the tool would be described to an LLM agent (name, description, inputs)
get_post_tool = {
    "name": "get_post",
    "description": "Get a blog post by its id. Returns title and body.",
    "input_schema": {
        "type": "object",
        "properties": {"post_id": {"type": "integer", "description": "Post id from 1 to 100"}},
        "required": ["post_id"],
    },
}

if __name__ == "__main__":
    # pretend the agent decided to call the tool with these inputs
    for pid in [5, 500]:
        print(f"get_post({pid}) ->", get_post(pid))
