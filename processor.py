# -*- coding: utf-8 -*-
import lxml
from urlparse import urlparse
from utils import Logger

class Processor(object):
    instaceConf = None
    redisDB = None
    def __init__(self, config=None, redis=None):
        self.instaceConf=config
        self.redisDB = redis

    def start(self):
        Logger().info('Processor Start!')

    def resovlerURL(self, url=None):
        result = {}
        if url != None:
            urlResult = urlparse(url)
            domain = urlResult.hostname
            port = urlResult.port
            path = url.path
            result = {'domain':domain, 'port':port, 'path':path}
        else:
            return None
    
    
        
