import csv
import random
from datetime import datetime, timedelta

OUTPUT_FILE = "datasets/authentication_logs.csv"

users = [
    "admin", "john", "alice", "bob", "sarah",
    "mike", "emma", "david", "guest", "root"
]

normal_ips = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30",
    "192.168.1.40",
    "192.168.1.50",
    "192.168.1.60",
    "192.168.1.70",
    "192.168.1.80"
]

start_time = datetime(2026, 7, 23, 9, 0, 0)

rows = []

# 70 Normal Login Events
for i in range(70):
    rows.append([
        (start_time + timedelta(minutes=i)).strftime("%Y-%m-%d %H:%M:%S"),
        random.choice(users),
        random.choice(normal_ips),
        "Success",
        0,
        "Login"
    ])

# 20 Failed Login Events
for i in range(20):
    rows.append([
        (start_time + timedelta(minutes=70 + i)).strftime("%Y-%m-%d %H:%M:%S"),
        random.choice(users),
        f"203.0.113.{random.randint(1,20)}",
        "Failed",
        random.randint(1,4),
        "Login"
    ])

# 10 Brute Force Events
attacker_ip = "203.0.113.99"

for attempt in range(1,11):
    rows.append([
        (start_time + timedelta(minutes=90 + attempt)).strftime("%Y-%m-%d %H:%M:%S"),
        "admin",
        attacker_ip,
        "Failed",
        attempt,
        "Login"
    ])

rows.sort(key=lambda x: x[0])

with open(OUTPUT_FILE, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Timestamp",
        "Username",
        "Source_IP",
        "Status",
        "Failed_Attempts",
        "Event"
    ])

    writer.writerows(rows)

print(f"Generated {len(rows)} authentication logs.")
print(f"Saved to {OUTPUT_FILE}")