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

    schema_path = Path(__file__).parent / "schema.sql"

    with open(schema_path, "r", encoding="utf-8") as file:
        schema = file.read()

    cursor.executescript(schema)

    conn.commit()
    conn.close()

    log_info("Database initialized successfully.")


def save_incident(incident):
    """
    Save an incident into the database.

    Args:
        incident (Incident): Incident object.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO incidents (
            attack,
            source_ip,
            severity,
            priority,
            risk_score,
            recommendation,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            incident.attack,
            incident.source_ip,
            incident.severity,
            incident.priority,
            incident.risk_score,
            incident.recommendation,
            incident.status,
        ),
    )

    conn.commit()
    conn.close()

    log_info(
        f"Incident saved successfully: "
        f"{incident.attack} ({incident.source_ip})"
    )

def get_all_incidents():
    """
    Retrieve all incidents from the database.

    Returns:
        list: All incident records.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            attack,
            source_ip,
            severity,
            priority,
            risk_score,
            recommendation,
            status
        FROM incidents
        ORDER BY id DESC
    """)

    incidents = cursor.fetchall()

    conn.close()

    log_info(f"Retrieved {len(incidents)} incidents from database.")

    return incidents

def get_attack_statistics():
    """
    Return number of incidents grouped by attack type.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT attack, COUNT(*)
        FROM incidents
        GROUP BY attack
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_severity_statistics():
    """
    Return number of incidents grouped by severity.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT severity, COUNT(*)
        FROM incidents
        GROUP BY severity
    """)

    data = cursor.fetchall()

    conn.close()

    return data

def get_dashboard_statistics():
    """
    Retrieve dashboard statistics.

    Returns:
        dict: Dashboard statistics.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # Total incidents
    cursor.execute("SELECT COUNT(*) FROM incidents")
    total_incidents = cursor.fetchone()[0]

    # Open incidents
    cursor.execute(
        "SELECT COUNT(*) FROM incidents WHERE status='Open'"
    )
    open_incidents = cursor.fetchone()[0]

    # High severity incidents
    cursor.execute(
        "SELECT COUNT(*) FROM incidents WHERE severity='High'"
    )
    high_severity = cursor.fetchone()[0]

    # Critical risk incidents
    cursor.execute(
        "SELECT COUNT(*) FROM incidents WHERE risk_score >= 90"
    )
    critical_risk = cursor.fetchone()[0]

    conn.close()

    return {
        "total_incidents": total_incidents,
        "open_incidents": open_incidents,
        "high_severity": high_severity,
        "critical_risk": critical_risk,
    }

def update_status(incident_id, new_status):
    """
    Update the status of an incident.

    Args:
        incident_id (int): Incident ID.
        new_status (str): New status.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE incidents
        SET status = ?
        WHERE id = ?
        """,
        (new_status, incident_id),
    )

    conn.commit()
    conn.close()

    log_info(
        f"Incident {incident_id} updated to '{new_status}'."
    )

def get_incident_by_id(incident_id):
    """
    Retrieve a single incident by ID.

    Args:
        incident_id (int): Incident ID.

    Returns:
        tuple | None
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            attack,
            source_ip,
            severity,
            priority,
            risk_score,
            recommendation,
            status
        FROM incidents
        WHERE id = ?
        """,
        (incident_id,),
    )

    incident = cursor.fetchone()

    conn.close()

    return incident

def delete_incident(incident_id):
    """
    Delete an incident.

    Args:
        incident_id (int): Incident ID.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM incidents
        WHERE id = ?
        """,
        (incident_id,),
    )

    conn.commit()
    conn.close()

    log_info(f"Incident {incident_id} deleted.")