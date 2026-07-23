"""
threat_detector.py

Threat Detection Module

Responsibilities:
- Detect brute-force login attacks
- Identify suspicious authentication activity

Author: Sakshi Burse
Project: AI Agent for Cybersecurity Incident Response
"""

from collections import defaultdict

from utils.logger import log_info


FAILED_LOGIN_THRESHOLD = 5


def detect_brute_force(logs):
    """
    Detect brute-force attacks based on failed login attempts.

    Args:
        logs (list): Authentication log records.

    Returns:
        list: Detected brute-force incidents.
    """

    log_info("Running brute-force detection...")

    failed_attempts = defaultdict(int)
    detected_threats = []

    for log in logs:

        if log["Status"] == "Failed":

            ip = log["Source_IP"]

            failed_attempts[ip] += 1

    for ip, attempts in failed_attempts.items():

        if attempts >= FAILED_LOGIN_THRESHOLD:

            detected_threats.append({
                "Attack": "Brute Force",
                "Source_IP": ip,
                "Failed_Attempts": attempts,
                "Severity": "High",
                "Recommendation": "Block IP and notify SOC analyst"
            })

    log_info(f"Threats Detected: {len(detected_threats)}")

    return detected_threats