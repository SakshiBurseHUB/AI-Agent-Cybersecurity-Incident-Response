import sys
from pathlib import Path

# ---------------------------------------------------------
# Add the src folder to the Python path
# ---------------------------------------------------------
SRC_DIR = Path(__file__).resolve().parent.parent

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from flask import Flask, render_template

from database.database import (
    create_tables,
    get_dashboard_statistics,
    get_all_incidents,
    get_attack_statistics,
    get_severity_statistics,
)

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
)

# ---------------------------------------------------------
# Initialize Database
# ---------------------------------------------------------
create_tables()


# ---------------------------------------------------------
# Dashboard
# ---------------------------------------------------------
@app.route("/")
def home():

    stats = get_dashboard_statistics()

    incidents = get_all_incidents()

    attack_stats = get_attack_statistics()

    severity_stats = get_severity_statistics()

    return render_template(

        "dashboard.html",

        stats=stats,

        incidents=incidents,

        attack_stats=attack_stats,

        severity_stats=severity_stats,

    )


# ---------------------------------------------------------
# Incidents Page
# ---------------------------------------------------------
@app.route("/incidents")
def incidents():

    incidents = get_all_incidents()

    return render_template(
        "incidents.html",
        incidents=incidents,
    )


# ---------------------------------------------------------
# Reports Page
# ---------------------------------------------------------
@app.route("/reports")
def reports():

    return render_template("reports.html")


# ---------------------------------------------------------
# Settings Page
# ---------------------------------------------------------
@app.route("/settings")
def settings():

    return render_template("settings.html")


# ---------------------------------------------------------
# Login Page
# ---------------------------------------------------------
@app.route("/login")
def login():

    return render_template("login.html")


# ---------------------------------------------------------
# Run Application
# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
    )