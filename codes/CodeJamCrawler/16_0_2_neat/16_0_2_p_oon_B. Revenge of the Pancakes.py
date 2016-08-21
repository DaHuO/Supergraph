import re
import sys
import random

def calc(s):
    s=s.rstrip('+')
    o=0
    ss=''
    for i in s:
        if ss!=i:
            o+=1
            ss=i
    return o


tddd = [
'-',
'-+',
'+-',
'+++',
'--+-',
]

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
ofg=1
tdd=0
if ofg and not tdd:
    sys.stdout = open('output.txt','w')
if tdd:
    for k,i in enumerate(tddd):
        print('TDD #%d: %s'%(k+1,str(calc(i))))
for i in range(scan()):
    print('Case #%d: %s'%(i+1,str(calc(scans()))))
if ofg and not tdd:
    sys.stdout.flush()
    sys.stdout.close()