#!/usr/bin/python

import sys, math

def factor(n):
  for i in range(2, 1+int(math.sqrt(n))):
    if n % i == 0:
      return i
  return None

def jamcoin(s):
  jc = s
  for b in range(2, 11):
    n = int(s, b)
    f = factor(n)
    if f == None:
      return None
    else:
      jc += " " + str(f)
  return jc

def base2(n, l):
  s = ""
  while n > 0:
    x = n % 2
    s = str(x) + s
    n = n / 2

  pad = l - len(s)
  if pad > 0:
    s = pad * "0" + s
  return s

T = int(sys.stdin.readline())
for test in range(T):
  print >> sys.stderr, "Test: %d" % (test+1)
  toks = sys.stdin.readline().strip().split()
  N = int(toks[0])
  J = int(toks[1])

  print >> sys.stderr, N,J

  print "Case #%d:" % (test+1)

  i = 0
  j = 0
  while j < J:
    jc = "1" + base2(i, N-2) + "1"
    print >> sys.stderr, jc
    res = jamcoin(jc)
    if res != None:
      print res
      j += 1
      print >> sys.stderr, jc, "!", j
    i += 1

