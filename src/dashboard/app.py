from flask import Flask, render_template

from database.database import (
    create_tables,
    get_dashboard_statistics,
)

app = Flask(__name__)

create_tables()


@app.route("/")
def home():

    stats = get_dashboard_statistics()

    return render_template(
        "index.html",
        stats=stats,
    )


if __name__ == "__main__":
    app.run(debug=True)