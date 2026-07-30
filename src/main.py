from ai_agent.orchestrator import run_ai_pipeline
from utils.logger import log_info
from database.database import create_tables, get_all_incidents
from database.database import create_tables, get_all_incidents


def main():
    """Start the AI Incident Response application."""

    log_info("Launching AI Agent...")

    # ---------------------------------------------------------
    # Initialize Database
    # ---------------------------------------------------------
    create_tables()

    # ---------------------------------------------------------
    # Execute Complete AI Pipeline
    # ---------------------------------------------------------
    (
        logs,
        threats,
        analysis,
        responses,
        execution_results,
        notifications
    ) = run_ai_pipeline()

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

            # -------------------------------------------------
            # Recommended Actions
            # -------------------------------------------------
            print("\nRecommended Actions:")

            for action in response["Actions"]:
                print(f"  • {action}")

            # -------------------------------------------------
            # Response Action Execution
            # -------------------------------------------------
            execution = execution_results[index - 1]

            print("\nResponse Action Execution")
            print("-----------------------------------------------")
            print(f"Execution Status : {execution['Execution_Status']}")

            print("\nExecuted Actions:")

            for action in execution["Executed_Actions"]:
                print(f"  ✔ {action['Action']} ({action['Status']})")

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

            # -------------------------------------------------
            # SOC Notification
            # -------------------------------------------------
            notification = notifications[index - 1]

            print("\nSOC Notification")
            print("-----------------------------------------------")
            print(f"Recipient : {notification['Recipient']}")
            print(f"Channel   : {notification['Channel']}")
            print(f"Status    : {notification['Status']}")

            print("\n===============================================")

    else:
        print("\nNo incident responses generated.")

    log_info("Application finished successfully.")

    # ---------------------------------------------------------
    # Saved Incidents
    # ---------------------------------------------------------
    incidents = get_all_incidents()

    print("\n============== Saved Incidents ==============")

    if incidents:

        for incident in incidents:

            print("-----------------------------------------------")
            print(f"Incident ID    : {incident[0]}")
            print(f"Attack         : {incident[1]}")
            print(f"Source IP      : {incident[2]}")
            print(f"Severity       : {incident[3]}")
            print(f"Priority       : {incident[4]}")
            print(f"Risk Score     : {incident[5]}")
            print(f"Recommendation : {incident[6]}")
            print(f"Status         : {incident[7]}")

        print("=============================================")

    else:
        print("\nNo incidents found in the database.")

if __name__ == "__main__":
    main()