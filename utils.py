#-*- coding: UTF-8 -*-
import os
import sys
import logging
import urllib

def URLEncode(content=''):
    return urllib.urlencode(content)

class Logger(object):
    __instance = None
    __logpath = ''
    def __init__(self):
        __logpath = '%s/log' % sys.path[0]

    def __new__(cls, *args, **kwd):
        if Logger.__instance is None:
            Logger.__instance = object.__new__(cls, *args, **kwd)
            Logger.__instance.__logger = logging.getLogger("logger1")
            Logger.__instance.__logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s', '%Y-%m-%d %H:%M:%S',)
            file_handler = logging.FileHandler(r"log/test.log")
            file_handler.setLevel(logging.INFO)
            stream_handler = logging.StreamHandler()
            file_handler.setFormatter(formatter)
            Logger.__instance.__logger.addHandler(file_handler)
            Logger.__instance.__logger.addHandler(stream_handler)
            Logger.__instance.__logger.info("log info: " + os.getcwd())
        return Logger.__instance

    def info(self,message):
        Logger.__instance.__logger.info(message)