# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 21:14:57 2016

@author: caiyi
"""

def write_res(file_name, res):
    with open(file_name,'w') as f:
        res_str = ''
        for i in range(len(res[:-1])):
            res_str += "Case #{}: ".format(i+1)+ str(res[i])+'\n'
        res_str += "Case #{}: ".format(i+2) + str(res[-1])
        f.write(res_str)
        

digits = {0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE"}

#def is_anagram (w1,w2): 
#    """
#    w1 w2 can be any iterable
#    """
#    if len(w1)!= len(w2):
#        return False
#    d = defaultdict(int)
#    for l in w1:
#        d[l] += 1
#    for l in w2:
#        d[l] -= 1
#        if d[l] < 0:
#            return False
#    return True
#    
# print is_anagram('how','wha') # tested now problem
        
        
    
import numpy as np
from collections import defaultdict
def split(s, word):
    """
    s: a list of letters as a numpy array
    strip word from S and return the rest, otherwise return None
    """
#    D1 = defaultdict(int)  # key:value is letter:nb_letter
#    D2 = defaultdict(list) # key:value is letter:list(index of that letter)
#    for l in word:
#        D1[l] += 1
#    for i in range(len(s)):
#        D2[s[i]].append(i)
#    res = []
#    if len(D1) != len(D2):
#        return None
#    for key in D1:
#        if D1[key] > len(D2[key]):
#            return None
#        res += D2[key][:D1[key]]
#    new_str = s[i for i in range(len(s)) if i not in set(res)]
    D = defaultdict(list)
    for i in range(len(s)):
        D[s[i]].append(i)
    for l in word:
        if l not in D or len(D[l])==0:
            return None
        D[l].pop()
    ind = []
    for key in D:
        ind += D[key]
#    print word
#    print s
#    print s[ind]
    return s[ind]



#s = np.array(list("OZONETOWER"))  # "tested, no problem"
#s1 = split(s,'TWO')
#print s1 
#s2 = split(s1,'ONE')
#print s2
#s3 = split(s2,'ZERO')
#print s3
    
def helper(s,res,l,start):
    """
    s is an array of letter, return the string of digits
    """
    
    for i in range(start,10):
        tmp = split(s,digits[i])
        #print tmp
        if tmp==None:
            continue
        if len(tmp) == 0:            
            res.append(l + str(i)) # why this is a bug
            return res
        else:
            helper(tmp,res,l + str(i),i) 
    return res
#S = np.array(list('NUINTFIONOEEREGH'))
#print helper(S,[],'',0)


with open('A-small-attempt1.in') as f:
    str1 = f.read()
    strs = str1.strip().split('\n')[1:]
##strs = [
##'OZONETOWER',
##'WEIGHFOXTOURIST',
##'OURNEONFOE',
##'ETHER'
##]
#
res_total = []
for S in strs:
    print "S", S
    s = np.array(list(S))
    res = helper(s,[],'',0)
    print 'res', res[0]
    res_total.append(res[0])
#print res_total
write_res('res_A_small.txt', res_total)
