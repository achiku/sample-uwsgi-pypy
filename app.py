# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/hello")
def hello():
    return "Hello PyPy + uWSGI"


if __name__ == "__main__":
    app.run()
