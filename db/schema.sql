-- Enable Foreign Key enforcement
PRAGMA foreign_keys = ON;

-- 1. Master Table
CREATE TABLE companies (
    id INTEGER PRIMARY KEY,
    ticker TEXT UNIQUE NOT NULL,
    company_name TEXT NOT NULL
);

-- 2. Profit and Loss
CREATE TABLE profitandloss (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    sales REAL,
    net_profit REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- 3. Balance Sheet
CREATE TABLE balancesheet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    assets REAL,
    liabilities REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- 4. Cash Flow
CREATE TABLE cashflow (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    operating_cash_flow REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- 5. Analysis
CREATE TABLE analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    description TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- 6. Documents
CREATE TABLE documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    doc_type TEXT,
    url TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- 7. ProsAndCons
CREATE TABLE prosandcons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    type TEXT CHECK(type IN ('PRO', 'CON')),
    description TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- 8. Sectors
CREATE TABLE sectors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    sector_name TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- 9. Stock_Prices
CREATE TABLE stock_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    close_price REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- 10. Financial_Ratios
CREATE TABLE financial_ratios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    pe_ratio REAL,
    roe REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);