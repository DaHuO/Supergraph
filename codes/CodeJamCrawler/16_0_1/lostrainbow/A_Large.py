# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:21:59 2016

@author: Benben
"""

def getdigits(n):
    need=[True]*10
    while n:
        need[n%10]=False
        n=n//10
    return need
    
    
def sol(IF):
    num=int(IF.readline())
    if num:
        cur=num
        need=getdigits(cur)        
        while any(need):
            cur+=num
            temp=getdigits(cur)
            need=[all(item) for item in zip(need,temp)]
        return str(cur)
    else:
        return 'INSOMNIA'      



IF=open('A-large.in','r')
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


            
            