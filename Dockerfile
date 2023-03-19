from python:3.11.2-slim-buster
env PYTHONBUFFERD 1

WORKDIR /app
run pip install django
run pip install djangorestframework
COPY . /app/

cmd python control_stock/manage.py runserver 0.0.0.0:8000