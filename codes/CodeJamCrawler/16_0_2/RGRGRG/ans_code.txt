import numpy as np
import random as rx
import math

f = open('test', 'r')
numcases = int(f.readline().rstrip('\n'))

for i in range(1,numcases+1):
    x = f.readline().rstrip('\n')
    count = 0
    for j in range(0,len(x)-1):
        if x[j] != x[j+1]:
            count = count+1
    if x[len(x)-1] == '-':
        count = count+1
    print "Case #" + str(i) +": "+str(count)
