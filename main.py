import os

from flask import Flask, render_template, redirect, url_for, request, session

import datetime

from helper import add_post, generate_post_id
from markupsafe import escape

#flask --app main run --debug

app = Flask(__name__)

app.secret_key = os.urandom(16)

@app.route("/")
def home():
    return redirect(url_for('login'))

@app.get("/login")
def login():
    return render_template("login.html")

@app.post("/login")
def login_post():
    name = request.form["name"]
    if not name:
        return render_template("login.html", error=True)
    session["user"] = name
    return redirect(url_for("dashboard"))

@app.get("/dashboard")
def dashboard():
    username = session.get("user", None)
    blog_posts = session.get("blog_posts", [])
    return render_template("dashboard.html", username=username, blog_posts=blog_posts)

@app.post("/dashboard")
def dashboard_post():
    date_created = datetime.datetime.now()
    
    new_post = {
        "title": request.form["title"],
        "post": request.form["post"],
        "author": session.get("user", "Unknown"),
        "id": generate_post_id(),
        "created_at": date_created.strftime("%d/%m/%Y - %H:%M:%S")
    }
    add_post(new_post)
    return redirect(url_for("dashboard"))
