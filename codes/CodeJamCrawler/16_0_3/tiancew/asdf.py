import numpy as np
def primesfrom2to(n):
  sieve = np.ones(n/3 + (n%6==2), dtype = np.bool)
  sieve[0] = False
  for i in xrange(int(n**0.5)/3+1):
     if sieve[i]:
        k = 3*i + 1|1
        sieve[((k*k)/3)::2*k] = False
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
  return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def isaprime(n):
  for i in range(2,int(n**0.5) + 1):
      if n%i == 0:
        return False
  return True

n = 16
j = 50
numMax = 10**(n/2)  
primes = primesfrom2to(numMax)
#print primes
print 'Case #1:'
count = 0
curr = 2**(n-1)-1
while count < j and curr < numMax:
  curr += 2
  st = bin(curr)[2:]
  num = [0 for i in range(9)] 
  for i in range(9):
    num[i] = int(st,i+2) 
    if isaprime(num[i]): 
      break  
    if i == 8 and not isaprime(num[i]):
      print st,
      for l in num:
        for k in primes:  
          if l%k == 0: 
            print k,
            break 
      print
      count += 1
