
import time
import math
import database.oracleInterface
import memory.redisInterface


def fromOracleToRedis():
    print('filter Oracle test')
    print('filter redis 3.0 test')
    
    tableName='SETTLE_ITME_DETAIL.TEST_1234567890'
    
    redisInt=memory.redisInterface.Redis()
    oracleInc=database.oracleInterface.Oracle()
    r=oracleInc.cur.execute('SELECT ACC_NBR FROM settle_item_detail p where rownum<2')
    
    beginSec=time.time()
    n=1;
    for cur_row in r:
        #print(n,':',end='')
        for index in range(len(cur_row)):
           #print(cur_row[index],',',end='') 
           iRet=redisInt.setHash(tableName,cur_row[index],1 )
           if  iRet == 0 :
               print('n :',n,',',cur_row[index],' return :',iRet)
               redisInt.SetHashInc(tableName,cur_row[index])
          
        n=n+1
        #print('')
        
    oracleInc.close()       
    runSec=time.time()-beginSec
    print(redisInt.getHashLen(tableName))
    print(runSec)

def CreateRedis():
    count=1234567890;
    base= 1000123351;

    print('filter redis 3.0 test')
    
    tableName='SETTLE_ITME_DETAIL.TEST_1234567890'    
    redisInt=memory.redisInterface.Redis()
    
    beginSec=time.time()
    for index in range(count):
       #print(index,',',end='') 
       iRet=redisInt.setHash(tableName,base+index,1)
       if  iRet == 0 :
           print('index :',index,',',base+index,' return :',iRet)
           redisInt.SetHashInc(tableName,base+index)  
       if index%5000 == 0 and index!=0 :
           RunSec=math.floor(time.time()-beginSec)
           beginSec=time.time()
           iPerl=math.floor(5000/RunSec)
           print('5000 time:',RunSec,'s,PERL:',iPerl ,'COUNT:',redisInt.getHashLen(tableName))
        
       if index==50000 :
           break

if __name__=='__main__':
    #fromOracleToRedis()
    CreateRedis()
   