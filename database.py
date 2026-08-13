import json
import os

STORE_FILE = "/tmp/store.json"  # Menggunakan folder /tmp karena Netlify bersifat read-only di root

def load_store():
    if not os.path.exists(STORE_FILE):
        return {"users": {}, "admin": {}, "vip": {}, "banned": {}, "maintenance": False, "stats": {}}
    with open(STORE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_store(store_data):
    with open(STORE_FILE, "w", encoding="utf-8") as f:
        json.dump(store_data, f, indent=4)

STORE = load_store()
ADMINS = STORE.get("admin", {})
ALLOWED_USERS = list(STORE.get("users", {}).keys())
EXPIRY = STORE.get("expiry", {})

def has_admin(user_id, min_role="admin"):
    levels = {"moderator": 5, "admin": 10, "superadmin": 50, "owner": 100}
    user_role = ADMINS.get(str(user_id), "user")
    return levels.get(user_role, 0) >= levels.get(min_role, 0)

def is_vip(user_id):
    return str(user_id) in STORE.get("vip", {})

def is_banned(user_id):
    return str(user_id) in STORE.get("banned", {})

def admin_log(user_id, action, details):
    print(f"[ADMIN LOG] User: {user_id} | Action: {action} | Details: {details}")

def store_add_vip(user_id):
    STORE.setdefault("vip", {})[str(user_id)] = True
    save_store(STORE)

def store_remove_vip(user_id):
    STORE.get("vip", {}).pop(str(user_id), None)
    save_store(STORE)

def store_add_admin(user_id, role):
    STORE.setdefault("admin", {})[str(user_id)] = role
    save_store(STORE)

def store_remove_admin(user_id):
    STORE.get("admin", {}).pop(str(user_id), None)
    save_store(STORE)

