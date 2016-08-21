T = 1#input()

N, J = 16,50#map(int, input().split())


from math import *

start = 2**(N-1) + 1


primes = dict()
def primefactor(n):
    if n in primes:
        return primes[n]

    else:
        sqtn = int(sqrt(n))
        for i in range(2, sqtn+2):
            if n % i == 0:
                return i

        return 0



ans = "Case #1:\n"
found = 0

while found < J:
    start += 2

    bnum = bin(start)[2:]


    works = True
    facs=[0 for i in range(10+1)] # only check 2 to 10
    
    for base in range(2, 10+1):
        numval = sum(base**(len(bnum)-i-1) * int(bnum[i]) for i in range(len(bnum)))

        #print(numval)
        
        facs[base] = primefactor(numval)
        if facs[base] == 0:
            works=False
            break


    if works:
        found += 1
        ans += bnum + " " + " ".join(str(f) for f in facs[2:]) + "\n"
        #print(ans)

print(ans)





#print(primefactor(35))
