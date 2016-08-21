def convert(s,b):
    num=0
    for i in range(len(s)):
        num+=(b**i)*(int(s[-i-1]))
    return num
import math
def check(num):
    n=2
    while n<=min(int(math.sqrt(num)),100000):
        if num%n==0:
            return n
        else:
            n+=1
    return 0
def done(s):
    op=[]
    for k in range(2,11):
        num=convert(s,k)
        if check(num)==0:
            op=[]
            return op
        else:
            op.append(check(num))
    return op

t=int(input())
n,j=map(int,input().split())
count=0
left=(2**(n-1))+1
right=(2**(n))-1
op=[]
used=[]
print('Case #1:')
while count<j:
    for i in range(left,right+1):
        if i%2!=0:
            s=bin(i)[2:]
            if s not in used:
                op=done(s)
                if len(op)==9 and count<j:
                    used.append(s)
                    print(s,end=' ')
                    for m in op:
                        print(m,end=' ')
                    print('')
                    count+=1
                    op=[]
