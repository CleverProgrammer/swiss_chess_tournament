from . import app
import psycopg2


conn = psycopg2.connect('dbname=tournament')
def hello_sql():
    with conn, conn.cursor() as cur:
        cur.execute('select * from players')
        return cur.fetchall()
