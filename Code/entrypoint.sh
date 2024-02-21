#!/bin/ash

echo "Changing directory"
cd plant-pals

echo "Apply database migrations"
python manage.py migrate

echo "Starting server"
python manage.py runserver 0.0.0.0:8000

exec "$@"