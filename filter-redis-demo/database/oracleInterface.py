import cx_Oracle
import ctypes


class Oracle(object):
    def __init__(self):
        ctypes.windll.LoadLibrary('D:/oracle/app/Administrator/product/11.2.0/dbhome_1/BIN/oci.dll')
        self.conn=cx_Oracle.connect('tpss_config/tpss_config@192.168.35.67')
        self.cur=self.conn.cursor();
        
    def close(self):
        self.cur.close()
        self.conn.close()



if __name__=='__main__':
    oracleInc=Oracle()
    r=oracleInc.cur.execute('SELECT * FROM tp_module p WHERE p.module_id>:module_id OR module_code=:code',
                  module_id=1008,code='psparam')
    
    #print(cur.description)
    #for column in range(len(cur.description)):
     #   print(cur.description[column]) 
    n=1;
    for cur_row in r:
        print(n,':',end='')
        for index in range(len(cur_row)):
           print(cur_row[index],',',end='') 
           
        n=n+1
        print('')
    oracleInc.close()