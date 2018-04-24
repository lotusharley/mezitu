import requests
import os
import json
from utils import Logger
from downloader import Downloader
from redisdb import RedisDB


class Spider(object):
    downloaders = list()
    redisDB = None
    instanceConf=None
    def __init__(self, config = None):
        self.instanceConf = config
        self.redisDB = RedisDB(config=self.instanceConf)
        self.redisDB.Enqueue(config.START_URL, depth=0, title='', trycount=0)
        for i in range(1, self.instanceConf.DOWNLOADSIZE, 1):
            downloader = Downloader(self.redisDB,config=config)
            downloader.start()
            self.downloaders.append(downloader)
    
    