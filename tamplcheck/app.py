from __future__ import print_function
from flask import Flask, render_template
from flask import request, jsonify

import os


app = Flask(__name__)
app.secret_key = 'key'
app.debug = True
app._static_folder = os.path.abspath("templates/static/")


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)