CREATE TABLE IF NOT EXISTS incidents (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    attack TEXT NOT NULL,

    source_ip TEXT NOT NULL,

    severity TEXT NOT NULL,

    priority TEXT NOT NULL,

    risk_score INTEGER NOT NULL,

    recommendation TEXT NOT NULL,

    status TEXT NOT NULL DEFAULT 'Open'
);