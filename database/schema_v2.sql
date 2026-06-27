DROP TABLE IF EXISTS IPO_MASTER;

CREATE TABLE IPO_MASTER (

    ipo_id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_name TEXT NOT NULL,

    symbol TEXT UNIQUE,

    isin TEXT,

    exchange TEXT,

    ipo_type TEXT,

    issue_price REAL,

    listing_price REAL,

    current_price REAL,

    ipo_open_date TEXT,

    ipo_close_date TEXT,

    listing_date TEXT,

    lot_size INTEGER,

    issue_size_cr REAL,

    face_value REAL,

    sector TEXT,

    industry TEXT,

    lead_manager TEXT,

    registrar TEXT,

    market_maker TEXT,

    status TEXT DEFAULT 'ACTIVE',

    created_at TEXT,

    updated_at TEXT

);