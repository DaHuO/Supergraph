# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 03:54:57 2016

@author: User
"""

out=open("D_result_small.txt","w+")
result =[]
with open("D-small-attempt0.in") as f:
    lines = f.read().splitlines()
num_cases=int(lines[0])

for i in range(1,len(lines)):
    temp= "Case #" + str(i)+ ":"
    for j in range(int(str.split(lines[i])[0])):
        temp += " " + str(j+1)
    result.append(temp)       

out.write("\n".join(result))
out.close()