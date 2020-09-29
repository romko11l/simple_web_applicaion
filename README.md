Гайд по установке и запуску:
1. Клонируйте репозиторий (git clone https://github.com/romko11l/simple_web_applicaion)
2. Создайте и запустите виртуальное окружение (virtualenv venv и source ./venv/bin/activate)
3. Установите зависимости из файлика requirements.txt (pip install requiremenst.txt).
Если pip ругается, то установите руками нужную версию Django (pip install Django==3.1.1)
4. Проведите миграции (python ./manage.py makemigrations) - в папке должна появиться бд bd.sqlite3
5. Заполните БД с файлом инициализации
6. Запустите приложение (python ./manage.py runserver)
7. Откройте в браузере ссылку, которую отдал django
