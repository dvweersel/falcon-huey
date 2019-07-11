from huey import RedisHuey

huey = RedisHuey('my-queue', host='127.0.0.1')