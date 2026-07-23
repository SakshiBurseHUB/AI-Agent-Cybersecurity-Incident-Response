"""
main.py

Entry point for the AI Agent for Cybersecurity Incident Response.
"""

from collectors.log_collector import collect_all_logs
from utils.logger import log_info


def main():
    """Application entry point."""

    log_info("Starting AI Agent...")

    logs = collect_all_logs()

    print("\n===================================")
    print(" AI Agent Started Successfully")
    print("===================================")
    print(f"Total Logs Loaded : {len(logs)}")
    print("===================================\n")


if __name__ == "__main__":
    main()