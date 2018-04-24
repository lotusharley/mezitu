import os


class defaultconfig(object):
    REDIS_DB = {'host':'localhost', 'port':6379, 'db':0}
    REDIS_NAMESPACE = "Mzitu.Redis"
    START_URL = "http://www.mzitu.com/all/"
    ALL_DOMAIN = "mzitu.com"
    CROWN_DEPTH_LIMITED = 3
    REDIS_QUEUE = "WAITURL"
    REDIS_WAITURL = "WAITFORREQUEST"
    DOWNLOADSIZE = 3