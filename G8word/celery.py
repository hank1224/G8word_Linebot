import os

from celery import Celery

import sys
from pathlib import Path

from .settings import CELERY_BROKER_URL

# BASE_DIR = Path(__file__).resolve().parent

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'G8word.settings')

# ！此處按啟動環境修改！
# 解決 Windows 環境下的問題，basically things become single threaded and are suppoted
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1') # 非windows請註解掉這行
# ！此處按啟動環境修改！

app = Celery('G8word', broker=CELERY_BROKER_URL)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')