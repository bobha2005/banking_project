# Implements banking functions 

import json 
import os
from datetime import datetime

TRANSACTIONS_FILE = "transactions.json"

def load_transactions():
    if not os.path.exists(TRANSACTIONS_FILE):
        return []
    with open(TRANSACTIONS_FILE, "r") as f:
        return json.load(f)
    
def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w") as f:
        json.dump(transactions, f, indent=2)

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
            transfer(username)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("\nInvalid options! Please try again.")

# Banking functions for deposit, withdraw, transfer, and view balance
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

def transfer(username):
    pass

def view_balance(username):
    balance = get_balance(username)
    print(f"Your current balance is ${balance:.2f}")

def get_balance(username):
    transactions = load_transactions()
    return current_balance(transactions, username)

def current_balance(transactions, username):
    balance = 0.0
    for transaction in transactions:
        if transaction["username"] == username:
            if transaction["type"] == "deposit":
                balance += transaction["amount"]
            elif transaction["type"] == "withdraw":
                balance -= transaction["amount"]
    return balance