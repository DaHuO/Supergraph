def isPrime(x):
    if x==1:
        return True
    i=2
    while i*i<=x:
        if x%i == 0:
            return False
        i+=1
    return True

primes = []

def findDiv(x):
    for n in primes:
        if n*n > x:
            break
        if x%n == 0:
            return n
    return None

MAX_PRIME = 10000
power=[]

def validate(mask, base):
    num = 0
    for i in range(N):
        if mask & (1<<i) != 0:
            num += power[base][i]
    return findDiv(num)

def maskStr(mask):
    res = ""
    i = N-1
    while i>=0:
        if mask&(1<<i) != 0:
            res += str(1)
        else:
            res += str(0)
        i-=1
    return res

if __name__ == '__main__':
    global N, J
    T=int(raw_input())
    for t in range(T):
        N, J = [int(x) for x in raw_input().split(' ')]
        print "Case #%d:" % (t+1)
        for i in range(2, MAX_PRIME):
            if isPrime(i):
                primes.append(i)
        power.append([0]*N)
        power[0][0]=1
        power.append([1]*N)
        for i in range(2, 11):
            p = [1]
            for j in range(1, N):
                p.append(p[j-1]*i)
            power.append(p)
        cnt = 0
        uplimit = 1<<(N-2)
        for i in range(uplimit):
            mask = (1<<(N-1)) | (i<<1) | 1
            divs = []
            for j in range(2, 11):
                div = validate(mask, j)
                if div==None:
                    break
                divs.append(div)
            if len(divs) == 9:
                ans = maskStr(mask)
                for d in divs:
                    ans += " "+str(d)
                print ans
                cnt += 1
                if cnt == J:
                    break
