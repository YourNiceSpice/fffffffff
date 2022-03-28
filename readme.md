Настройка клиентской части:

1.pip freeze -r requirements.txt
 
 cd ~/client
2. pip install --editable .

3. старт клиента repo --help


Настройка сервера:

1.cd ~/chat 
2.python manage.py makemigrations
3.python manage.py migrate
4.python manage.py runserver
5.в файл ~/client/.env добавить ip/port хоста, по умолчанию установлен localhost
