from . import app
from . import database


@app.route("/")
def hello():
    players = database.hello_sql()
    return str(players)
