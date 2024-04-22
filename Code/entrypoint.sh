#!/bin/ash

echo "Changing directory"
cd plant-pals

echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate --run-syncdb

echo "Starting server"
python manage.py runserver 0.0.0.0:80

exec "$@"

