cd /app
pip install -r requirements.txt
playwright install chromium
python manage.py rqworker default