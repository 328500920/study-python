

import redis

class Redis(object):
    def __init__(self):
        print(redis)
        self.client = redis.StrictRedis(host='192.168.35.177',port=6371,db=0)
        
    def setHash(self,hashKey,key,value):
        return self.client.hset(hashKey,key,value)
    
    def getHash(self,hashKey,key):
        return self.client.hget(hashKey,key)
    
    def SetHashInc(self,hashkey,key):
        self.client.hincrby(hashkey, key, 1)
    
    def getHashLen(self,hashKey):
        return self.client.hlen(hashKey)
    
    def setList(self,key,value):
        return self.client.lpush(key,value)
        
    def getList(self,key):
        return self.client.lpop(key)   
    

if __name__=='__main__':
    print('filter redis 3.0')
    keys='fuxingwang'
    
    redisInt=Redis()
    redisInt.setHash(keys,'chinese','199')
    print(redisInt.getHash(keys,'chinese'))
    
    keys='fuxingwangList'
    redisInt.setList(keys, '299')
    redisInt.setList(keys, '201')
    print(redisInt.getList(keys))
    
    
    
    
    