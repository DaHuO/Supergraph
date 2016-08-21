import numpy as np
import random as rx
import math
import random

rem = np.zeros(15).astype(int)
count = 0
print "Case #" + str(1) +":"
seen = []
num = 1000000000000000
two = 65536/2-1

while count < 50:
    #num = 1
    two = two+2
    num = int("{0:b}".format(two))
    rem = np.zeros(15).astype(int)
    #for i in range(0,14):
    #    num = 10*num + random.randint(0,1)
    #num = 10*num + 1
    #print num
    #if seen.count(num)==1:
    #    continue
    #seen.append(num)

    fullsuc = 1
    for j in range(2,11):
        #convert to base
        base = 0.0
        suc = 0
        for i in range (0,16):
            base = j*base + int(str(num)[i])
            #print base
        #check if number is divis
        i = 2
        while i <= math.sqrt(base):
            if round(base/i) == base/i:
                #found
                suc = 1
                rem[j] = i
                break
            i = i+1
        if suc == 1:
            continue
        else:
            fullsuc = 0
            break

    if fullsuc == 1:
        print str(num)+" "+ str(rem[2])+ " "+ str(rem[3])+ " "+ str(rem[4])+" "+  str(rem[5])+ " "+ str(rem[6])+ " "+ str(rem[7])+" "+  str(rem[8])+ " "+ str(rem[9])+ " "+ str(rem[10])
        count = count+1