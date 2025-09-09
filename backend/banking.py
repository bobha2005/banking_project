# Implements banking functions 

import json 
import os
from auth import load_users, save_users
from datetime import datetime

TRANSACTIONS_FILE = "transactions.json"

# Function to load transactions from a file
def load_transactions():
    if not os.path.exists(TRANSACTIONS_FILE):
        return []
    try:
        with open(TRANSACTIONS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# Function to save transactions to a file    
def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w") as f:
        json.dump(transactions, f, indent=2)

# Function to handle deposit into a user's account
def deposit(username, amount):

    if amount <= 0:
        return False, "Amount must be positive."
    
    users = load_users()
    if username not in users:
        return False, "Username not found."
    
    users[username]["balance"] += amount
    save_users(users)
    
    transactions = load_transactions()
    transactions.append({
        "username": username,
        "type": "deposit",
        "amount": amount,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_transactions(transactions)
    return True, f"Successfully deposited ${amount:.2f} to your account."

# Function to handle withdrawal from a user's account
def withdraw(username, amount):
    if amount <= 0:
        return False, "Amount must be positive."
    
    users = load_users()
    if username not in users:
        return False, "Username not found."
    
    balance = users[username]["balance"]
    if amount > balance:
        return False, f"Insufficient funds. Your current balance is ${balance:.2f}"
    
    users[username]["balance"] -= amount
    save_users(users)

    transactions = load_transactions()
    transactions.append({
        "username": username,
        "type": "withdraw",
        "amount": amount,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_transactions(transactions)
    return True, f"Successfully withdraw ${amount:.2f} from your account."

# Function to handle money transfer between users
def transfer(sender, receiver, amount):
    if amount <= 0:
        return False, "Amount must be positive."

    users = load_users()
    if sender not in users:
        return False, "Sender username not found."
    
    if receiver not in users:
        return False, "Receiver username not found."
    
    sender_balance = users[sender]["balance"]
    if amount > sender_balance:
        return False, f"Insufficient funds. Your current balance is ${balance:.2f}"
    
    users[sender]["balance"] -= amount
    users[receiver]["balance"] += amount
    save_users(users)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transactions = load_transactions()
    transactions.append({
        "username": sender,
        "type": "transfer",
        "amount": -amount,
        "to": receiver,
        "timestamp": timestamp
    })
    transactions.append({
        "username": receiver,
        "type": "transfer",
        "amount": amount,
        "from": sender,
        "timestamp": timestamp
    })
    save_transactions(transactions) 
    return True, f"Successfully transferred ${amount:.2f} from {sender} to {receiver}."

# Check balance of a user's account
def get_balance(username):
    users = load_users()
    if username not in users:
        return False, "Username not found."
    return True, users[username]["balance"]

def get_transaction_history(username):
    transactions = load_transactions()
    user_transactions = [t for t in transactions if t["username"] == username]
    return user_transactions