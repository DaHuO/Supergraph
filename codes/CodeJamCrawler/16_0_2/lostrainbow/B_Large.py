# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:38:48 2016

@author: Benben
"""


    
def sol(IF):
    pancakes=IF.readline()
    if pancakes[-1]=='\n':
        pancakes=pancakes[:-1]+'+'
    else:
        pancakes+='+'
    l=len(pancakes)
    count=0
    for i in range(l-1,0,-1):
        if pancakes[i]!=pancakes[i-1]:
            count+=1
    return str(count)



IF=open('B-large.in','r')
OF=open('output','w')
CaseN=int(IF.readline())
for i in range(1, CaseN+1):
    pretext='Case #{}: '.format(i)
    ans=sol(IF)
    if i<CaseN:
        ans=ans+'\n'
    OF.write(pretext+ans)
    
    
    
IF.close()
OF.close()


            
            