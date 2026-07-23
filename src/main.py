from collectors.log_collector import collect_all_logs
from detection.threat_detector import detect_brute_force
from utils.logger import log_info


def main():

    log_info("Starting AI Agent...")

    logs = collect_all_logs()

    threats = detect_brute_force(logs)

    print("\n========== AI Detection Summary ==========")
    print(f"Total Logs Loaded : {len(logs)}")
    print(f"Threats Detected  : {len(threats)}")

    if threats:
        print("\nDetected Threats:")
        for threat in threats:
            print("----------------------------------------")
            print(f"Attack Type      : {threat['Attack']}")
            print(f"Source IP        : {threat['Source_IP']}")
            print(f"Failed Attempts  : {threat['Failed_Attempts']}")
            print(f"Severity         : {threat['Severity']}")
            print(f"Recommendation   : {threat['Recommendation']}")

    else:
        print("No threats detected.")

    print("===========================================")


if __name__ == "__main__":
    main()