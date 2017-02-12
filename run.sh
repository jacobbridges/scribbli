#!/bin/sh
/usr/bin/python3 manage.py migrate
/usr/bin/python3 manage.py collectstatic --noinput
/usr/bin/supervisord