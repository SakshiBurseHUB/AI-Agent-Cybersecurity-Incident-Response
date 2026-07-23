"""
orchestrator.py

AI Workflow Orchestrator

Responsibilities:
- Coordinate the complete AI workflow
- Collect logs
- Detect threats
- Classify threats
- Analyze threats
- Return final analysis

Author: Sakshi Burse
Project: AI Agent for Cybersecurity Incident Response
"""

from collectors.log_collector import collect_all_logs
from detection.threat_detector import detect_brute_force
from ai_agent.classifier import classify_threats
from ai_agent.analyzer import analyze_threats
from utils.logger import log_info


def run_ai_pipeline():
    """
    Execute the complete AI incident response workflow.

    Returns:
        tuple: (logs, threats, analysis)
    """

    log_info("Starting AI workflow...")

    logs = collect_all_logs()

    if not logs:
        return [], [], []

    threats = detect_brute_force(logs)

    classified_threats = classify_threats(threats)

    analysis = analyze_threats(classified_threats)

    log_info("AI workflow completed successfully.")

    return logs, classified_threats, analysis