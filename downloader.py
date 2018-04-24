# -*- coding: utf-8 -*-
import requests
from baseconfig import BaseConfig
import json
import time


class Downloader(object):
    instanceConf = None
    redisDB = None
    #Start,Running,Wait
    Status = 'stoped'

    def __init__(self,rdb = None, config = None):
        self.redisDB = rdb
        self.instanceConf = config

    def start(self):
        self.Status='running'
        while(self.Status):
            rValue = self.redisDB.GetQuene()
            if rValue != None:
                rDict = dict()
                rDict = json.loads(json.loads(rValue))
                self.download(rDict['url'], rDict['depth'], rDict['title'], trycount=rDict['trycount'])
            else:
                time.sleep(5)
    
    def download(self, url='', depth=0, title='', trycount=0):
        response = requests.get(url)
        context = response.content
        context = context.decode('utf-8').encode('gbk')
        if response.status_code == 200:
            self.redisDB.RemoveURL(url)
            self.redisDB.DBHashSet(hashkey='DOWNLOADEDURL', rkey='DownloadedURL', rvalue=url)
        else:
            self.redisDB.Enqueue(url=url, depth=depth, title=title, trycount=trycount+1)
            return
        