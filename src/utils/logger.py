from datetime import datetime


def log_info(message):
    print(f"[INFO] {datetime.now():%Y-%m-%d %H:%M:%S} - {message}")


def log_error(message):
    print(f"[ERROR] {datetime.now():%Y-%m-%d %H:%M:%S} - {message}")