#!/bin/bash
python3 manage.py makemigrations common
python3 manage.py migrate common

python3 manage.py migrate

python3 manage.py makemigrations laboratorium_app
python3 manage.py migrate laboratorium_app

python3 manage.py makemigrations przychodnia_app
python3 manage.py migrate przychodnia_app

python3 manage.py makemigrations przychodnia_pacjent
python3 manage.py migrate przychodnia_pacjent

python3 manage.py makemigrations przychodnia_wizyta
python3 manage.py migrate przychodnia_wizyta