

import os

from celery import Celery, Task
from django.db import connection


# Set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings.local')

app=Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

"""class DBTask(Task):
    abstract=True
    
    Custom Celery Task that ensures the database connection is closed
    after the task is executed.
    
    def after_return(self, status, retval=None, task_id=None, args=None, kwargs=None, einfo=None):
        # Close the database connection to prevent leaks
        if connection.is_usable():
            connection.close()
        print(f"DEBUG : TASK {task_id} completed.")

app.Task = DBTask"""