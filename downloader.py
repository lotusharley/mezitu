# -*- coding: utf-8 -*-
import requests
import json
import time
from utils import Logger


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
                Logger().info('No New URL Wait Wait')
                time.sleep(5)
    
    def download(self, url='', depth=0, title='', trycount=0,headers = None):
        if headers == None:
            headers = self.instanceConf.DEFAULT_REQUESTHEADER
        response = requests.get(url, headers=headers)
        context = response.content
        #context = context.decode('utf-8').encode('gbk')
        if response.status_code == 200:
            self.redisDB.RemoveURL(url)
            jsonValue = json.dumps({'url':url,'depth':depth, 'title':title, 'trycount':trycount, 'finishedtime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, encoding='utf-8')
            self.redisDB.DBHashSet(hashkey=self.instanceConf.REDIS_FINISHED, rkey=url, rvalue=jsonValue)
            self.redisDB.RemoveURL(hashkey=self.instanceConf.REDIS_WAITURL,rkey=url)
            self.redisDB.EnqueueContext(Url=url,Content=context, Depth=depth, Title=title, Expression='')
            Logger().info('Download %s Finished HTTP Status %s'% (url,response.status_code))
        else:
            self.redisDB.Enqueue(url=url, depth=depth, title=title, trycount=trycount+1)
            return
        