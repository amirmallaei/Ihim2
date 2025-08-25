python manage.py makemigrations user books carts &&
python manage.py migrate user books carts &&
celery -A config.celery worker -l INFO -B & 
python manage.py runserver 0.0.0.0:8000