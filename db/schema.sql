-- Ensure this is in your db/schema.sql
CREATE TABLE companies (
    ticker TEXT PRIMARY KEY,
    company_name TEXT,
    sector TEXT
);

CREATE TABLE profitandloss (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT,
    year INTEGER,
    revenue REAL,
    expenses REAL,
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
);
-- Repeat this pattern for all other tables, ensuring 'ticker' is always TEXT