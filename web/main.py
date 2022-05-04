import os

import requests
from flask import Flask, render_template

app = Flask(__name__)

BACKEND_HOST = os.environ.get("BACKEND_HOST", "http://127.0.0.1:8000")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_users/", methods=["GET"])
def get_users():
    response = requests.get(os.path.join(BACKEND_HOST, "test_users"))
    return render_template("index.html", response=response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
