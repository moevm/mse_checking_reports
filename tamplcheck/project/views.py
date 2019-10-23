from flask import render_template, request, jsonify
from project import app
from project.module.cmpFiles import analysis_doc


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title='Home')


@app.route("/index/result", methods=['GET', 'POST'])
def get_result():
    if request.method == 'POST':
        msg = {'resp': analysis_doc(request.get_data())}
        print(request.get_data())
        return analysis_doc(request.get_data())
    else:
        return 'get request', 200
