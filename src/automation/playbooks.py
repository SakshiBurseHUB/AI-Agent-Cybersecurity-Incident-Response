"""
playbooks.py

SOC Incident Response Playbooks

Responsibilities:
- Map attacks to standard response playbooks
- Provide investigation steps
- Provide containment and recovery guidance

Author: Sakshi Burse
Project: AI Agent for Cybersecurity Incident Response
"""

from utils.logger import log_info


PLAYBOOKS = {

    "Brute Force": {
        "Playbook": "PB-001",
        "Title": "Brute Force Login Attack",

        "Containment": [
            "Block the attacker's IP address",
            "Lock the affected account",
            "Enable multi-factor authentication"
        ],

        "Investigation": [
            "Review authentication logs",
            "Identify affected user accounts",
            "Check for successful logins after failed attempts"
        ],

        "Recovery": [
            "Reset compromised passwords",
            "Monitor login activity",
            "Remove temporary account lock if safe"
        ]
    },

    "SQL Injection": {
        "Playbook": "PB-002",
        "Title": "SQL Injection Attack",

        "Containment": [
            "Block malicious requests",
            "Enable WAF rules",
            "Restrict database access"
        ],

        "Investigation": [
            "Review web server logs",
            "Check database queries",
            "Identify exploited endpoints"
        ],

        "Recovery": [
            "Patch the vulnerable application",
            "Restore affected data",
            "Verify application security"
        ]
    },

    "Malware": {
        "Playbook": "PB-003",
        "Title": "Malware Infection",

        "Containment": [
            "Isolate affected host",
            "Disconnect from network"
        ],

        "Investigation": [
            "Identify malware type",
            "Scan all affected systems"
        ],

        "Recovery": [
            "Remove malware",
            "Restore clean backup"
        ]
    },

    "DDoS": {
        "Playbook": "PB-004",
        "Title": "Distributed Denial of Service",

        "Containment": [
            "Enable DDoS protection",
            "Rate-limit suspicious traffic"
        ],

        "Investigation": [
            "Analyze traffic patterns",
            "Identify attack sources"
        ],

        "Recovery": [
            "Restore normal traffic",
            "Continue monitoring"
        ]
    }
}


def get_playbook(attack_type):
    """
    Return the SOC playbook for a given attack.

    Args:
        attack_type (str): Attack type.

    Returns:
        dict: Playbook details.
    """

    log_info(f"Loading playbook for {attack_type}")

    return PLAYBOOKS.get(
        attack_type,
        {
            "Playbook": "PB-000",
            "Title": "Unknown Threat",
            "Containment": [],
            "Investigation": [],
            "Recovery": []
        }
    )