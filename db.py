import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def get_connection():  #opens a connection to the jobfit database i made, using the password from .env, the same pattern as Gemini key.
    return psycopg.connect(
        dbname="jobfit",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        port=5432,
    )

def get_jobs():
    with get_connection() as conn:
        with conn.cursor() as cur:    #A cursor is the object that sends SQL and collects results.
            cur.execute("SELECT id , title , company FROM jobs")  #runs the same SELECT , typed in psql
            return cur.fetchall()    # fetchall() returns every row as a list of tuples

def save_job(title, company, job_text, gaps=None):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO jobs (title, company, job_text, gaps) VALUES(%s,%s,%s,%s)",
                (title,company, job_text,gaps),
            )

