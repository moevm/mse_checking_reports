# coding=utf-8
"""Модуль обработки запросов к серверу"""
import os
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
import subprocess


@app.route("/")
@app.route("/index")
def index():
    """ отрисовка стартовой страницы

    :return: шаблон страницы """
    #test_compare()
    #test_analysis()
    return render_template("index.html", title='Home')


@app.route("/index/result", methods=['POST'])
def get_result():
    """ обработка результата сравнения 2 файлов

    :return: ответ на запрос, либо успех, либо список несоответсвий при сравнении """
    if request.method == 'POST':
        req = request.data.decode('utf-8')
        res = re.findall(r'\b\w+\.[pdor]\w+\b', req)
        print(res)
        first = subprocess.Popen([
            '/usr/bin/soffice',
            '--headless',
            '--convert-to',
            'docx',
            '--outdir',
            os.path.abspath(os.path.dirname(res[0])),
            os.path.abspath(res[0])
        ])
        first.wait()
        second = subprocess.Popen([
            '/usr/bin/soffice',
            '--headless',
            '--convert-to',
            'docx',
            '--outdir',
            os.path.abspath(os.path.dirname(res[1])),
            os.path.abspath(res[1])
        ])
        second.wait()
        converted_base = "{}.docx".format(res[0].split(".")[0])
        converted_template = "{}.docx".format(res[0].split(".")[0])
        base_format = analysis_doc(converted_base)
        templ_format = analysis_doc(converted_template)
        response = comparison_algorithm(base_format, templ_format)
        if not response:
            return 'base file and template are equal', 200
        else:
            return str(response), 200


    else:
        return 'get request', 200
