# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:21:59 2016

@author: Benben
"""

def toint(C,K):
    ans=1
    base=K
    for _ in range(C-1):
        ans+=base
        base*=K
    return ans

def SolveKC(K,C):
    if C==1:
        return list(range(1,K+1))
    else:
        ans=SolveKC(K,C-1)[1:2]
        step=toint(C,K)
        for _ in range(K-C):
            pre=ans[-1]
            ans.append(pre+step)
        return ans
    
    
def sol(IF):
    KCS=IF.readline().split()
    K=int(KCS[0])
    C=int(KCS[1])
    S=int(KCS[2])
    if S>K-C:
        ans=SolveKC(K,min(K,C))
        return ' '.join(str(item) for item in ans)
    else:
        return 'IMPOSSIBLE'
          



IF=open('D-small-attempt1.in','r')
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


            
            