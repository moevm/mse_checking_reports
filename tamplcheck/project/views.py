import json
import re
from builtins import range, str

from flask import render_template, request, jsonify
from project import app
from project.module.cmpFiles import comparison_algorithm, analysis_doc


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title='Home')


@app.route("/index/result", methods=['POST'])
def get_result():
    if request.method == 'POST':
        req = request.data.decode('utf-8')
        res = re.findall(r'\w+.docx', req)
        print(res)
        base_format = analysis_doc(res[0])
        templ_format = analysis_doc(res[1])
        response = comparison_algorithm(base_format, templ_format)
        if not response:
            return 'base file and template are equal', 200
        else:
            return str(response), 200


    else:
        return 'get request', 200
