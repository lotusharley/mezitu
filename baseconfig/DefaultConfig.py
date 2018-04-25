import os


class defaultconfig(object):
    REDIS_DB = {'host':'localhost', 'port':6379, 'db':0}
    REDIS_NAMESPACE = "Mzitu.Redis"
    START_URL = ["http://www.mzitu.com/all/","http://www.mzitu.com/old/"]
    ALL_DOMAIN = "mzitu.com"
    CROWN_DEPTH_LIMITED = 3
    REDIS_QUEUE = "WAITURL"
    REDIS_WAITURL = "WAITFORREQUEST"
    REDIS_FINISHED = "FINISHEDURL"
    REDIS_URLCONTENT = "URLCONTENT"
    DOWNLOADSIZE = 1
    PROCESSORSIZE = 1
    DEFAULT_REQUESTHEADER = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'utf-8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}