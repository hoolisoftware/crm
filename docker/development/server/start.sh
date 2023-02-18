#! /bin/bash

python manage.py compilemessages -v 0
python manage.py migrate -v 0 --no-input
python manage.py ensure_admin --email admin@admin.com --password admin

exec python manage.py runserver 0.0.0.0:8000
