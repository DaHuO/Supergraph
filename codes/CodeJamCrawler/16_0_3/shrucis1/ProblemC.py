import random

def isprime(n):
    if(n%2 == 0):
        return 2
    for i in range(3,int(n**(1/2))+2,2):
        if (n%i == 0):
            return i
    return True
    
def genhelper(l,c,n):
    if(n==1):
        l.append(c+"1")
    else:
        genhelper(l,c+"0",n-1)
        genhelper(l,c+"1",n-1)

def gen(n):
    l = []
    genhelper(l,"1",n-1)
    return l

def docase(a):
    ansstr = a
    for j in range(2,11):
        p = isprime(int(a,j))
        if(p == True):
            return False
        ansstr += " " + str(p)
    print(ansstr)
    return True

data_n = int(input("n=? "))
data_j = int(input("j=? "))
lst = gen(data_n)
random.shuffle(lst)
print("Case #1: ")
ans = 0
cur = 0
while ans < data_j:
    if(docase(lst[cur])):
        ans += 1
    cur += 1
