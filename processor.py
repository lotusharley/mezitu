# -*- coding: utf-8 -*-
import lxml
from urlparse import urlparse
from utils import Logger
from baseconfig import defaultconfig
import json
import time
from multiprocessing import Pool
import zmq

class Processor(object):
    instaceConf = None
    redisDB = None
    def __init__(self, config=None, redis=None):
        self.instaceConf=config
        self.redisDB = redis

    def start(self):
        Logger().info('Processor Start!')
        while(True):
            urlcontent = self.redisDB.GetQueueContent()
            if urlcontent == None:
                time.sleep(5)
                continue
            urlcontent = json.loads(json.loads(urlcontent))
            url = urlcontent['url']
            urlResult = self.resovlerURL(url=url)

    def resovlerURL(self, url=None):
        result = {}
        if url != None:
            urlResult = urlparse(url)
            domain = urlResult.hostname
            port = urlResult.port
            path = urlResult.path
            result = {'domain':domain, 'port':port, 'path':path}
            return result
        else:
            return None    

def startProcessor():
    from dbOperator import DBOperator
    from baseconfig import defaultconfig
    conf = defaultconfig()
    dbo = DBOperator(config=conf)
    localQueue = Queue(maxsize=conf.PROCESSOR_QUEUE_SIZE)
    while True:
        getSize = conf.PROCESSOR_QUEUE_SIZE - localQueue.qsize()
        if getSize>0:
            urls = dbo.getURL(maxdataLength=conf.DOWNLOADER_QUEUE_SIZE)
            print 'Process #%s Get %s URLS FOR Request'%(str(os.getpid()), str(len(urls)))
            for i in urls:
                localQueue.put(urls)
        else:
            print 'Reach Max Queue Size Wait...'
        time.sleep(15)

def start():
    from baseconfig import defaultconfig
    config = defaultconfig()
    zContext = zmq.Context()
    zSocket = zContext.socket(zmq.SUB)
    zSocket.connect('tcp://127.0.0.1:32768')
    zSocket.setsockopt(zmq.SUBSCRIBE,'')
    processPool = Pool(processes=config.DOWNLOADER_PROCESS)
    for i in range(0,2):
        processPool.apply_async(startProcessor,())
    print 'Wait Dispatcher Signal...'
    sRecv = zSocket.recv()
    if(sRecv == 'end'):
        print 'Receive Dispatcher End Signal...'
        processPool.terminate()
    processPool.join()

if __name__ == '__main__':
    defaultconfig = defaultconfig()