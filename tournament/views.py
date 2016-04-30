from flask import render_template, request, redirect, url_for
from . import app
from . import database


@app.route("/")
def hello():
    # players = database.hello_sql()
    return render_template('index.html',
                           matches=database.all_matches(),
                           players=database.hello_sql(),
                           count=database.countPlayers())
    # return render_template("index.html", players=database.hello_sql())


# @app.route("/addplayer", methods=["GET"])
# def addplayer_get():
    # return render_template("add_player.html")


@app.route("/addplayer", methods=["POST"])
def addplayer_post():
    player = request.form['player']
    # winner = request.form["winner_id"]
    # loser = request.form["loser_id"]
    # database.reportMatch(winner, loser)
    database.registerPlayer(player)
    return redirect(url_for("hello"))


@app.route('/query', methods=['POST'])
def query_result():
    # query = request.form['Total Player Count']
    return render_template('query.html', query=database.countPlayers())


@app.route('/delete', methods=['POST'])
def remove_players():
    database.deletePlayers()
    return redirect(url_for('hello'))
