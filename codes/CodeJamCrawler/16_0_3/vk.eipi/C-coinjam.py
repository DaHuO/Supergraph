#!/usr/bin/python
import random
import sys
import math

# Sieve
MAX = 100000
primes = []
#divisor = [1 for i in xrange(MAX)]
is_prime = [True for i in xrange(MAX)]
is_prime[0] = False
is_prime[1] = False
for p in xrange(2, MAX):
  if is_prime[p]:
    primes.append(p)
    for multiple in xrange(p*p, MAX, p):
#      divisor[multiple] = p
      is_prime[multiple] = False

def try_coin(coin):
  divs = []
  for base in xrange(2, 10+1):
    bbase = int(coin, base)
    plim = int(math.sqrt(bbase))
    for p in primes:
      if p > plim:
        return None
      if bbase%p == 0:
        divs.append(p)
        break
    else:
      return None
  return divs

T= int(sys.stdin.readline())
assert(T == 1)
N, J= map(int, sys.stdin.readline().split())
triedcoins = set()
jamcoins = []
jamdivs = {}
TIMES = 100000
print "Case #1:"
for trial in xrange(TIMES):
  b2 = random.randrange(2**(N-2), 2**(N-1))*2+1
  coin = "{0:b}".format(b2)
  if coin in triedcoins:
    continue
  divs = try_coin(coin)
  triedcoins.add(coin)
  if divs is None:
    #print "fail", coin
    continue
  assert len(divs) == 9
  print coin, " ".join(map(str, divs))
  jamcoins.append(coin)
  jamdivs[coin] = tuple(divs)
  if (len(jamcoins) >= J):
    break
else:
  print "only found ", len(jamcoins)
