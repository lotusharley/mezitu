# -*- coding: UTF-8 -*-
import requests
import json
import time
from utils import Logger
import ctypes
import zmq
from multiprocessing import Process, Pool, Queue
import os
import threading


def startDownloader(lq):
    from dbOperator import DBOperator
    from baseconfig import defaultconfig
    conf = defaultconfig()
    dbo = DBOperator(config=conf)
    while True:
        getSize = conf.DOWNLOADER_QUEUE_SIZE - lq.qsize()
        if getSize>0:
            urls = dbo.getURL(maxdataLength=conf.DOWNLOADER_QUEUE_SIZE)
            print 'Process #%s Get %s URLS FOR Request'%(str(os.getpid()), str(len(urls)))
            for i in urls:
                lq.put(urls)
        else:
            print 'Reach Max Queue Size Wait...'
        time.sleep(15)


def requestURL(lq):
    from baseconfig import defaultconfig
    while True:
        target = lq.get()
        if target == None:
            time.sleep(10)
            continue
        config = defaultconfig()
        url = target['url']
        header = config.DEFAULT_REQUESTHEADER
        if url=='':
            return 
        response = requests.get(url=url, header=header)
        print response.content


def start():
    from baseconfig import defaultconfig
    config = defaultconfig()
    localQueue = Queue(config.DOWNLOADER_QUEUE_SIZE)
    zContext = zmq.Context()
    zSocket = zContext.socket(zmq.SUB)
    zSocket.connect('tcp://127.0.0.1:32768')
    zSocket.setsockopt(zmq.SUBSCRIBE,'')
    processPool = Pool(processes=config.DOWNLOADER_PROCESS)
    for i in range(0,2):
        processPool.apply_async(startDownloader,())
    for j in range(0,2):
        processPool.apply_async(requestURL,())
    print 'Wait Dispatcher Signal...'
    sRecv = zSocket.recv()
    if(sRecv == 'end'):
        print 'Receive Dispatcher End Signal...'
        processPool.terminate()
    processPool.join()

if __name__ =='__main__':
    start()