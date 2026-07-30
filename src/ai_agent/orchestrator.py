from collectors.log_collector import collect_all_logs
from detection.threat_detector import detect_brute_force

from ai_agent.classifier import classify_threats
from ai_agent.analyzer import analyze_threats
from ai_agent.responder import generate_response

from automation.response_actions import execute_response_actions
from automation.notifier import notify_soc_team

from database.models import Incident
from database.database import save_incident

from utils.logger import log_info


def run_ai_pipeline():
    """
    Execute the complete AI Incident Response pipeline.
    """

    log_info("========================================")
    log_info("Starting AI Incident Response Pipeline")
    log_info("========================================")

    # ---------------------------------------------------------
    # Step 1: Collect Logs
    # ---------------------------------------------------------
    logs = collect_all_logs()

    if not logs:
        log_info("No logs available.")
        return [], [], [], [], [], []

    # ---------------------------------------------------------
    # Step 2: Detect Threats
    # ---------------------------------------------------------
    threats = detect_brute_force(logs)

    # ---------------------------------------------------------
    # Step 3: Classify Threats
    # ---------------------------------------------------------
    classified_threats = classify_threats(threats)

    # ---------------------------------------------------------
    # Step 4: Analyze Threats
    # ---------------------------------------------------------
    analysis = analyze_threats(classified_threats)

    # ---------------------------------------------------------
    # Step 5: Save Incidents
    # ---------------------------------------------------------
    for item in analysis:

        incident = Incident(
            attack=item["Attack"],
            source_ip=item["Source_IP"],
            severity=item["Severity"],
            priority=item["Priority"],
            risk_score=item["Risk_Score"],
            recommendation=item["Recommendation"],
        )

        save_incident(incident)

    # ---------------------------------------------------------
    # Step 6: Generate Responses
    # ---------------------------------------------------------
    responses = generate_response(analysis)

    # ---------------------------------------------------------
    # Step 7: Execute Response Actions
    # ---------------------------------------------------------
    execution_results = execute_response_actions(responses)

    # ---------------------------------------------------------
    # Step 8: Notify SOC Team
    # ---------------------------------------------------------
    notifications = notify_soc_team(responses)

    log_info("========================================")
    log_info("AI Pipeline Completed Successfully")
    log_info("========================================")

    return (
        logs,
        classified_threats,
        analysis,
        responses,
        execution_results,
        notifications,
    )