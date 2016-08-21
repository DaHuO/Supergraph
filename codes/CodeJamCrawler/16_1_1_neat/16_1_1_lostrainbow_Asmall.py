# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:21:59 2016

@author: Benben
"""


def sol(IF):
    ori=IF.readline()
    if ori[-1]=='\n':
        ori=ori[:-1]
    res=ori[0]
    for i in range(1,len(ori)):
        if ord(res[0])>ord(ori[i]):
            res=res+ori[i]
        else:
            res=ori[i]+res
    return res
    
          



IF=open('A-large.in','r')
OF=open('large_output','w')
CaseN=int(IF.readline())
for i in range(1, CaseN+1):
    pretext='Case #{}: '.format(i)
    ans=sol(IF)
    if i<CaseN:
        ans=ans+'\n'
    OF.write(pretext+ans)
    
    
    
IF.close()
OF.close()


            
            