"""
auth_collector.py

Authentication Log Collector

Responsibilities:
- Load authentication log dataset
- Validate required columns
- Return authentication log records

Author: Sakshi Burse
Project: AI Agent for Cybersecurity Incident Response
"""

import csv
from pathlib import Path

from utils.logger import log_info, log_error

# --------------------------------------------------------------------
# Dataset Configuration
# --------------------------------------------------------------------

DATASET_PATH = Path("datasets/authentication_logs.csv")

REQUIRED_COLUMNS = [
    "Timestamp",
    "Username",
    "Source_IP",
    "Status",
    "Failed_Attempts",
    "Event"
]


# --------------------------------------------------------------------
# Authentication Log Collector
# --------------------------------------------------------------------

def load_authentication_logs():
    """
    Load authentication logs from CSV file.

    Returns:
        list[dict]: List of authentication log records.
    """

    if not DATASET_PATH.exists():
        log_error(f"Dataset not found: {DATASET_PATH}")
        return []

    log_info("Loading authentication logs...")

    try:

        with open(DATASET_PATH, "r", encoding="utf-8") as csv_file:

            reader = csv.DictReader(csv_file)

            # Validate CSV columns
            if reader.fieldnames != REQUIRED_COLUMNS:
                log_error("Invalid authentication log format.")
                return []

            records = list(reader)

            log_info(f"{len(records)} authentication logs loaded successfully.")

            return records

    except Exception as error:
        log_error(f"Failed to load authentication logs: {error}")
        return []