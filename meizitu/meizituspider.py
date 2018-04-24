import requests
from BeautifulSoup import BeautifulSoup
import os
import redis

class spider(object):
    def __init__(self, config = None):
        #Start
        #redisDB = redis.StrictRedis(host=config('host'), port=config['port'],db=config['db'])
        redisDB = redis.StrictRedis(host=config.REDIS_DB['host'], port=config.REDIS_DB['port'], db=config.REDIS_DB['db'])
        redisDB.lpush('cc','fdfdf','222','333')

    def run(self):
        pass