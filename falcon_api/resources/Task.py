import json
import time
import numpy as np
from falcon_api.extensions.queue import huey


class Task:

    @staticmethod
    def on_get(req, resp):
        """
            Created a task and returns ID
        """
        task = make_task()
        print(task.id)
        resp.body = json.dumps(f'Created task with ID {task.id}')


class TaskStatus:

    @staticmethod
    def on_get(req, resp, id):
        """
            Created a task and returns ID
        """
        task = huey.get(id)
        resp.body = json.dumps({'result' : task})


@huey.task()
def make_task():
    time.sleep(np.random.randint(1, 3))  # simulate slow computation
    return "Task completed"