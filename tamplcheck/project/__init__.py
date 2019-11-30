# coding=utf-8
"""Стартовая точка программы"""
from flask import Flask
"""Минимальная реализация сервера flask"""

app = Flask(__name__)
app.config.from_object(__name__)

import project.views


if __name__ == '__main__':
    """Главная функция"""
    app.run(debug=True, host="localhost")
