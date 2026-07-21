import sqlite3
import os

from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

app = Flask(__name__)

def get_db():
    db = sqlite3.connect(DB_URL)
    db.row_factory = sqlite3.Row
    return db

@app.route("/", methods=['GET'])
def home():
    return render_template("base.html")


@app.route("/texto", methods=['GET'])
def text():
    return "hola con todos"

@app.route("/posts", methods=['GET'])
def list_posts():
    connection = get_db()
    posts_data = connection.execute("SELECT * FROM posts").fetchall()
    connection.close()
    return render_template("index.html", posts_list=posts_data)


@app.route("/api/posts", methods=['GET'])
def list_posts_json():
    connection = get_db()
    posts_data = connection.execute("SELECT * FROM posts").fetchall()
    connection.close()
    print("posts_data", posts_data)
    return jsonify(posts_data)
