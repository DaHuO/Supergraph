
# coding: utf-8

# In[19]:

import os


# In[20]:

def findmaxindex(ls):
    if (ls[0] < ls[1]):
        res = (1, 0)
    else:
        res = (0, 1)
        
    for i in range(2, len(ls)):
        if (ls[i] > ls[res[0]]):
            res = (i, res[0])
        elif (ls[i] > ls[res[1]]):
            res = (res[0], i)
    return res

def solve(ls):
    i, j = findmaxindex(ls)
    vi, vj = ls[i], ls[j]
    
    result = ""
    while (vj < vi):
        result += "{} ".format(chr(ord('A') + i))
        vi -= 1
        ls[i] -= 1
    
    for k in range(len(ls)):
        for d in range(ls[k]):
            if k != i and k != j:
                result += "{} ".format(chr(ord('A') + k))

    maxC1 = chr(ord('A') + i)
    maxC2 = chr(ord('A') + j)
    for f in range(vi):
        result += "{}{} ".format(maxC1, maxC2)
    return result 


# In[21]:

path = "input.txt"
result = []
with open(path, "r") as fin:
    T = int(fin.readline())
    for t in range(T):
        groups = int(fin.readline().strip())
        senat = [int(x) for x in fin.readline().strip().split(" ")]
        result.append(solve(senat))


# In[22]:

with open("result.txt", "w") as f: 
    for t in range(len(result)):
        f.write("Case #{}: {}\n".format(t + 1, result[t]))


# In[ ]:



