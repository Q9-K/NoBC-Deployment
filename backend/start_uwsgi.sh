#!/bin/bash
#python manage.py makemigrations \ &&
#python manage.py migrate \ &&
uwsgi --ini /code/uwsgi/uwsgi.ini
tail -f /dev/null