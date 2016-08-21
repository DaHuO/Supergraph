#!/usr/bin/env python3
import sys
import numpy as np
import random
import functools

def factors(n):    
  return set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def hasfactor(x):
  for i in range(2, 50):
    if x % i == 0:
        return i
  else:
      return False


N = 32
J = 500

def Mutant():
  return '1'+''.join(np.random.choice(['0','1'],size=N-2,replace=True).tolist())+'1'

jamcoins = set()

print('Case #1:')

while J>0:
  cjc = Mutant()
  while cjc in jamcoins:
    cjc = Mutant()

  fstr = ""
  good = True
  for i in range(2,10+1):
    rep = int(cjc,base=i)
    fac = hasfactor(rep)
    if fac:
      fstr = fstr+str(fac)+" "
    else:
      good = False
      break

  if good:
    print("{0} {1}".format(cjc,fstr))
    jamcoins.add(cjc)
    J -= 1