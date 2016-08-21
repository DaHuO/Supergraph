#dancers

import math
import itertools
import statistics

def readinput():
    inputs=[]
    f=open('input.txt','r')
    for line in f:
        #inputs=line.rstrip().split(' ')
        inputs.append(line.rstrip())
    f.close()
    return inputs
    
def nCr(n,r):
    f=math.factorial()
    return f(n)/(f(r)/f(n-r))

def solve(l):
    if l==0:
        return 'INSOMNIA'
    chars=set()
    i=1
    while True:
        num=l*i
        n=list(str(num))
        n=list(map(int,n))
        for j in range(len(n)):
            chars.add(n[j])
        if len(chars)==10:
            return num
        i+=1

inputs=readinput()
cases=int(inputs[0])
inputs=inputs[1:]

f=open('output.txt','w')

for i in range(0,len(inputs)):
    #ints=inputs[i].split(' ')
    #ints=list(map(int,ints))
    solved=solve(int(inputs[i]))
    #solved=list(map(str,solved))
    f.write("Case #{}: ".format(str(i+1))+str(solved))
    f.write('\n')

f.close()
