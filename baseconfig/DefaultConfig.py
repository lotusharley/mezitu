# -*- coding: UTF-8 -*-
import os


class defaultconfig(object):
    REDIS_DB = {'host':'localhost', 'port':6379, 'db':0}
    REDIS_NAMESPACE = "Mzitu.Redis"
    START_URL = [{'url':'http://www.mzitu.com/all/','title':'mzituAll'},{'url':'http://www.mzitu.com/old/', 'title':'mzituOld'}]
    ALL_DOMAIN = "mzitu.com"
    CROWN_DEPTH_LIMITED = 3
    DB_WAITURL = "WAITFORREQUEST"
    DB_COLLECTION = "seed"
    DB_NAME = 'Fireseed'
    REDIS_FINISHED = "FINISHEDURL"
    REDIS_URLCONTENT = "URLCONTENT"
    DOWNLOADSIZE = 1
    PROCESSORSIZE = 1
    DEFAULT_REQUESTHEADER = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'utf-8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    PUBLISHER_URL = 'tcp://*:32768'
    DOWNLOADER_PROCESS = 2
    MONGODB_CONNECTIONSTRING = {'host':'localhost', 'port':27017}
    DOWNLOADER_QUEUE_SIZE=100
    PROCESSOR_QUEUE_SIZE=200