# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:21:59 2016

@author: Benben
"""
import bisect

def mytry(known):
    if len(known)==1:
        return known[0]
    Min=2500
    Max=1
    small=[]
    large=[]
    for i in range(len(known)):
        if known[i][0]<=Min:
            Min=known[i][0]
        if known[i][-1]>=Max:
            Max=known[i][-1]
    for i in range(len(known)):
        if known[i][0]==Min:
            small.append(i)
        if known[i][-1]==Max:
            large.append(i)
    if len(small)==2:
        frow=known.pop(small[0])
        fcol=known.pop(small[1]-1)
        frow.pop(0)
        fcol.pop(0)
        f=frow+fcol
        f.sort()
        for item in known:
            temp=item.pop(0)
            bl=bisect.bisect_left(f,temp)
            f.pop(bl)
        return f+mytry(known)
    else:
        frow=known.pop(large[0])
        fcol=known.pop(large[1]-1)
        frow.pop(-1)
        fcol.pop(-1)
        f=frow+fcol
        f.sort()
        for item in known:
            temp=item.pop(-1)
            bl=bisect.bisect_left(f,temp)
            f.pop(bl)
        return mytry(known)+f
        
        

def sol(IF):
    N=int(IF.readline())
    known=[]
    for i in range(N+N-1):
        temp=IF.readline().split()
        temp=[int(item) for item in temp]
        known.append(temp)
    res=mytry(known)
    return ' '.join([str(item) for item in res])
    
        
        
        
    
    
          



IF=open('B-large.in','r')
OF=open('small_output','w')
CaseN=int(IF.readline())
for i in range(1, CaseN+1):
    pretext='Case #{}: '.format(i)
    ans=sol(IF)
    if i<CaseN:
        ans=ans+'\n'
    OF.write(pretext+ans)
    
    
    
IF.close()
OF.close()


            
            