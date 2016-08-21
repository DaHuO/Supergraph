from math import sqrt
from sys import stderr

# n,j are known in advance (see hint in problem), define n,j here:
n = 32
j = 500

# as we deal with a factoring problem, some prime number database
# has to be provided. The needed size can be determined by trial and error.
maxPrime = 10

# compute primes 
sieve = list(range(maxPrime+1))
sieve[1] = 0
for i in range(2, int(sqrt(maxPrime))+1):
    if sieve[i] != 0:
        for ii in range(2*i,maxPrime+1,i):
            sieve[ii] = 0
sieve = [x for x in sieve if x !=0]

# now generate coins with increasing values and check validity of each
print("Case #1:")
generated = 0
val = 0
while generated<j:
    if val >= 2**(n-2):
        print("ERROR: Increase number of primes!")
        break
        
    coin = "1"+(n*"0"+bin(val)[2:])[2-n:]+"1"
    
    l = []
    for base in range(2,11):
        v = int(coin,base)
        for prime in sieve:
            if v%prime==0 and prime<v:
                l.append(prime)
                break
    val += 1
                
    if len(l)==9:
        # coin valid -> print
        generated += 1
        print(coin+" "+" ".join(str(item) for item in l))

      
    

        
    
