# -*- conding:UTF-8 -*-

from pymongo import MongoClient
import time
from common import URLStatus

class DBOperator:
    instanceConf = None
    mongo = None
    def __init__(self,config=None):
        self.instanceConf=config
        self.mongo = MongoClient(host=self.instanceConf.MONGODB_CONNECTIONSTRING['host'], port=self.instanceConf.MONGODB_CONNECTIONSTRING['port'])

    def getCollection(self, collectionName=''):
        if collectionName == '':
            return None
        mongo = self.mongo
        db = mongo[self.instanceConf.DB_NAME]
        collection = db[collectionName]
        return collection
    
    def initDB(self):
        urls = []
        for item in self.instanceConf.START_URL:
            urls.append({'url':item['url'], 'title':item['title'],'depth':0, 'trycount':0, 'status': URLStatus.WAITFORHANDLE,'createtime':time.time()})
        self.insertURLS(urls)
    
    def insertURL(self, url=None, depth=0, title='', trycount=0):
        collection = self.getCollection(self.instanceConf.DB_WAITURL)
        #result = collection.find_one({'url':url})
        collection.insert_one({'url': url, 'title':title, 'depth':depth, 'trycount':trycount, 'status': URLStatus.WAITFORHANDLE,'createtime':time.time()})
        return 0

    def insertURLS(self,urls=[]):
        collection = self.getCollection(self.instanceConf.DB_WAITURL)
        waitforinsert = []
        for i in urls:
            result = collection.find_one(filter={'url':i['url']})
            if result == None:
                waitforinsert.append(i)
        if waitforinsert != []:
            collection.insert_many(waitforinsert)


    def getURL(self, maxdataLength=100):
        collection = self.getCollection(self.instanceConf.DB_WAITURL)
        result = []
        for i in range(0,maxdataLength):
            rs = collection.find_one_and_update(filter={'status':URLStatus.WAITFORHANDLE},update={'$set':{'status':URLStatus.PROCESSING}})
            if rs == None:
                break
            result.append(rs)
        return result


if __name__=='__main__':
    from baseconfig import defaultconfig
    conf = defaultconfig()
    dbo = DBOperator(config=conf)
    dbo.initDB()
    print 'Unit Test Finished.'
            
        
