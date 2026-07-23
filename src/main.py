"""
main.py

Entry point for the AI Agent for Cybersecurity Incident Response.

Author: Sakshi Burse
Project: AI Agent for Cybersecurity Incident Response
"""

from ai_agent.orchestrator import run_ai_pipeline
from utils.logger import log_info


def main():
    """Start the AI Incident Response application."""

    log_info("Launching AI Agent...")

    # ---------------------------------------------------------
    # Execute Complete AI Pipeline
    # ---------------------------------------------------------
    logs, threats, analysis, responses = run_ai_pipeline()

    if not logs:
        print("\nNo logs found.")
        return

    # ---------------------------------------------------------
    # Detection Summary
    # ---------------------------------------------------------
    print("\n========== AI Detection Summary ==========")
    print(f"Total Logs Loaded : {len(logs)}")
    print(f"Threats Detected  : {len(threats)}")
    print("==========================================")

    # ---------------------------------------------------------
    # AI Analysis Report
    # ---------------------------------------------------------
    if analysis:

        print("\n============== AI Analysis Report ==============")

        for index, item in enumerate(analysis, start=1):

            print(f"\nThreat #{index}")
            print("-----------------------------------------------")
            print(f"Attack Type     : {item['Attack']}")
            print(f"Category        : {item['Category']}")
            print(f"MITRE ATT&CK ID : {item['MITRE_ID']}")
            print(f"MITRE Technique : {item['MITRE_Name']}")
            print(f"Source IP       : {item['Source_IP']}")
            print(f"Severity        : {item['Severity']}")
            print(f"Risk Score      : {item['Risk_Score']}/100")
            print(f"Priority        : {item['Priority']}")
            print(f"Summary         : {item['Summary']}")
            print(f"Recommendation  : {item['Recommendation']}")

        print("\n===============================================")

    else:
        print("\nNo threats detected.")

    # ---------------------------------------------------------
    # Incident Response
    # ---------------------------------------------------------
    if responses:

        print("\n============== Incident Response ==============")

        for index, response in enumerate(responses, start=1):

            print(f"\nIncident #{index}")
            print("-----------------------------------------------")
            print(f"Attack Type     : {response['Attack']}")
            print(f"Source IP       : {response['Source_IP']}")
            print(f"Severity        : {response['Severity']}")
            print(f"Priority        : {response['Priority']}")
            print(f"Response Time   : {response['Response_Time']}")

            print("\nRecommended Actions:")

            for action in response["Actions"]:
                print(f"  • {action}")

            # -------------------------------------------------
            # SOC Playbook
            # -------------------------------------------------
            playbook = response["Playbook"]

            print("\nSOC Playbook")
            print("-----------------------------------------------")
            print(f"Playbook ID : {playbook['Playbook']}")
            print(f"Title       : {playbook['Title']}")

            print("\nContainment")
            for step in playbook["Containment"]:
                print(f"  • {step}")

            print("\nInvestigation")
            for step in playbook["Investigation"]:
                print(f"  • {step}")

            print("\nRecovery")
            for step in playbook["Recovery"]:
                print(f"  • {step}")

        print("\n===============================================")

    else:
        print("\nNo incident responses generated.")

    log_info("Application finished successfully.")


if __name__ == "__main__":
    main()