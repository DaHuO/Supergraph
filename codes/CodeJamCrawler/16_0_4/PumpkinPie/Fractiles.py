from __future__ import division

import os
import os.path, time
import itertools
import numpy as np


        
def genorig(K):
    ArrOrig=[]
    for i in range(0,2**K):
        seq=str("{0:b}".format(i)).zfill(K)
        ArrOrig.append(seq)
    return ArrOrig

def gencomp(K,C):
    ArrComp=[]
    ArrSum=[]
    for i in xrange(0,2**K):
        seqorig=str("{0:b}".format(i)).zfill(K)
        seq=seqorig
        for i in range(1,C):
            seqlist=list(seq)
            for i in range(0,len(seq)):
                if seqlist[i]=='1':
                   seqlist[i]='1'*K
                elif seqlist[i]=='0':
                    seqlist[i]=seqorig
            seq=''.join(seqlist)
            
        ArrComp.append(seq)
        
        seqlist=[int(x) for x in seq]
        
        if len(ArrSum)==0:
            ArrSum=np.array(seqlist)
        else:
            ArrSum=ArrSum+np.array(seqlist)

    return ArrComp,ArrSum


#fo=open("test.txt")
#fw=open("test_out.txt","w")
fo=open("D-small-attempt1.in")
fw=open("D-small-attempt1.out","w")

n=int(fo.readline())
for k in range(0,n):
        Line=fo.readline().split()
        K=int(Line[0])
        C=int(Line[1])
        S=int(Line[2])
        print "Case #"+ str(k+1)+": "
      
        '''ArrComp,ArrSum=gencomp(K,C)
        for i in range(0,len(ArrComp)):
            print ArrComp[i]'''
        text=""
        for i in range(1,S+1):
            text=text+str(i)+" "
        
        '''if ArrSum.max()+S<2**K:
            text="IMPOSSIBLE"
        else:
            ind = np.argpartition(ArrSum, -S)[-S:]
            indlist=[str(x) for x in ind+1]
            text=' '.join(indlist)'''
        print text
        fw.write("Case #"+ str(k+1)+": ")
        fw.write(str(text)+"\n")
                        
     
fw.close()        
        
                





