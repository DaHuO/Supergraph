import re
import sys
import random

def bbk(buck,x):
    x=str(x)
    for i in x:
        buck[int(i)]=1

def calc(x):
    if x==0:
        return 'INSOMNIA'
    buck = [0]*10
    bbk(buck,x)
    inc=x
    while not all(buck):
        x+=inc
        bbk(buck,x)
    return x


tddd = [
0,
1,
2,
11,
1692
]

buf=[]
def scans():
    global buf
    while 1:
        while len(buf) <= 0:
            buf=input().replace('\n',' ').split(' ')
        o=buf.pop(0)
        if o!='':
            break
    return o
def scan():
    return int(scans())
sys.stdin = open('input.txt')
ofg=1
tdd=0
if ofg and not tdd:
    sys.stdout = open('output.txt','w')
if tdd:
    for k,i in enumerate(tddd):
        print('TDD #%d: %s'%(k+1,str(calc(i))))
for i in range(scan()):
    print('Case #%d: %s'%(i+1,str(calc(scan()))))
if ofg and not tdd:
    sys.stdout.flush()
    sys.stdout.close()