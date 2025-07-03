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
    # TODO: CLI menu once logged in
    pass

def deposit(username, amount):
    pass

def withdraw(username, amount):
    pass

def transfer(username,receiver, amount):
    pass

def view_balance(username):
    pass