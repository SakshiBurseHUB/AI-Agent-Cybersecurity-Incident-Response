"""
log_collector.py

Central Log Collector

Responsibilities:
- Collect logs from all available collectors
- Merge logs into a single dataset
- Return all collected logs

Author: Sakshi Burse
Project: AI Agent for Cybersecurity Incident Response
"""

from collectors.auth_collector import load_authentication_logs
from utils.logger import log_info


def collect_all_logs():
    """
    Collect logs from all log sources.

    Returns:
        list: Combined security log records.
    """

    log_info("Starting log collection...")

    all_logs = []

    # Authentication Logs
    auth_logs = load_authentication_logs()

    if auth_logs:
        log_info(f"Authentication Logs : {len(auth_logs)} records")
        all_logs.extend(auth_logs)

    # --------------------------------------------------
    # Future Collectors
    # --------------------------------------------------
    # firewall_logs = load_firewall_logs()
    # windows_logs = load_windows_logs()
    # linux_logs = load_linux_logs()
    # web_logs = load_webserver_logs()
    #
    # all_logs.extend(firewall_logs)
    # all_logs.extend(windows_logs)
    # all_logs.extend(linux_logs)
    # all_logs.extend(web_logs)
    # --------------------------------------------------

    log_info(f"Total Logs Collected : {len(all_logs)}")

    return all_logs