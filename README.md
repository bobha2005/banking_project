# 💰 banking_project

This is a secure command-line banking system built for COMP6441. It supports encrypted user registration, login, transactions, and account balance tracking — all through a lightweight Python CLI.

---

## 🚀 Setup

1. Clone the repository
2. Create virtual environment:  
   `python3 -m venv venv`
3. Activate environment:  
   `source venv/bin/activate`
4. Install dependencies:  
   `pip install -r requirements.txt`
5. Run the program:  
   `python src/main.py`

---

## ✅ Features

- 🔐 Secure password hashing (bcrypt)
- 🧾 Deposit, Withdraw, and Transfer funds
- 📊 View balance (real-time from transaction history)
- 📂 JSON file storage for users and transactions
- 💡 Handles edge cases (e.g., new users, empty logs)
- 🧱 Modular codebase (auth.py, banking.py, main.py)

---

## 📌 Project Milestones

- ✅ Phase 1: Research & Requirements
- ✅ Phase 2: Design & Planning
- ✅ Phase 3: Prototyping Core Logic
- ✅ Phase 4: Full Feature Implementation & Error Handling
- ✅ Phase 5: Final Report & Reflection

---

## 🛡️ Security Considerations

- Passwords are never stored in plaintext.
- bcrypt hashing makes user data resistant to brute-force attacks.
- Input validation ensures transaction and access reliability.
