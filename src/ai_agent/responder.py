"""
responder.py

AI Incident Responder

Responsibilities:
- Generate response actions
- Assign response priority
- Recommend immediate actions

Author: Sakshi Burse
Project: AI Agent for Cybersecurity Incident Response
"""

from utils.logger import log_info
from automation.playbooks import get_playbook


def generate_response(analysis):
    """
    Generate response recommendations.

    Args:
        analysis (list): AI analysis results.

    Returns:
        list: Incident response recommendations.
    """

    log_info("Generating incident response recommendations...")

    responses = []

    for incident in analysis:

        severity = incident["Severity"]

        if severity == "High":

            actions = [
                "Block the source IP",
                "Disable affected user account",
                "Notify SOC analyst immediately",
                "Start forensic investigation"
            ]

            response_time = "Immediately"
            playbook = get_playbook(incident["Attack"])

        elif severity == "Medium":

            actions = [
                "Monitor suspicious activity",
                "Notify security team",
                "Review authentication logs"
            ]

            response_time = "Within 30 Minutes"

        else:

            actions = [
                "Log the incident",
                "Continue monitoring"
            ]

            response_time = "Normal"

        responses.append({
    "Attack": incident["Attack"],
    "Source_IP": incident["Source_IP"],
    "Severity": severity,
    "Priority": incident["Priority"],
    "Response_Time": response_time,
    "Actions": actions,
    "Playbook": playbook
})

    log_info(f"Generated {len(responses)} response plans.")

    return responses