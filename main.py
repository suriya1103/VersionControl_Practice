import os
from flask import Flask, render_template, request 

app = Flask(__name__)   #Creating an instance of the Flask class.

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

app.run(debug=True)