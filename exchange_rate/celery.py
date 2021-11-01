from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from exchange_task.tasks import store_exchange_info
# Default Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchange_rate.settings')

app = Celery('exchange_rate')

# Using a string here eliminates the need to serialize
# the configuration object to child processes by the Celery worker.

# - namespace='CELERY' means all celery-related configuration keys
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django applications.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task(name="task_store_exchange_info")
def task_store_exchange_info():
    store_exchange_info()


app.conf.beat_schedule = {
    # Execute the Speed Test every 60 minutes
    'store_exchange_info-60min': {
        'task': "task_store_exchange_info",
        'schedule': crontab(minute='*/1'),
    },
}
