from flask import Flask


app = Flask(__name__)
app.config.from_object(__name__)

import project.views


if __name__ == '__main__':
    app.run(debug=True, host="localhost")
