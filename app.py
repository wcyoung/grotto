import json
import os

from flask import Flask

app = Flask(__name__)

with open("config.json") as json_file:
    CONFIG_DATA = json.load(json_file)


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
