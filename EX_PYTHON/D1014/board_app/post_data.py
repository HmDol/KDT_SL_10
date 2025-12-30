import json
import os
from datetime import datetime

POST_FILE = "posts.json"

def load_posts():
    if not os.path.exists(POST_FILE):
        return []
    with open(POST_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_posts(posts):
    with open(POST_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    posts = load_posts()
    new_post = {
        "id": len(posts) + 1,
        "author": "test",
        "title": "테스트 게시글",
        "content": "내용입니다.",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    posts.append(new_post)
    save_posts(posts)
    print("저장된 게시글 목록:", load_posts())
