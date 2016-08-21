import sys
import logutil
import yaml
import os
import import_utils

LOG = logutil.initlog('importer')

def icr(line,d):

    incr_cnt = 0
    
    if int(line) == 0:
       return "INSOMNIA"

    while len(d) < 10:
        incr_cnt = incr_cnt + 1
        val = incr_cnt * int(line)

        for i in str(val):
           d.add(int(i))

        ##logutil.log(LOG,logutil.INFO, "original value %s New value %s set %s " %(line,val,d))

        if len(d) == 10:
            return val

def main(args=None):
    
    cnt = 0;
    target = open("/home/siyer/result.txt", 'w')
    target.truncate()
    f = open("/home/siyer/input.txt")
    next(f)
    for line in f:
        ##print "value",line
        d = set()
        cnt = cnt + 1
        
        if len(d) == 0:
           
           for i in str.strip(line):
              d.add(int(i))

        val = icr(line,d)
        target.write( "Case #"+ str(cnt) + ": "+ str(val)) 
        target.write("\n")
   
    target.close()
    ###logutil.log(LOG, logutil.INFO, "End.")

if __name__ == "__main__":
    sys.exit(main())
