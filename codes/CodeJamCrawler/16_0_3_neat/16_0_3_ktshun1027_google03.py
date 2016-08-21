#coding = utf-8
import sys
from itertools import product

def is_prime(n):
    i = 2
    while i * i <=n:
        if n % i == 0:
            return i
        i += 1
    return 0

caseNum = input()
for i in xrange(caseNum):
    n,j = map(int,raw_input().split())
    nums = [0,1]
    case = i + 1
    A = []
    B = []
    for l in product(nums, repeat = n-2):
        temp = ""
        for m in l:
            temp += str(m)
        temp = "1" + temp +"1"
        anstemp = []
        for k in xrange(2,11):
            x = int(temp,k)
            ans = is_prime(x)
            if ans == 0:
                break
            else:
                anstemp.append(str(ans))
        if len(anstemp) == 9:
            A.append(temp)
            B.append(anstemp)
        if len(B) == j:
            break
    print "Case #{}:".format(case)
    for k in xrange(j):
        print A[k]+" "+" ".join(B[k])



