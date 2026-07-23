"""
classifier.py

AI Threat Classifier

Responsibilities:
- Classify detected threats
- Assign attack category
- Assign MITRE ATT&CK technique
- Return enriched threat information

Author: Sakshi Burse
Project: AI Agent for Cybersecurity Incident Response
"""

from utils.logger import log_info


def classify_threats(threats):
    """
    Classify detected threats.

    Args:
        threats (list): List of detected threats.

    Returns:
        list: Classified threats.
    """

    log_info("Classifying detected threats...")

    classified_threats = []

    for threat in threats:

        attack = threat["Attack"]

        if attack == "Brute Force":

            threat["Category"] = "Credential Access"

            threat["MITRE_ID"] = "T1110"

            threat["MITRE_Name"] = "Brute Force"

        elif attack == "SQL Injection":

            threat["Category"] = "Initial Access"

            threat["MITRE_ID"] = "T1190"

            threat["MITRE_Name"] = "Exploit Public-Facing Application"

        elif attack == "Malware":

            threat["Category"] = "Execution"

            threat["MITRE_ID"] = "T1204"

            threat["MITRE_Name"] = "User Execution"

        elif attack == "DDoS":

            threat["Category"] = "Impact"

            threat["MITRE_ID"] = "T1498"

            threat["MITRE_Name"] = "Network Denial of Service"

        else:

            threat["Category"] = "Unknown"

            threat["MITRE_ID"] = "N/A"

            threat["MITRE_Name"] = "Unknown"

        classified_threats.append(threat)

    log_info(f"Classified {len(classified_threats)} threats.")

    return classified_threats