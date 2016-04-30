from . import app
import psycopg2
import os


db_url = os.environ.get("DATABASE_URL", "dbname=tournament")
conn = psycopg2.connect(db_url)
def hello_sql():
    with conn, conn.cursor() as cur:
        cur.execute('select * from players')
        return cur.fetchall()
