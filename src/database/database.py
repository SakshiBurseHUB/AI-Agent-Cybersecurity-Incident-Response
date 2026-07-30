import sqlite3

from utils.logger import log_info

DATABASE_NAME = "incident_response.db"


def get_connection():
    """
    Create SQLite database connection.
    """

    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    """
    Create database tables if they do not exist.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        attack TEXT,

        source_ip TEXT,

        severity TEXT,

        priority TEXT,

        risk_score INTEGER,

        recommendation TEXT,

        status TEXT
    )
    """)

    conn.commit()
    conn.close()

    log_info("Database initialized successfully.")