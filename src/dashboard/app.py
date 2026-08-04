import sys
from pathlib import Path

# ---------------------------------------------------------
# Add the src folder to the Python path
# ---------------------------------------------------------
SRC_DIR = Path(__file__).resolve().parent.parent

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    flash,
    jsonify
)

from database.database import (
    create_tables,
    get_dashboard_statistics,
    get_all_incidents,
    get_attack_statistics,
    get_severity_statistics,
)

from ai_agent.orchestrator import run_ai_pipeline

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
)

app.secret_key = "soc_dashboard_secret_key"

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
# Run AI Analysis
# ---------------------------------------------------------
@app.route("/run-analysis")
def run_analysis():

    try:

        run_ai_pipeline()

        return jsonify({

            "success": True,

            "message": "AI Pipeline completed successfully."

        })

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500

    # ---------------------------------------------------------
# Dashboard API
# ---------------------------------------------------------
@app.route("/dashboard-data")
def dashboard_data():

    stats = get_dashboard_statistics()

    attack_stats = get_attack_statistics()

    severity_stats = get_severity_statistics()

    incidents = get_all_incidents()

    return jsonify({

        "stats": stats,

        "attack_stats": attack_stats,

        "severity_stats": severity_stats,

        "incidents": incidents

    })

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