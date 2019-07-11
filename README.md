# Falcon-Huey
API made with Falcon to serve a machine learning model together with Huey

# Set up

## DockerFile
WIP

## Manual
1. Make a conda environment with requirements.txt
2. Run a redis server on localhost:6379 (standard port)
3. Run serve.py (might need to change gunicorn to waitress)
4. Run a consumer for huey (how?)

# Test
localhost:5555 gives 'API is working'
localhost:5555/task created a task and gives the ID
localhost:5555/task/{id} gives NULL if the task is running and "Task completed" when the task is completed