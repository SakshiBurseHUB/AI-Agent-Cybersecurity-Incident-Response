"""
orchestrator.py

AI Workflow Orchestrator

Responsibilities:
- Coordinate the complete AI workflow
- Collect logs
- Detect threats
- Classify threats
- Analyze threats
- Generate incident responses
- Return final results

Author: Sakshi Burse
Project: AI Agent for Cybersecurity Incident Response
"""

from collectors.log_collector import collect_all_logs
from detection.threat_detector import detect_brute_force
from ai_agent.classifier import classify_threats
from ai_agent.analyzer import analyze_threats
from ai_agent.responder import generate_response
from utils.logger import log_info


def run_ai_pipeline():
    """
    Execute the complete AI Incident Response workflow.

    Returns:
        tuple:
            logs (list)
            threats (list)
            analysis (list)
            responses (list)
    """

    log_info("========================================")
    log_info("Starting AI Incident Response Pipeline")
    log_info("========================================")

    # ---------------------------------------------------------
    # Step 1 : Collect Logs
    # ---------------------------------------------------------
    logs = collect_all_logs()

    if not logs:
        log_info("No logs available for analysis.")
        return [], [], [], []

    # ---------------------------------------------------------
    # Step 2 : Detect Threats
    # ---------------------------------------------------------
    threats = detect_brute_force(logs)

    # ---------------------------------------------------------
    # Step 3 : Classify Threats
    # ---------------------------------------------------------
    classified_threats = classify_threats(threats)

    # ---------------------------------------------------------
    # Step 4 : Analyze Threats
    # ---------------------------------------------------------
    analysis = analyze_threats(classified_threats)

    # ---------------------------------------------------------
    # Step 5 : Generate Responses
    # ---------------------------------------------------------
    responses = generate_response(analysis)

    log_info("========================================")
    log_info("AI Pipeline Completed Successfully")
    log_info("========================================")

    return logs, classified_threats, analysis, responses