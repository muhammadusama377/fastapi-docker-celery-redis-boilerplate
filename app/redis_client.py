import json

import redis
from .conf import settings
from typing import Any


class Cache:
    def __init__(self):
        self.client = redis.from_url(settings.redis_url)

    def get_value(self, key: str):
        value = self.client.get(key)
        if value:
            return json.loads(value)

    def set_value(self, key: str, value: Any):
        return self.client.set(key, json.dumps(value))


cache = Cache()
