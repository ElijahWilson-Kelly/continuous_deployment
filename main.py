from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>My name is Fred</h1>"

@app.route("/contact")
def contact_page():
    return "<h1>Welcome to the contacts page</h1>"