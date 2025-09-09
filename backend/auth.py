# Handle users authentication logic 

import bcrypt
import json
import os

USERS_FILE = "users.json"

# Function to load users from a file
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

# Function to save users to a file    
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f,  indent=2)

# Function to register a new user
def register(username, password, confirm_password):
    users = load_users()

    if not username:
        return False, "Username cannot be empty."

    if username in users:
        return False, "Username already exists."
    
    if not password:
        return False, "Password cannot be empty."

    if password != confirm_password:
        return False, "Passwords do not match."
    
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    users[username] = {
        "password": hashed_password, 
        "balance": 0.0
    }
    save_users(users)

    return True, f"User {username} registered."

# Function to login a user 
def login(username, password):
    users = load_users()

    if username not in users:
        return False, "Username not found."
    
    check_password = users[username]["password"].encode()

    if bcrypt.checkpw(password.encode(), check_password):
        return True, "Login successful."
    
    return False, "Incorrect password."
