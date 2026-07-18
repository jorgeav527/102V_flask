import sqlite3
import os

from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

app = Flask(__name__)

def get_db():
    db = sqlite3.connect(DB_URL)
    db.row_factory = sqlite3.Row
    return db


@app.route("/")
def hello_world():
    return render_template("index.html")