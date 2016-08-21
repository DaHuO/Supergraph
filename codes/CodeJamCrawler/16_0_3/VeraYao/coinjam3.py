import random
from fractions import Fraction
import sys

def isaprime(n):
  for i in range(2,int(n**0.5) + 1):
      if n%i == 0:
        return False
  return True

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def divisor(N):
        if N%2==0:
                return 2
        x = random.randint(1, N-1)
        y = x
        c = random.randint(1, N-1)
        g = 1
        while g==1:             
                x = ((x*x)%N+c)%N
                y = ((y*y)%N+c)%N
                y = ((y*y)%N+c)%N
                g = gcd(abs(x-y),N)
        return g

n = 16
j = 50
numMax = 10**(n/2)

def devisor(n):
  for i in range(2,n/2):
    if n%i == 0:
      return i 
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
        k = divisor(l)
        print k,
         
      print
      count += 1
