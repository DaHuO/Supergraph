
# coding: utf-8

# In[44]:

import sys

def solve(N):
    res = set()
    findans = False
    
    if N == 0:
        return("INSOMNIA")        
    for i in range(1,100):
        num = str(i*N)
        for j in num:
            if j not in res:
                res.add(j)
        if len(res) == 10:
            findans = True
            break            
    if findans:
        return(num)
    else:
        return("INSOMNIA")


# In[45]:

f = open("./2016_QR/A-large.in",'r')
w = open("./2016_QR/A-large.in.ans",'w')
numcases = int(f.readline())
for casenum in range(1,numcases+1):
    N = int(f.readline().strip())
    
    print('Case #' + repr(casenum) + ': ' + solve(N))
    w.write('Case #' + repr(casenum) + ': ' + solve(N) + '\n')

f.close()
w.close()