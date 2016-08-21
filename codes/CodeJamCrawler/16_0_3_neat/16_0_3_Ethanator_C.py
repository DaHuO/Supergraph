#!/usr/bin/python -tt
import random
import sys
from math import sqrt
import time
from itertools import count, islice

def is_prime(n): # prime return -1 else return factor
  if n == 2 or n == 3: return -1
  if n < 2 or n % 2 == 0: return 2
  if n < 9: return -1
  if n % 3 == 0: return 3
  r = int(n ** 0.5)
  f = 5
  while f <= r and time.time() < t_elapsed:
    if n % f == 0: return f
    if n % (f + 2) == 0: return f + 2
    f += 6
  return -1

def gen_ran(l):
  s = "1"
  for i in xrange(l-2):
    s += str(random.randint(0,1))
  s += "1"
  return int(s)

def base(a, b):
  s = str(a)
  k = 1
  res = 0
  for i in xrange(len(s)):
    x = int(s[len(s) - 1 - i])
    res += x * k
    k *= b
  return res

n = int(raw_input())
t_elapsed = 0
ouf = open("C.out", "w")
ouf.close()
for i in xrange(n):
  ouf = open("C.out", "a")
  ouf.write("Case #" + str(i + 1) + ":\n")
  ouf.close()
  line = raw_input().rstrip().split()
  n = int(line[0])
  j = int(line[1])
  d = []
  while len(d) < j:
    r = gen_ran(n)
    while r in d:
      r = gen_ran(n)
    t_elapsed = time.time() + 1
    factt = is_prime(r)
    if factt == -1:
      continue
    flag = False
    bases = []
    for k in xrange(2, 10):
      rr = base(r, k)
      t_elapsed = time.time() + 1
      fact = is_prime(rr)
      if fact == -1:
        flag = True
        break
      bases.append(fact)
    if flag:
      continue
    bases.append(factt)
    d.append(r)
    ouf = open("C.out", "a")
    ouf.write(str(r))
    for k in bases:
      ouf.write(" " + str(k))
    ouf.write("\n")
    ouf.close()
    print len(d)
