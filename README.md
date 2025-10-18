# Sweet Life Django

## Run (local)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Deploy (Render)
- Set env: DJANGO_SECRET_KEY, DJANGO_DEBUG=False
- Build: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
- Start: gunicorn <project_package>.wsgi
