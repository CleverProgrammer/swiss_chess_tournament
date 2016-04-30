from flask import render_template

from . import app
from . import database


@app.route("/")
def hello():
    # players = database.hello_sql()
    return render_template("index.html", players=database.hello_sql())
