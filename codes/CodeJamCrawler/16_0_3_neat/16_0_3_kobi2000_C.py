import os
import sys
import StringIO

inputs="""\
"""
inf = StringIO.StringIO(inputs)

def prime_test(v):
  d = 2
  while d*d <= v:
    if v % d == 0:
      return d
    d+=1
  return True

def get_val(n, base):
  return sum(base**ix * int(v) for ix, v in enumerate(reversed(str(n))))

#def solve(S):
#  cnt = 0
#  s = S[0]
#  if len(S) > 0:
#    for ix in range(1, len(S)):
#      if S[ix] != s:
#        cnt += 1
#        s = S[ix]
#  return cnt + (s == '-')
#
#def nextVal():
#  return sys.stdin.readline().rstrip('\n')
#  #return inf.readline().rstrip('\n')
#
#T = int(nextVal())
#for t in range(1,T+1):
#  S = nextVal()
#  print "Case #%d: %s"%(t, solve(S),)

L = 16
J = 50
print "Case #1:"
import itertools
for x in reversed(list(itertools.product('10',repeat=L-2))):
  v = '1'+''.join(x)+'1'
  divisors = [prime_test(get_val(v, b)) for b in range(2,10+1)]
  if all(d != True for d in divisors):
    J -= 1
    print v, ' '.join(map(str,divisors))

  if J <= 0:
    break
