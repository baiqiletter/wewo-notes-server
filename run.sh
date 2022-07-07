source env/bin/activate
nohup python manage.py runserver 0.0.0.0:8000 > log.txt 2>&1 &