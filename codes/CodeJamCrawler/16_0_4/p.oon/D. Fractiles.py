import re
import sys
import random

def pc(k,c):
    return [int(k**(c-i-1)) for i in range(c)]
def loc(pc,sq):
    return sum(i*j for i,j in zip(pc,sq))

def calc(k,c,s):
    '''
    K tiles
    C layers
    S tries
    '''
    pcz=pc(k,c)
    oo=[]
    ps=0
    cln=list(range(k))+[0]*c
    for i in range(s):
        oo+=[loc(pcz,cln[:c])+1]
        cln=cln[c:]
        ps+=c
        if(ps>=k):
            break
    else:
        return 'IMPOSSIBLE'
    return ' '.join(map(str,oo))

buf=[]
def scans():
    global buf
    while 1:
        while len(buf) <= 0: buf=input().replace('\n',' ').split(' ')
        o=buf.pop(0)
        if o!='': break
    return o
def scan(): return int(scans())
sys.stdin = open('input.txt')
ofg=0
if ofg:
    sys.stdout = open('output.txt','w')
for i in range(scan()):
    print('Case #%d: %s'%(i+1,str(calc(scan(),scan(),scan()))))
if ofg:
    sys.stdout.flush()
    sys.stdout.close()