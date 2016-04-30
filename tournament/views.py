from flask import render_template, request, redirect, url_for
from . import app
from . import database


@app.route("/")
def hello():
    # players = database.hello_sql()
    return render_template('index.html',
                           matches=database.all_matches(), players=database.hello_sql())
    # return render_template("index.html", players=database.hello_sql())

@app.route("/addplayer", methods=["GET"])
def addplayer_get():
    return render_template("add_player.html")

@app.route("/addplayer", methods=["POST"])
def addplayer_post():
    winner = request.form["winner_id"]
    loser = request.form["loser_id"]
    database.reportMatch(winner, loser)
    # database.registerPlayer(player)
    return redirect(url_for("hello"))

