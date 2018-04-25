import requests
import os
import json
from utils import Logger
from downloader import Downloader
from redisdb import RedisDB
from processor import Processor
import threading


class Spider(object):
    downloaders = list()
    redisDB = None
    instanceConf=None
    def __init__(self, config = None):
        self.instanceConf = config
        self.redisDB = RedisDB(config=self.instanceConf)
        for url in config.START_URL:
            self.redisDB.Enqueue(url, depth=0, title='', trycount=0)
        t1 = threading.Thread(target=self.startDownloader)
        t1.setDaemon(False)
        t1.start()
        self.downloaders.append(t1)
            
    def startDownloader(self):
        downloader = Downloader(self.redisDB,config=self.instanceConf)
        downloader.start()

    def stop(self):
        for t in self.downloaders:
            t.
            
    