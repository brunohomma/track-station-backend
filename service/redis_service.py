import redis
from django.conf import settings

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)
'''
    Shortcuts for redis
'''

class RedisClient:

    def __init__(self, instance,):
        self.instance = instance

    def _set_value_by_key_redis(self, key, data, expire_key=False, expire_time=None):
        try:
            self.instance.set(key, str(data))
            if expire_key: self.instance.expire(key, expire_time)
            return True
        except: ...
        
        return False

    def _get_value_by_key_redis(self, key):
        try:
            value = self.instance.get(key)
            return value.decode('utf-8')
        except: ...

        return ''

    def _del_key_redis(self, key):
        if not key: return

        try:
            result = self.instance.delete(key)
            return result
        except: ...
            
        return False

    def _exist_key(self, key):
        try:
            value = self.instance.get(key)
            if value: return True
        except: ...

        return False

redis_client = RedisClient(redis_instance)
DAY_TIME = 86400