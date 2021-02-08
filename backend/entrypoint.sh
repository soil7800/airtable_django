#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Update db from airtable
echo "Update db from airtable"
python manage.py update_db

echo "Run gunicorn"
gunicorn --bind 0.0.0.0:8000 meta.wsgi