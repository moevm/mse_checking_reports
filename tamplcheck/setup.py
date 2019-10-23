from setuptools import setup

setup(
    name = "tamplcheck",
    packages = ["project"],
    include_package_data = True,
    install_requires = [
        "Flask==1.1.1",
        "Flask-Script==2.0.6",
        "Flask-WTF==0.14.2",
        "WTForms==2.2.1"
    ]
)