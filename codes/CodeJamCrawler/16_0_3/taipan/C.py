N = 30000000
nums = [int(bin(i)[2:]) for i in range(32769, 65535, 2)]

def cb(n, b):
    out = 0
    s = str(n)
    for i in range(len(s)):
        out += int(s[i]) * pow(b, len(s) - i - 1)
    return out
    
primes = [True for i in range(N)]
primes[0] = False
primes[1] = False
p = []

def sieve():
    i = 2
    while i < N**0.5:
        for j in range(i + i, N, i):
            primes[j] = False
        
        i += 1
        while not primes[i]:
            i += 1
            
    for i in range(len(primes)):
        if primes[i]:
            p.append(i)
            
sieve()

t = int(input())
n, nn = input().split(' ')
n = int(n)
nn = int(nn)

for i in range(t):
    print('Case #' + str(t) + ':')
    
    for j in nums:
        fac = []
        for k in range(2, 11):
            n2 = cb(j, k)
            if n2 < N:
                if primes[n2]:
                    break
            for l in p:
                if n2 % l == 0:
                    fac.append(l)
                    break
                    
        if len(fac) < 9:
            continue
        else:
            print(j, end=' ')
            print(" ".join(str(asdf) for asdf in fac))
            nn -= 1
        if nn == 0:
            break