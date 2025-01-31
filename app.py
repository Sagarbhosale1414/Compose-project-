from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Database connection
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")

@app.route("/")
def hello():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        return "Connected to the database successfully!"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
