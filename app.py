import json

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


def create_app():
    return app


def get_config():
    with open('config.json') as json_file:
        json_data = json.load(json_file)

    return json_data
