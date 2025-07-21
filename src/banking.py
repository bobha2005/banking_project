# Implements banking functions 

import json 
import os

from auth import load_users
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

# Function to display banking menu and handle user actions
def banking_menu(username):
    while True:
        print(f"\n Welcome, {username}!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Transfer")
        print("5. Logout")

        choice = input("Select options: ").strip()
        if choice == "1":
            deposit(username)
        elif choice == "2":
            withdraw(username)
        elif choice == "3":
            view_balance(username)
        elif choice == "4":
            receiver = input("Enter receiver username: ").strip()
            try:
                amount = float(input("Enter amount to transfer: "))
                if amount <= 0:
                    print("Amount must be positive.")
                else:
                    transfer(username, receiver, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("\nInvalid options! Please try again.")

# Function to handle deposit into a user's account
def deposit(username):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    transactions = load_transactions()
    transactions.append({
        "username": username,
        "type": "deposit",
        "amount": amount,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_transactions(transactions)
    print(f"Successfully deposited ${amount:.2f} to your account.")

# Function to handle withdrawal from a user's account
def withdraw(username):
    try: 
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    balance = get_balance(username) 
    if amount > balance:
        print(f"Insufficient funds. Your current balance is ${balance:.2f}")
        return
    
    transactions = load_transactions()
    transactions.append({
        "username": username,
        "type": "withdraw",
        "amount": amount,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_transactions(transactions)
    print(f"Successfully withdraw ${amount:.2f} from your account.")

# Function to handle money transfer between users
def transfer(sender, receiver, amount):
    users = load_users()

    if sender not in users:
        print("Sender username not found.")
        return
    
    if receiver not in users:
        print("Receiver username not found.")
        return
    
    balance = get_balance(sender)
    if amount <= 0:
        print("Transfer amount must be positive.")
        return
    
    if amount > balance:
        print(f"Insufficient funds. Your current balance is ${balance:.2f}")
        return
    
    timestampe = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transactions = load_transactions()
    transactions.append({
        "username": sender,
        "type": "transfer",
        "amount": -amount,
        "to": receiver,
        "timestamp": timestampe
    })
    transactions.append({
        "username": receiver,
        "type": "transfer",
        "amount": amount,
        "from": sender,
        "timestamp": timestampe
    })
    save_transactions(transactions) 
    print(f"Successfully transferred ${amount:.2f} from {sender} to {receiver}.")

# Function to view current balance for a user
def view_balance(username):
    balance = get_balance(username)
    print(f"Your current balance is ${balance:.2f}")

# Helper function to get the current balance for a user
def get_balance(username):
    transactions = load_transactions()
    if not transactions:
        return 0.0
    # Calculate balance based on transactions
    return current_balance(transactions, username)

# Helper function to calculate current balance
def current_balance(transactions, username):
    balance = 0.0
    for transaction in transactions:
        if transaction["username"] == username:
            if transaction["type"] == "deposit":
                balance += transaction["amount"]
            elif transaction["type"] == "withdraw":
                balance -= transaction["amount"]
    return balance