CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    transaction_type VARCHAR(10) CHECK (transaction_type IN ('deposit', 'withdraw')),
    amount DECIMAL(18, 8) NOT NULL,
    transaction_hash VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE web3_wallets (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    wallet_address VARCHAR(42) UNIQUE NOT NULL,
    balance DECIMAL(18, 8) DEFAULT 0.0
);
