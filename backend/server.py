from flask import Flask, jsonify, request
import os
from flask_cors import CORS
from banking import deposit, withdraw, get_balance, transfer, get_transaction_history
from auth import register, login

app = Flask(__name__)
CORS(app, origins=["https://bobha2005.github.io"]) # Enable CORS for React frontend

# Register a new user
@app.route('/register', methods=['POST'])
def api_register():
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "message": "No data provided"}), 400
        
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        success, message = register(username, password, confirm_password)

        if success:
            return jsonify({"success": True, "message": message}), 201
        else:
            return jsonify({"success": False, "message": message}), 400
        
    except Exception as e:
        return jsonify({"success": False, "message": "Server Error"}), 500

# Login a user
@app.route('/login', methods=['POST'])
def api_login():
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "message": "No data provided"}), 400
        
        username = data.get('username')
        password = data.get('password')

        success, message = login(username, password)
        
        if success:
            return jsonify({"success": True, "message": message, "username": username}), 200
        else:
            return jsonify({"success": False, "message": message}), 401
        
    except Exception as e:
        return jsonify({"success": False, "message": "Server Error"}), 500

# Balance 
@app.route('/balance', methods=['GET'])
def api_balance():
    try:
        username = request.args.get('username')
        if not username:
            return jsonify({"success": False, "message": "Username is required"}), 400
        
        success, balance = get_balance(username)

        if success:
            return jsonify({"success": True, "username": username, "balance": balance}), 200
        else:
            return jsonify({"success": False, "message": balance}), 404
        
    except Exception as e:
        return jsonify({"success": False, "message": "Server Error"}), 500

# Deposit
@app.route('/deposit', methods=['POST'])
def api_deposit():
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "message": "No data provided"}), 400
            
        username = data.get('username')
        amount = data.get('amount')
        
        if not username or amount is None:
            return jsonify({"success": False, "message": "Username and amount required"}), 400
            
        try:
            amount = float(amount)
        except ValueError:
            return jsonify({"success": False, "message": "Invalid amount"}), 400
            
        success, message = deposit(username, amount)
        
        if success:
            # Get updated balance
            _, new_balance = get_balance(username)
            return jsonify({"success": True, "message": message, "new_balance": new_balance}), 200
        else:
            return jsonify({"success": False, "message": message}), 400
            
    except Exception as e:
        return jsonify({"success": False, "message": "Server error"}), 500
    
# Withdraw
@app.route('/withdraw', methods=['POST'])
def api_withdraw():
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "message": "No data provided"}), 400
            
        username = data.get('username')
        amount = data.get('amount')
        
        if not username or amount is None:
            return jsonify({"success": False, "message": "Username and amount required"}), 400
            
        try:
            amount = float(amount)
        except ValueError:
            return jsonify({"success": False, "message": "Invalid amount"}), 400
            
        success, message = withdraw(username, amount)
        
        if success:
            # Get updated balance
            _, new_balance = get_balance(username)
            return jsonify({"success": True, "message": message, "new_balance": new_balance}), 200
        else:
            return jsonify({"success": False, "message": message}), 400
            
    except Exception as e:
        return jsonify({"success": False, "message": "Server error"}), 500
    
# Transfer
@app.route('/transfer', methods=['POST'])
def api_transfer():
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "message": "No data provided"}), 400
            
        sender = data.get('username')
        receiver = data.get('to')
        amount = data.get('amount')
        
        if not sender or not receiver or amount is None:
            return jsonify({"success": False, "message": "Sender, receiver, and amount required"}), 400
            
        try:
            amount = float(amount)
        except ValueError:
            return jsonify({"success": False, "message": "Invalid amount"}), 400
            
        success, message = transfer(sender, receiver, amount)
        
        if success:
            # Get updated balance for sender
            _, new_balance = get_balance(sender)
            return jsonify({"success": True, "message": message, "new_balance": new_balance}), 200
        else:
            return jsonify({"success": False, "message": message}), 400
            
    except Exception as e:
        return jsonify({"success": False, "message": "Server error"}), 500
    
# Transaction history
@app.route('/transactions', methods=['GET'])
def api_transactions():
    try:
        username = request.args.get('username')
        if not username:
            return jsonify({"success": False, "message": "Username required"}), 400
            
        transactions = get_transaction_history(username)
        return jsonify({"success": True, "transactions": transactions}), 200
        
    except Exception as e:
        return jsonify({"success": False, "message": "Server error"}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Banking API is running"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001)) # Uses service port or 5001
    app.run(host='0.0.0.0', port=port)