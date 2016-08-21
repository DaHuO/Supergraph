import math
def isPrime(n):
    l = int(math.sqrt(n)+1)
    if(n>2):
        divs =  range(2,l+1)
        for i in divs:
            if(n%i==0):
                return n/i
    return 0

def perms(n):
    if not n:
        return

    for i in xrange(2**n):
        s = bin(i)[2:]
        s = "0" * (n-len(s)) + s
        yield s

def getNumber(n,j):
    ps = list(perms(n))
    xs = filter(lambda x:(x[0]=='1' and x[len(x)-1]=='1'),ps)
    ls = filter(lambda x:isPrime(int(x,2))!=0,xs)
    valid = []
    cnt = 0
    for num in ls:
        tmp1 = []
        tmp1.append(num)
        tmp2 = []
        flag=0
        for m in range(2,11):
            new = int(num,m)
            isP = isPrime(new)
            if(isP == 0):
                flag = 1
                break
            else:
                tmp2.append(isP)

        if(flag==1):
            continue
        else:
            tmp1.append(tmp2)
            valid.append(tmp1)
            cnt += 1
            if(cnt==j):
                break
    return  valid

t = input();
inps = []
for i in range(0,t):
    m,n = map(lambda x:int(x),raw_input().split());
    inps.append((m,n))



for i in range(0,t):
    ans = getNumber(inps[i][0],inps[i][1])
    print "Case #"+str(i+1)+":"
    for a in ans:
        print a[0],
        for b in a[1]:
            print b,
        print ""



