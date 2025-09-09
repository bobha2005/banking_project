import React, { useState } from 'react';

function App() {
  const [username, setUsername] = useState('');
  const [balance, setBalance] = useState(null);

  const fetchBalance = async () => {
    const response = await fetch(`http://localhost:5000/balance?username=${username}`);
    const data = await response.json();
    setBalance(data.balance);
  };
  
  return (
    <div>
      <h1>Secure Banking</h1>
      <input
        type="text"
        placeholder="Enter username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <button onClick={fetchBalance}>Get Balance</button>
      {balance !== null && <p>Balance: ${balance}</p>}
    </div>
  );
}

export default App;
