import json
import os

from flask import abort
from flask import Flask

app = Flask(__name__)

with open("config.json") as json_file:
    CONFIG = json.load(json_file)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/view/")
@app.route("/view/<path:path>")
def view(path=""):
    file_path = os.path.join(CONFIG["base_dir"], path)

    if not os.path.exists(file_path):
        abort(404)

    if os.path.isdir(file_path):
        return {
            "files": os.listdir(file_path)
        }
    else:
        return os.path.basename(file_path)


if __name__ == "__main__":
    app.run(debug=True)
