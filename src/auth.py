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
        json.dump(users, f, indent=2)

# Function to register a new user
def register():
    users = load_users()

    username = input("Enter username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    if username in users:
        print("Username already exists.")
        return
    
    password = input("Enter password: ").strip()
    confrim_password = input("Confirm password: ").strip()

    if password != confrim_password:
        print("Passwords do not match.")
        return
    
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed_password.decode()

    save_users(users)
    print("User registered successfully.")

# Function to login a user 
def login():
    users = load_users()

    username = input("Enter username: ").strip()
    if username not in users:
        print("Username not found.")
        return None
    
    password = input("Enter your password: ").strip()
    hashed_pw = users[username].encode()

    if bcrypt.checkpw(password.encode(), hashed_pw):
        print("Login successful.")
        return username
    else:
        print("Invalid password.")
        return None
    
