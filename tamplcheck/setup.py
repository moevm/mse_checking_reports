"""Модуль автоматической установки нужных пакетов проекта"""
from setuptools import setup

setup(
    name = "tamplcheck",
    packages = ["project"],
    include_package_data = True,
    install_requires = [
        "Flask==2.3.2",
        "Flask-Script==2.0.6",
        "Flask-WTF==0.14.2",
        "WTForms==2.2.1",
        "python-docx==0.8.10"
    ]
)