#!/bin/bash -x
python manage.py makemigrations --noinput || exit 1
python manage.py migrate --noinput || exit 1
exec "$@"