'''
Varun Bharadwaj
'''
import itertools

l = []

def check_circle(x):
    n = len(x)
    if l[x[0]-1] != x[1] and l[x[0]-1] != x[-1]:
        return False
    if l[x[-1]-1] != x[-2] and l[x[-1]-1] != x[0]:
        return False
    for i in range(1,n-1):
        if l[x[i]-1] != x[i-1] and l[x[i]-1] != x[i+1]:
            return False
    return True

def numstudents(n):
    res = []
    s = list(range(1,n+1))
    for i in range(3,n+1):
        for x in itertools.permutations(s,i):
            if check_circle(x):
                res.append(len(x))
    return max(res)
    
    

testcases = int(input())

for t in  range(1,testcases+1):
    n = int(input())
    l = [int(x) for x in input().split()]
    print('Case #',t,': ',numstudents(n),sep='')
    
