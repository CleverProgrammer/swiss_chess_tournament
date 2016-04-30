#!/usr/bin/env python
# Author: Rafeh Qazi
# tournament.py -- implementation of a Swiss-system tournament

from . import app
import psycopg2
import os


db_url = os.environ.get("DATABASE_URL", "dbname=tournament")
conn = psycopg2.connect(db_url)

def hello_sql():
    with conn, conn.cursor() as cur:
        cur.execute('select * from players')
        return cur.fetchall()

def all_matches():
    with conn, conn.cursor() as cur:
        cur.execute('select * from matches')
        return cur.fetchall()

def deleteMatches():
    """Remove all the match records from the database."""
    with conn, conn.cursor() as cur:
        cur.execute("DELETE FROM matches;")

def deletePlayers():
    """Remove all the player records from the database."""
    with conn, conn.cursor() as cur:
        cur.execute("DELETE FROM players;")


def countPlayers():
    """Returns the number of players currently registered."""
    with conn, conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) as num FROM players;")
        return cur.fetchone()[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    with conn, conn.cursor() as cur:
        cur.execute("INSERT INTO players (full_name) VALUES (%s)", (name,))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    with conn, conn.cursor() as cur:
        cur.execute('SELECT * FROM standings;')
        return cur.fetchall()

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
      Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    with conn, conn.cursor() as cur:
        cur.execute('insert into matches(winner_id, loser_id) values(%s, %s)', (winner, loser))


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings. Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pass
    # conn = connect()
    # c = conn.cursor()
    # c.execute('select * from final_standings;')
    # return [pair1 + pair2 for pair1, pair2 in zip(c, c)]
