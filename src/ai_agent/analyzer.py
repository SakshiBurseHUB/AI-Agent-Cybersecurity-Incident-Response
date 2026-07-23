"""
analyzer.py

AI Threat Analyzer

Responsibilities:
- Analyze detected threats
- Assess risk level
- Generate AI security insights

Author: Sakshi Burse
Project: AI Agent for Cybersecurity Incident Response
"""

from datetime import datetime

from utils.logger import log_info


def analyze_threats(threats):
    """
    Analyze detected threats and generate AI insights.

    Args:
        threats (list): List of detected threats.

    Returns:
        list: AI analysis results.
    """

    log_info("Analyzing detected threats...")

    analysis_results = []

    for threat in threats:

        attack = threat["Attack"]
        severity = threat["Severity"]
        ip = threat["Source_IP"]

        if severity == "High":
            risk_score = 90
            priority = "Immediate"
        elif severity == "Medium":
            risk_score = 60
            priority = "High"
        else:
            risk_score = 30
            priority = "Normal"

        analysis = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Attack": attack,
            "Source_IP": ip,
            "Severity": severity,
            "Risk_Score": risk_score,
            "Priority": priority,
            "Summary": (
                f"Detected a {attack} attack from {ip}. "
                f"Risk Score: {risk_score}/100."
            ),
            "Recommendation": threat["Recommendation"]
        }

        analysis_results.append(analysis)

    log_info(f"AI analyzed {len(analysis_results)} threats.")

    return analysis_results