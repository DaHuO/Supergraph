
# coding: utf-8

# In[87]:

import sys
import numpy as np


# In[117]:

def flip(subline):
    subline = subline[::-1]*-1
    return(subline)


# In[370]:

def solve(line):
    flipcount = 0
    endflip = False

    for i in range(1,len(line)+1):
        if line[-i] == -1 and i == 1:
            for j in range(1,len(line)+1):
                if line[j-1] == -1 and j == 1:
                    line[:] = flip(line[:])
                    flipcount += 1
                    break
                elif line[j-1] == -1:
                    line[:j-1] = flip(line[:j-1])
                    line[:] = flip(line[:])
                    flipcount += 2
                    break
        elif line[-i] == -1:
            for j in range(1,len(line)+1):
                if line[j-1] == -1 and j == 1:
                    line[:-i+1] = flip(line[:-i+1])
                    flipcount += 1
                    break
                elif line[j-1] == -1:
                    line[:j-1] = flip(line[:j-1])
                    line[:-i+1] = flip(line[:-i+1])
                    flipcount += 2
                    break
    print(line)
    print(flipcount)
    return(str(flipcount))


# In[372]:

f = open("./2016_QR/B-small-attempt1.in",'r')
w = open("./2016_QR/B-small-attempt1.in.ans",'w')
numcases = int(f.readline())
for casenum in range(1,numcases+1):
    line00 = f.readline().strip()
    line01 = line00.replace("-","-1 ")
    line = line01.replace("+","1 ")
    line = np.fromstring(line, dtype=int, sep=' ')
#     print('Case #' + repr(casenum) + ': ' + solve(line))
    w.write('Case #' + repr(casenum) + ': ' + solve(line) + '\n')

f.close()
w.close()

