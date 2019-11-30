# coding=utf-8
"""Модуль обработки запросов к серверу"""
import re

from project.tests.cmptests import test_compare, test_analysis

"""обработка проверки имени файла с помощью регулярного выражения"""
from builtins import str
"""преобразование ответа к серверу в строку"""
from flask import render_template, request, jsonify
"""функции обработки html шаблона, get/post запросов и преобразование файла в json"""
from project import app
"""для работы с путями"""
from project.module.cmpFiles import comparison_algorithm, analysis_doc
"""нужны для вызова функций сопоставления алгоритмов"""


@app.route("/")
@app.route("/index")
def index():
    """ отрисовка стартовой страницы

    :return: шаблон страницы """
    test_compare()
    test_analysis()
    return render_template("index.html", title='Home')


@app.route("/index/result", methods=['POST'])
def get_result():
    """ обработка результата сравнения 2 файлов

    :return: ответ на запрос, либо успех, либо список несоответсвий при сравнении """
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
