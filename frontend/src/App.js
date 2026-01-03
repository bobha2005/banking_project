import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  // State management
  const [currentUser, setCurrentUser] = useState(null);
  const [balance, setBalance] = useState(null);
  const [transactions, setTransactions] = useState([]);
  const [activeTab, setActiveTab] = useState('login');
  const [message, setMessage] = useState('');
  const [messageType, setMessageType] = useState(''); // 'success' or 'error'

  // Form states
  const [loginForm, setLoginForm] = useState({ username: '', password: '' });
  const [registerForm, setRegisterForm] = useState({ 
    username: '', 
    password: '', 
    confirm_password: '' 
  });
  const [transactionForm, setTransactionForm] = useState({ 
    amount: '', 
    recipient: '' 
  });

  const API_BASE = 'http://localhost:5001';

  // Show message helper
  const showMessage = (msg, type = 'info') => {
    setMessage(msg);
    setMessageType(type);
    setTimeout(() => setMessage(''), 5000);
  };

  // API call helper
  const apiCall = async (endpoint, method = 'GET', data = null) => {
    try {
      const options = {
        method,
        headers: { 'Content-Type': 'application/json' }
      };
      
      if (data) {
        options.body = JSON.stringify(data);
      }
      
      const response = await fetch(`${API_BASE}${endpoint}`, options);
      return await response.json();
    } catch (error) {
      console.error('API Error:', error);
      return { success: false, message: 'Network error' };
    }
  };

  // Authentication functions
  const handleLogin = async (e) => {
    e.preventDefault();
    const result = await apiCall('/login', 'POST', loginForm);
    
    if (result.success) {
      setCurrentUser(loginForm.username);
      setActiveTab('dashboard');
      showMessage(result.message, 'success');
      await fetchBalance(loginForm.username);
      await fetchTransactions(loginForm.username);
    } else {
      showMessage(result.message, 'error');
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    const result = await apiCall('/register', 'POST', registerForm);
    
    if (result.success) {
      showMessage(result.message, 'success');
      setActiveTab('login');
      setRegisterForm({ username: '', password: '', confirm_password: '' });
    } else {
      showMessage(result.message, 'error');
    }
  };

  const handleLogout = () => {
    setCurrentUser(null);
    setBalance(null);
    setTransactions([]);
    setActiveTab('login');
    setLoginForm({ username: '', password: '' });
    showMessage('Logged out successfully', 'success');
  };

  // Banking functions
  const fetchBalance = async (username = currentUser) => {
    if (!username) return;
    
    const result = await apiCall(`/balance?username=${username}`);
    if (result.success) {
      setBalance(result.balance);
    } else {
      showMessage(result.message, 'error');
    }
  };

  const fetchTransactions = async (username = currentUser) => {
    if (!username) return;
    
    const result = await apiCall(`/transactions?username=${username}`);
    if (result.success) {
      setTransactions(result.transactions);
    }
  };

  const handleDeposit = async (e) => {
    e.preventDefault();
    const result = await apiCall('/deposit', 'POST', {
      username: currentUser,
      amount: transactionForm.amount
    });
    
    if (result.success) {
      setBalance(result.new_balance);
      showMessage(result.message, 'success');
      setTransactionForm({ ...transactionForm, amount: '' });
      await fetchTransactions();
    } else {
      showMessage(result.message, 'error');
    }
  };

  const handleWithdraw = async (e) => {
    e.preventDefault();
    const result = await apiCall('/withdraw', 'POST', {
      username: currentUser,
      amount: transactionForm.amount
    });
    
    if (result.success) {
      setBalance(result.new_balance);
      showMessage(result.message, 'success');
      setTransactionForm({ ...transactionForm, amount: '' });
      await fetchTransactions();
    } else {
      showMessage(result.message, 'error');
    }
  };

  const handleTransfer = async (e) => {
    e.preventDefault();
    const result = await apiCall('/transfer', 'POST', {
      username: currentUser,
      to: transactionForm.recipient,
      amount: transactionForm.amount
    });
    
    if (result.success) {
      setBalance(result.new_balance);
      showMessage(result.message, 'success');
      setTransactionForm({ amount: '', recipient: '' });
      await fetchTransactions();
    } else {
      showMessage(result.message, 'error');
    }
  };

  // Auto-refresh balance and transactions
  useEffect(() => {
    if (currentUser) {
      const interval = setInterval(() => {
        fetchBalance();
        fetchTransactions();
      }, 30000); // Refresh every 30 seconds
      
      return () => clearInterval(interval);
    }
  }, [currentUser]);

  return (
    <div className="App">
      <header className="app-header">
        <h1>DABank</h1>
        {currentUser && (
          <div className="user-info">
            <span>Welcome, {currentUser}!</span>
          </div>
        )}
      </header>

      {/* Message Display */}
      {message && (
        <div className={`message ${messageType}`}>
          {message}
        </div>
      )}

      {/* Authentication Section */}
      {!currentUser && (
        <div className="auth-section">
          <div className="tab-buttons">
            <button 
              className={`tab-btn ${activeTab === 'login' ? 'active' : ''}`}
              onClick={() => setActiveTab('login')}
            >
              Login
            </button>
            <button 
              className={`tab-btn ${activeTab === 'register' ? 'active' : ''}`}
              onClick={() => setActiveTab('register')}
            >
              Register
            </button>
          </div>

          {activeTab === 'login' && (
            <form onSubmit={handleLogin} className="auth-form">
              <h2>Login</h2>
              <input
                type="text"
                placeholder="Username"
                value={loginForm.username}
                onChange={(e) => setLoginForm({...loginForm, username: e.target.value})}
                required
              />
              <input
                type="password"
                placeholder="Password"
                value={loginForm.password}
                onChange={(e) => setLoginForm({...loginForm, password: e.target.value})}
                required
              />
              <button type="submit" className="btn btn-primary">Login</button>
            </form>
          )}

          {activeTab === 'register' && (
            <form onSubmit={handleRegister} className="auth-form">
              <h2>Register</h2>
              <input
                type="text"
                placeholder="Username"
                value={registerForm.username}
                onChange={(e) => setRegisterForm({...registerForm, username: e.target.value})}
                required
              />
              <input
                type="password"
                placeholder="Password"
                value={registerForm.password}
                onChange={(e) => setRegisterForm({...registerForm, password: e.target.value})}
                required
              />
              <input
                type="password"
                placeholder="Confirm Password"
                value={registerForm.confirm_password}
                onChange={(e) => setRegisterForm({...registerForm, confirm_password: e.target.value})}
                required
              />
              <button type="submit" className="btn btn-primary">Register</button>
            </form>
          )}
        </div>
      )}

      {/* Banking Dashboard */}
      {currentUser && (
        <div className="dashboard">
          <div className="balance-card">
            <h2>Account Balance</h2>
            <div className="balance-amount">
              ${balance !== null ? balance.toFixed(2) : 'Loading...'}
            </div>
            <button onClick={() => fetchBalance()} className="btn btn-secondary">
              Refresh Balance
            </button>
          </div>

          <div className="operations-section">
            <div className="tab-buttons">
              <button 
                className={`tab-btn ${activeTab === 'deposit' ? 'active' : ''}`}
                onClick={() => setActiveTab('deposit')}
              >
                Deposit
              </button>
              <button 
                className={`tab-btn ${activeTab === 'withdraw' ? 'active' : ''}`}
                onClick={() => setActiveTab('withdraw')}
              >
                Withdraw
              </button>
              <button 
                className={`tab-btn ${activeTab === 'transfer' ? 'active' : ''}`}
                onClick={() => setActiveTab('transfer')}
              >
                Transfer
              </button>
              <button 
                className={`tab-btn ${activeTab === 'history' ? 'active' : ''}`}
                onClick={() => setActiveTab('history')}
              >
                History
              </button>
            </div>

            {/* Deposit Form */}
            {activeTab === 'deposit' && (
              <form onSubmit={handleDeposit} className="transaction-form">
                <h3>💰 Deposit Money</h3>
                <input
                  type="number"
                  step="0.01"
                  min="0.01"
                  placeholder="Amount"
                  value={transactionForm.amount}
                  onChange={(e) => setTransactionForm({...transactionForm, amount: e.target.value})}
                  required
                />
                <button type="submit" className="btn btn-success">Deposit</button>
              </form>
            )}

            {/* Withdraw Form */}
            {activeTab === 'withdraw' && (
              <form onSubmit={handleWithdraw} className="transaction-form">
                <h3>💸 Withdraw Money</h3>
                <input
                  type="number"
                  step="0.01"
                  min="0.01"
                  placeholder="Amount"
                  value={transactionForm.amount}
                  onChange={(e) => setTransactionForm({...transactionForm, amount: e.target.value})}
                  required
                />
                <button type="submit" className="btn btn-warning">Withdraw</button>
              </form>
            )}

            {/* Transfer Form */}
            {activeTab === 'transfer' && (
              <form onSubmit={handleTransfer} className="transaction-form">
                <h3>💳 Transfer Money</h3>
                <input
                  type="text"
                  placeholder="Recipient Username"
                  value={transactionForm.recipient}
                  onChange={(e) => setTransactionForm({...transactionForm, recipient: e.target.value})}
                  required
                />
                <input
                  type="number"
                  step="0.01"
                  min="0.01"
                  placeholder="Amount"
                  value={transactionForm.amount}
                  onChange={(e) => setTransactionForm({...transactionForm, amount: e.target.value})}
                  required
                />
                <button type="submit" className="btn btn-info">Transfer</button>
              </form>
            )}

            {/* Transaction History */}
            {activeTab === 'history' && (
              <div className="transaction-history">
                <h3>📋 Transaction History</h3>
                {transactions.length === 0 ? (
                  <p>No transactions yet.</p>
                ) : (
                  <div className="transactions-list">
                    {transactions.slice().reverse().map((transaction, index) => (
                      <div key={index} className={`transaction-item ${transaction.type}`}>
                        <div className="transaction-info">
                          <strong>{transaction.type.toUpperCase()}</strong>
                          <span className="transaction-amount">
                            ${Math.abs(transaction.amount).toFixed(2)}
                          </span>
                        </div>
                        <div className="transaction-details">
                          {transaction.to && <span>To: {transaction.to}</span>}
                          {transaction.from && <span>From: {transaction.from}</span>}
                          <span className="timestamp">{transaction.timestamp}</span>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      )}
      {/* Logout Button Pinned to Bottom */}
        {currentUser && (
          <div className="logout-container">
            <button onClick={handleLogout} className="btn-logout">
              Logout
            </button>
          </div>
        )}
    </div>
  );
}

export default App;
