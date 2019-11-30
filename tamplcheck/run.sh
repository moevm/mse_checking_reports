 #!/usr/bin/env bash

# имя корневой папки приложения
export FLASK_APP=project

# мод установки
export FLASK_ENV=development

export SERVER_NAME=localhost:5000

# установка проекта в виртуальном окружении
pip3 install -e .

# запуск приложения
flask run