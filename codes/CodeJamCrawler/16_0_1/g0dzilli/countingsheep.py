#Code by Lilli Christoph 2016
#!usr/bin/python


import sys

num_cases = int(sys.stdin.readline())
loopmax = 2000 #should only need like 45
for i in range(num_cases):
    numberwang = int(sys.stdin.readline())

    myDigits = []
    lastSheep = numberwang
    if(numberwang == 0):
        print'Case #{}: {} '.format(i+1, 'INSOMNIA')
        continue
    for j in range(1,loopmax):      
        lastSheep = str(j*numberwang)
        for k in lastSheep:
            if(myDigits.count(k) == 0):
                #digit has not been seen
                 myDigits.append(k)
                
        if (len(myDigits) == 10):
            #seen it all, print and go next numberwang
            break
            
    if j >= loopmax:
        print 'ERROR YOU SUCK'
    print 'Case #{}: {}'.format(i+1, lastSheep)
