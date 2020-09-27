import json
import os

from flask import abort
from flask import Flask

from utils import get_file_info

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

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
        file_info_list = []

        file_name_list = os.listdir(file_path)
        for file_name in file_name_list:
            file_info = get_file_info(os.path.join(file_path, file_name))
            file_info_list.append(file_info)

        return {
            "files": file_info_list
        }
    else:
        return get_file_info(file_path)


if __name__ == "__main__":
    app.run(debug=True)
