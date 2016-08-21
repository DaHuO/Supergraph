
# coding: utf-8

# In[77]:

from __future__ import division
import fileinput
import math
import subprocess
import time
import numpy as np;
from sys import stdin;
from collections import defaultdict;




import itertools
def choose(n,k):
    return list(itertools.combinations(range(n),k))




# In[78]:

number_order = [("ZERO", 'Z',0),
("TWO", 'W',2),
("SIX", 'X',6),
("SEVEN", 'S',7),
("FIVE", 'V',5),
("EIGHT", 'G',8),
("FOUR", 'F',4),
("ONE", 'O',1),
("THREE", 'R',3),
("NINE", 'I',9)]


# In[79]:


f = open("test_input.in", "r")
T = int(f.readline());
input_x=[];
for case in range(1, T+1):
    input_x.append(f.readline().strip());


# In[80]:

from collections import Counter


# In[81]:

a


# In[82]:


def solve_bruteforce(ins, number_order):
    res = {};
    
    counta = Counter(list(ins))
    for number in number_order:
        num_of_number = counta[number[1]];
        for alphabet in list(number[0]):
            counta[alphabet] = counta[alphabet] - num_of_number;
        res[number[2]] = num_of_number;
    
    output_="";
    for i in res:
        for j in np.arange(res[i]):
            output_+=str(i);
            
    return output_;
            
            


# In[83]:

def solve_all_brute(all_ins):
    res = [];
    for instance in all_ins:
        res.append(solve_bruteforce(instance, number_order));
    return res;


def WriteResult(outputs):
    fh = open("output.out", "w")
    case_i = 1;
    for case in outputs:
        fh.write("Case #" + str(case_i) + ": " + case + "\n");
        case_i += 1;
        
    fh.close()

    


# In[84]:

out_x = solve_all_brute(input_x)


# In[ ]:




# In[85]:

WriteResult(out_x)


# In[44]:




# In[ ]:




# In[ ]:



