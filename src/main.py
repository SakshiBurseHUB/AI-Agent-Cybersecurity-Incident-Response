"""
main.py

Entry point for the AI Agent for Cybersecurity Incident Response.

Author: Sakshi Burse
Project: AI Agent for Cybersecurity Incident Response
"""

from collectors.log_collector import collect_all_logs
from detection.threat_detector import detect_brute_force
from ai_agent.analyzer import analyze_threats
from utils.logger import log_info


def main():
    """
    Main application workflow.
    """

    log_info("Starting AI Agent for Cybersecurity Incident Response...")

    # ------------------------------------------------------------
    # Step 1: Collect Logs
    # ------------------------------------------------------------
    logs = collect_all_logs()

    if not logs:
        print("\nNo logs were collected.")
        return

    # ------------------------------------------------------------
    # Step 2: Detect Threats
    # ------------------------------------------------------------
    threats = detect_brute_force(logs)

    # ------------------------------------------------------------
    # Step 3: AI Analysis
    # ------------------------------------------------------------
    analysis = analyze_threats(threats)

    # ------------------------------------------------------------
    # Step 4: Detection Summary
    # ------------------------------------------------------------
    print("\n========== AI Detection Summary ==========")
    print(f"Total Logs Loaded : {len(logs)}")
    print(f"Threats Detected  : {len(threats)}")
    print("==========================================")

    # ------------------------------------------------------------
    # Step 5: AI Analysis Report
    # ------------------------------------------------------------
    if analysis:

        print("\n============== AI Analysis Report ==============")

        for index, item in enumerate(analysis, start=1):

            print(f"\nThreat #{index}")
            print("-----------------------------------------------")
            print(f"Attack Type     : {item['Attack']}")
            print(f"Source IP       : {item['Source_IP']}")
            print(f"Severity        : {item['Severity']}")
            print(f"Risk Score      : {item['Risk_Score']}/100")
            print(f"Priority        : {item['Priority']}")
            print(f"Summary         : {item['Summary']}")
            print(f"Recommendation  : {item['Recommendation']}")

        print("\n===============================================")

    else:
        print("\nNo threats detected. System appears secure.")

    log_info("AI Agent execution completed.")


if __name__ == "__main__":
    main()