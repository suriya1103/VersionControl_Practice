import os
from flask import Flask, render_template, request 

app = Flask(__name__)   #Creating an instance of the Flask class.

@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True)