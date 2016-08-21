
# coding: utf-8

# In[1]:

import sys
import numpy as np


# In[2]:

def flip(subline):
    subline = subline[::-1]*-1
    return(subline)


# In[56]:

def solve(line):
    input_vec = np.zeros(26)
    ans_vec = np.zeros(10)
    for chara in line:
        idx = ord(chara) - 65
        input_vec[idx] += 1

    if input_vec[25] > 0:
        ans_vec[0] += input_vec[25]
        input_vec[4] -= input_vec[25]
        input_vec[14] -= input_vec[25]
        input_vec[17] -= input_vec[25]
        input_vec[25] -= input_vec[25]
    if input_vec[22] > 0:
        ans_vec[2] += input_vec[22]
        input_vec[14] -= input_vec[22]
        input_vec[19] -= input_vec[22]
        input_vec[22] -= input_vec[22]
    if input_vec[20] > 0:
        ans_vec[4] += input_vec[20]
        input_vec[5] -= input_vec[20]
        input_vec[14] -= input_vec[20]
        input_vec[17] -= input_vec[20]
        input_vec[20] -= input_vec[20]
    if input_vec[23] > 0:
        ans_vec[6] += input_vec[23]
        input_vec[8] -= input_vec[23]
        input_vec[18] -= input_vec[23]
        input_vec[23] -= input_vec[23]
    if input_vec[6] > 0:
        ans_vec[8] += input_vec[6]
        input_vec[4] -= input_vec[6]
        input_vec[7] -= input_vec[6]
        input_vec[8] -= input_vec[6]
        input_vec[19] -= input_vec[6]
        input_vec[6] -= input_vec[6]
        
    if input_vec[14] > 0:
        ans_vec[1] += input_vec[14]
        input_vec[4] -= input_vec[14]
        input_vec[13] -= input_vec[14]
        input_vec[14] -= input_vec[14]
    if input_vec[7] > 0:
        ans_vec[3] += input_vec[7]
        input_vec[4] -= input_vec[7] * 2
        input_vec[17] -= input_vec[7]
        input_vec[19] -= input_vec[7]
        input_vec[7] -= input_vec[7]        
    if input_vec[18] > 0:
        ans_vec[7] += input_vec[18]
        input_vec[21] -= input_vec[18]
        input_vec[13] -= input_vec[18]
        input_vec[4] -= input_vec[18] * 2
        input_vec[18] -= input_vec[18]

    if input_vec[21] > 0:
        ans_vec[5] += input_vec[21]
        input_vec[4] -= input_vec[21]
        input_vec[5] -= input_vec[21]
        input_vec[8] -= input_vec[21]
        input_vec[21] -= input_vec[21]
        
    if input_vec[13] > 0:
        ans_vec[9] += input_vec[13] / 2
        input_vec[8] -= input_vec[13] / 2 
        input_vec[4] -= input_vec[13] / 2
        input_vec[13] -= input_vec[13]
        
        
        
    print(input_vec)
    print(ans_vec)
    answer = []
    for i,j in enumerate(ans_vec):
        for k in range(int(j)):
            answer.append(i)
    return answer
    
    


# In[58]:

f = open("./2016_1B/A-small-attempt0.in",'r')
w = open("./2016_1B/A-small-attempt0.in.ans",'w')
numcases = int(f.readline())
for casenum in range(1,numcases+1):
    line00 = f.readline().strip()
    answer = solve(line00)
    print(line00)
    ans_int = map(str,answer)
    
    print('Case #' + repr(casenum) + ': ' + "".join(ans_int) + '\n')
    w.write('Case # ' +repr(casenum) + ': ' +  "".join(ans_int) + '\n')

f.close()
w.close()


# In[54]:



