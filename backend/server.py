from flask import Flask, jsonify, request
from banking import deposit, withdraw, get_balance, transfer
from auth import register, login, load_users, save_users

app = Flask(__name__)

# Register a new user
@app.route('/register', methods=['POST'])
def api_register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    return jsonify({"message": f"User {username} registered!"})

# Login a user
@app.route('/login', methods=['POST'])
def api_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    return jsonify({"message": f"User {username} logged in!"})

# Balance 
@app.route('/balance', methods=['GET'])
def api_balance():
    username = request.args.get('username', '')
    balance = get_balance(username)
    return jsonify({"username": username, "balance": balance})

# Withdraw
@app.route('/withdraw', methods=['POST'])
def api_withdraw():
    data = request.json
    username = data.get('username')
    amount = float(data.get('amount'))
    new_balance = withdraw(username, amount)
    return jsonify({"username": username, "new_balance": new_balance})

# Transfer
@app.route('/transfer', methods=['POST'])
def api_transfer():
    data = request.json
    sender = data.get('username')
    receiver = data.get('to')
    amount = float(data.get('amount'))
    new_balance = transfer(sender, receiver, amount)
    return jsonify({"from": sender, "to": receiver, "new_balance": new_balance})

if __name__ == '__main__':
    app.run(debug=True, port=5000)