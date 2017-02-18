#!/bin/sh
until nc -z postgres 5432; do
    echo "$(date) - waiting for postgres..."
    sleep 1
done
/usr/bin/python3 manage.py makemigrations
/usr/bin/python3 manage.py migrate
/usr/bin/python3 manage.py collectstatic --noinput
/usr/bin/supervisord