from celery import shared_task
import time

@shared_task
def async_func():
    # 非同步操作
    print('start sleep')
    time.sleep(5)
    print('end sleep')
    return 'Hello, world!'