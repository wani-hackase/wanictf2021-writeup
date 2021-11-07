cd /app
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
uwsgi --ini /etc/uwsgi/uwsgi.ini