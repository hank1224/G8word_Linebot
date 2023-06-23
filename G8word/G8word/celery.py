import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'G8word.settings')

app = Celery('G8word')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()