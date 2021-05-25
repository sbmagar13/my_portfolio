#!/bin/sh

set -e # exit if errors happen anywhere
python manage.py migrate
python manage.py collectstatic --no-input --clear

uwsgi --socket :8000 --master --enable-threads --module personal.wsgi
