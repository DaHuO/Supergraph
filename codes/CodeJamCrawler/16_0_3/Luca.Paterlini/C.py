import math
def AtkinSieve (limit):
    results = [2,3,5]
    sieve = [False]*(limit+1)
    factor = int(math.sqrt(limit))+1
    for i in range(1,factor):
        for j in range(1, factor):
            n = 4*i**2+j**2
            if (n <= limit) and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3*i**2+j**2
            if (n <= limit) and (n % 12 == 7):
                sieve[n] = not sieve[n]
            if i>j:
                n = 3*i**2-j**2
                if (n <= limit) and (n % 12 == 11):
                    sieve[n] = not sieve[n]
    for index in range(5,factor):
        if sieve[index]:
            for jndex in range(index**2, limit, index**2):
                sieve[jndex] = False
    for index in range(7,limit):
        if sieve[index]:
            results.append(index)
    return results

def conv_base(s,b,l):
    r=0
    for i in xrange(l):r=r*b+int(s[i])
    return r

def lowest_div(n,ps):
    for c in ps:
        if n%c==0: return c
    return -1

prime_sieve=AtkinSieve(10**6)
input()
N,J=map(int,raw_input().split())
u=0
print "Case #1:"
while J>0:
    u+=1
    q=bin(u)[2:]
    s='1'+'0'*(N-2-len(q))+q+'1'
    v=[]
    for c in xrange(2,11): v.append(conv_base(s,c,N))
    v=[lowest_div(x,prime_sieve) for x in v]
    if all(i>0 for i in v):
        print s,' '.join([str(x) for x in v]);J-=1
