import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'G8word.G8word.settings')

app = Celery('G8word')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# 測試用
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')