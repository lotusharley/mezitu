import redis
import json
from utils import Logger, URLEncode

class RedisDB(object):
    instanceConf = None
    redisDB = None

    def __init__(self, config=None):
        self.instanceConf=config
        self.redisDB = redis.StrictRedis(host=config.REDIS_DB['host'], port=config.REDIS_DB['port'], db=config.REDIS_DB['db'])

    def Enqueue(self,url=None, depth=0, title='',trycount=0):
        redisKeyname = '%s:%s' % (self.instanceConf.REDIS_NAMESPACE,self.instanceConf.REDIS_QUEUE)
        jencoder = json.encoder.JSONEncoder(skipkeys=False,ensure_ascii=True)
        redisValue = jencoder.encode(json.dumps({'url':url,'depth':depth, 'title':title, 'trycount':trycount}, encoding='utf-8'))
        if url==None:
            pass
        else:
            if not self.DBHExist(url):
                if depth == 0:
                    self.redisDB.rpush(redisKeyname,redisValue)
                    Logger().info('%s Insert To Queue'%url)
                else:
                    self.redisDB.lpush(redisKeyname,redisValue)
                    Logger().info('%s Append To Queue'%url)
                self.DBHashSet(hashkey=self.instanceConf.REDIS_WAITURL, rkey=url, rvalue=redisValue, timeoutspan=0)
            else:
                Logger().info('%s URL Already In Queue'%url)
    
    def EnqueueContext(self, Url='', Content='', Depth='', Expression='',Title=''):
        redisKeyname = '%s:%s' % (self.instanceConf.REDIS_NAMESPACE, self.instanceConf.REDIS_URLCONTENT)
        jencoder = json.encoder.JSONEncoder(skipkeys=False, ensure_ascii=True)
        redisValue = jencoder.encode(json.dumps({'url':Url,'depth':Depth, 'title':Title, 'Content':Content, 'Expression':Expression}, encoding='utf-8'))
        self.redisDB.rpush(redisKeyname,redisValue)

                
    def DBHashSet(self, hashkey='', rkey='', rvalue='',timeoutspan=0):
        redisKeyname = '%s:%s' %(self.instanceConf.REDIS_NAMESPACE, hashkey)
        self.redisDB.hset(redisKeyname, rkey, rvalue)
        if(timeoutspan>0):
            self.redisDB.expire(redisKeyname, timeoutspan*60)

    def DBHExist(self, hashkey='', rkey=''):
        redisKeyname = '%s:%s' %(self.instanceConf.REDIS_NAMESPACE, rkey)
        if(self.redisDB.exists(redisKeyname)):
            return True
        else:
            return False

    def GetQuene(self):
        rvalue = self.redisDB.lpop(self.instanceConf.REDIS_NAMESPACE + ':' + self.instanceConf.REDIS_QUEUE)
        if rvalue != None:
            return rvalue
        else:
            return None

    def GetQueueContent(self):
        rvalue = self.redisDB.lpop(self.instanceConf.REDIS_NAMESPACE + ':' +self.instanceConf.REDIS_URLCONTENT)
        if rvalue != None:
            return rvalue
        else:
            return None
    
    def RemoveURL(self, hashkey='', rkey=''):
        redisKeyname ='%s:%s' % (self.instanceConf.REDIS_NAMESPACE, hashkey)
        self.redisDB.hdel(redisKeyname,rkey)