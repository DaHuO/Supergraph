
# coding: utf-8

# In[7]:

import sys
import numpy as np


# In[163]:

def pick(line):
    line_sorted = np.argsort(line)
    if (sum(line) == len(line)) and sum(line) > 2:
        line[line_sorted[-1]] -= 1
        ans = chr(line_sorted[-1] + ord('A') )        
    elif line[line_sorted[-1]] == line[line_sorted[-2]]:
        line[line_sorted[-1]] -= 1
        line[line_sorted[-2]] -= 1
        ans = chr(line_sorted[-1] + ord('A') ) +chr(line_sorted[-2] + ord('A') )
    else:
        line[line_sorted[-1]] -= 1
        ans = chr(line_sorted[-1] + ord('A') )
    new_line = line
    return(ans, new_line)


# In[167]:

def solve(line00,line01):
    ans = []
    niter = sum(line01)
    for i in range(niter):
        ans00,line01 = pick(line01)
        ans.append(ans00)
        if sum(line01) < 1:
            break
    lasts = np.argsort(line01)
    ans_r = ans[::-1]
#     c1 = chr(lasts[-2] + ord('A') )
#     c2 = chr(lasts[-1] + ord('A') )
#     ans.append(c1+c2)
    return ans


# In[169]:

f = open("./2016_1C/A-small-attempt2.in",'r')
w = open("./2016_1C/A-small-attempt2.in.ans",'w')
numcases = int(f.readline())
for casenum in range(1,numcases+1):
    line00 = int(f.readline().strip())
    line01 = f.readline().strip().split(" ")
    line01 = map(int,line01)
    print(line01)
    ans = solve(line00,line01)
    ans1 = " ".join(ans)

    print('Case #' +repr(casenum) + ': ' +  " ".join(ans) + '\n')
    w.write('Case #' +repr(casenum) + ': ' +  " ".join(ans) + '\n')

f.close()
w.close()


# In[132]:



