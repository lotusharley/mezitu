import requests
import os
import json
from utils import Logger
from downloader import Downloader
from redisdb import RedisDB
import threading
from baseconfig import DefaultConfig


class Spider(object):
    downloaders = list()
    redisDB = None
    instanceConf=None
    def __init__(self, config = None):
        self.instanceConf = config
        self.redisDB = RedisDB(config=self.instanceConf)
        for url in config.START_URL:
            self.redisDB.Enqueue(url, depth=0, title='', trycount=0)
        self.startDownloader()
            
    def startDownloader(self):
        downloader = Downloader(self.redisDB,config=self.instanceConf)
        downloader.start()


if __name__=='__main__':
    defconfig = DefaultConfig.defaultconfig()
    Logger().info('Start Spider')
    spiderInstance = Spider(config=defconfig)