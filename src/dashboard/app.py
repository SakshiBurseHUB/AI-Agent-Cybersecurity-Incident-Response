import sys
from pathlib import Path

# ---------------------------------------------------------
# Add the src folder to the Python path
# ---------------------------------------------------------
SRC_DIR = Path(__file__).resolve().parent.parent

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from flask import Flask, render_template

from database.database import create_tables, get_dashboard_statistics

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Create database tables
create_tables()


@app.route("/")
def home():
    """
    Dashboard Home Page
    """

    stats = get_dashboard_statistics()

    return render_template(
        "index.html",
        stats=stats
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )