# Handle users authentication logic 

import bcrypt
import json
import os 

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)
    
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def register(username, password):
    # TODO: Secure user registration
    pass

def login(username, password):
    # TODO: Secure user login
    pass