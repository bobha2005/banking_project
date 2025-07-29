# 🧠 Project Notes — Secure Banking CLI

This document tracks internal planning and progress across the project phases.

---

## 📅 Phase 1: Research & Requirements (Week 1–2)

### 🎯 Project Goal
(Describe what the project aims to do — secure CLI banking system.)

### ✅ Core Features
- ✅ Register
- ✅ Login
- ✅ View Balance
- ✅ Deposit
- ✅ Withdraw
- ✅ Transaction Logging
- [ ] Transfer

### 🔐 Security Considerations
- ✅ Use bcrypt for password hashing
- ✅ Avoid storing plaintext passwords
- ✅ Ensure transaction integrity
- ✅ Basic input validation
- ✅ Local file-based storage

### 📦 Tools & Stack
- Language: Python 3
- Storage: JSON
- Hashing: bcrypt
- Version Control: Git + GitHub
- Editor: VS Code

### 🗃️ Data Format (Planned)
- users.json: store username, hashed password, balance
- transactions.json: store transfer logs with timestamps

---

## 📐 Phase 2: Design & Planning (Week 2–3)
### 🧩 Project Structure
- main.py: handles CLI interface + routing
- auth.py: handles registration + login logic
- banking.py: handles deposit, withdraw, balance
- transactions.json: persistent store for financial activity
- users.json: persistent user store

### 🧪 Testing Strategy
- Manual testing via CLI (Python run + input)
- JSON inspection + debugging via print()
- Planned: small test.py module to isolate logic

---

## 🔧 Phase 3: Prototyping (Week 3–4)
### ✅ Implemented:
- CLI Menu Flow
- Secure Registration/Login with bcrypt
- Deposit with timestamped logging
- Withdraw with balance check
- View Balance

### 📁 Notes:
- Users file is validated for missing/corrupt states
- Edge cases like negative input, malformed files are handled

---

## 🛠️ Phase 4: Build & Improve (Week 5–7)
### ✅ What Was Implemented

- Core banking features: deposit, withdraw, transfer, balance check
- Transaction logging to JSON file
- Balance calculated from transaction history
- Input validation (e.g., positive amounts, username checks)
- Default balance starts at $0 for new users
- bcrypt for password hashing (security best practice)
- Clear CLI interface with menu options
- Graceful error handling (e.g., empty or missing files)

### 📁 Project Structure
- `auth.py`: handles registration/login
- `banking.py`: contains all banking operations
- `main.py`: application entry point
- `users.json`, `transactions.json`: file-based local storage
- `project_notes.md`: internal planning document
- `README.md`: public-facing project overview

### 🔍 Testing & Validation
- Manual CLI tests for each core operation
- Edge cases: new accounts, no transactions, wrong usernames/passwords
- JSON data correctly updated across all operations

---

## 📋 Phase 5: Final Report & Reflection (Week 8)
In this final phase, I consolidated all project work and completed a written report and video demonstration. I reflected on the design decisions, implementation challenges, and lessons learned throughout the project. The report outlines the overall structure of the application, key security measures, testing strategies, and areas for potential future improvement.

Deliverables:
- Final system implementation (CLI banking system)
- 3–4 minute demonstration video
- Written report covering all phases, security considerations, and reflection

