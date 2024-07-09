from __future__ import absolute_import

from celery import Celery


app = Celery('task_server')


@app.task(bind=True)
def debug_task(self):
    print(f"Request : {self.request}")

