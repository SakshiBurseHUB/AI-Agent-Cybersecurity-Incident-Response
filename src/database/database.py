import sqlite3
from pathlib import Path

from utils.logger import log_info

DATABASE_NAME = "incident_response.db"


def get_connection():
    """
    Create SQLite database connection.
    """

    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    """
    Create database tables using schema.sql.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # Locate schema.sql
    schema_path = Path(__file__).parent / "schema.sql"

    # Read SQL schema
    with open(schema_path, "r", encoding="utf-8") as file:
        schema = file.read()

    # Execute SQL script
    cursor.executescript(schema)

    conn.commit()
    conn.close()

    log_info("Database initialized successfully.")