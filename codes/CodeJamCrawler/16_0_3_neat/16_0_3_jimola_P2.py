SIZE = 40000
n = 32
j = 500
powers = [[0 for x in range(0, 32)] for x in range(0, 11)]
for i in range(2, 11):
    powers[i][0] = 1
    for z in range(1, 32):
        powers[i][z] = i*powers[i][z-1]
is_prime = [0 for x in range(0, SIZE)]
primes = [2]
for i in range(1, SIZE, 2):
    is_prime[i] = 1
is_prime[1] = 0
is_prime[2] = 1

for i in range(3, SIZE, 2):
    if(is_prime[i] == 1):
        primes.append(i)
        for z in range(2*i, SIZE, i):
            is_prime[z] = 0;
i = 0
ans = []
while(len(ans) < j):
    not_prime = 1
    temp = [i]
    for base in range(2, 11):
        b = 1+powers[base][n-1]
        s = bin(i)[2:]
        idx = len(s)-1
        while(idx >= 0):
            if(s[idx] == '1'):
                b += powers[base][len(s)-idx]
            idx-=1
        is_prime = 1
        for p in primes:
            if(b == p):
                break
            elif(b % p == 0):
                temp.append(p)
                is_prime = 0
                break
        if(is_prime == 1):
            not_prime = 0
            break
    i += 1
    if(not_prime == 1):
        ans.append(temp)
for x in ans:
    s = '1'
    t = bin(x[0])[2:]
    for y in range(0, n-2-len(t)):
        s += '0'
    s += t+'1'
    print(s),
    for i in range(1, len(x)):
        print(x[i]),
    print
                
