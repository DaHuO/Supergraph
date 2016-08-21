#!/usr/bin/env python
# -*- codinf: utf8 -*-
from itertools import product
from math import sqrt

inputfile = 'C-small-attempt1.in'
outputfile = 'small-output.op'

def nonTrivial(n):
  for i in xrange(2, int(sqrt(n))):
    if n%i==0:
      return i
  return -1

def checkprime(base, possi):
  val = 0
  for power, i in enumerate(possi[::-1]):
    val_no = int(i) * (base**power)
    val+=val_no
  return nonTrivial(val)

def et2brute(N, limit):
  dct = {}
  for j in product('01', repeat=N-2):
    if len(dct.keys()) == limit:
      break
    possi = '1'+''.join(j)+'1'
    tmp=[]
    for base in range(2, 11):
      val = checkprime(base, possi)
      if val!=-1:
        tmp.append(val)
      else: break
    if len(tmp) == 9:
      dct[possi] = tmp
  return dct

if __name__ == '__main__':
  inputdata = open(inputfile, 'rb').readlines()[1]
  N, j = map(int , inputdata.split())
  dct = et2brute(N, j)
  with open(outputfile, 'wb') as out:
    out.write('Case #1:\n')
    for k, v in dct.iteritems():
      result = str(k)
      for val in v:
        result+=' '+(str(val))
      out.write(result+'\n')