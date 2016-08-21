# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:25:50 2016

@author: jo
"""
import numpy as np

def is_prime(n):
  factor = 0
  if n<= 3: return factor
  if n%2 == 0: 
      return 2
  if n < 9: return factor
  if n%3 == 0: return 3
  r = int(n**0.5)
  f = 5
  while f <= r:
    #print '\t',f
    if n%f == 0: return f
    if n%(f+2) == 0: return (f+2)
    f +=6
  return factor  
  
def str_base(number,base):
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + str(m)
    return str(m)
  
with open('input', 'r') as f:
    cases = 0
    case = 0
    with open('output', 'w') as fo:
     for line in f: 
        if case == 0:
            cases = int(line)
            case = 1
            #print(line)
        else:
          numbers = line.split()
          N = int(numbers[0])
          J = int(numbers[1])
          print(N)
          factors = [0]*9
          print(factors)
          maxNumber = 0
          for i in xrange(N):
              maxNumber += 10**(i)
              #print(maxNumber)
          minNumber = (10**(N-1) +1)
          
          #print(minNumber)
          Js = 0
          fo.write('Case #1:')
          for i in xrange(int(str(minNumber), 2),int(str(maxNumber), 2), 2):
              isPrime = False
              for j in xrange(2,11):
                  inBin = str_base(i, 2)
                  f= is_prime(int(inBin, j))
                  if(f>0):
                      factors[j-2] = f
                  else:
                      isPrime = True
                      break
              if isPrime: continue
              Js += 1
              
              fo.write('\n' + str(inBin))
              for factor in factors:
                  fo.write(' ' + str(factor))
              
              if(Js >= J):
                  break
          case +=1
                  
          