import sys
import logutil
import yaml
import os
import import_utils
import string
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
    aDict = dict(zip(string.ascii_lowercase, range(1, 27))) 
    print aDict
    for line in f:
       cnt = cnt + 1
       first_time = True
       str2 =''
       for i in str.strip(line.lower()):
         if first_time:
             val = str.strip(line.lower())[0]
             first_time = False
             first_letter = previous_letter = new_letter = aDict[i]
         else:
             new_letter = aDict[i]
             previous_letter  = aDict[val]
             val =  i

         if first_letter > new_letter:
            str2 = str2 + i
         else:
            str2 = i + str2
            first_letter = new_letter
         val = i           
       target.write( "Case #"+ str(cnt) + ": "+ str(str2).upper()) 
       target.write("\n")

   
    target.close()

if __name__ == "__main__":
    sys.exit(main())
