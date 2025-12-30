import json
import os

USER_FILE = "users.json"

def load_users():
    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    users = load_users()
    users.append({"id": "test", "pw": "1234", "name": "테스트"})
    save_users(users)
    print("저장된 회원 목록:", load_users())
