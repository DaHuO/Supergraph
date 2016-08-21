import random
import sys
_mrpt_num_trials = 50 # number of bases to test

N = 32
J = 500
max_val = 1 << N
min_val = 1 + (1 << (N - 1))
max_prime = 3 << ((N + 1)/2)

def is_probable_prime(n):
    #Miller-Rabin primality test.
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True # no base tested showed n as composite

primes = [2]
x = 3
while x < max_prime: 
  if is_probable_prime(x):
    primes += [x]
  x += 2
#print len(primes)

pows = []
for b in xrange(2,11):
  bpows = []
  for p in xrange(N):
    bpows += [pow(b, p)]
  pows += [bpows]
#print pows

def to_base(x, base):
  bidx = base - 2
  if base == 2:
    return x
  r = 0
  for i in xrange(N):
    if x % 2 == 1:
      r += pows[bidx][i]
    x >>= 1
  return r

#x = 1 + (1 << 15)
#to_base(x, 3)

def toStr(x):
  S = ""
  while x > 0:
    S = ("1" if x&1 else "0") + S
    x >>= 1
  return S + " "


print "Case #1:"
cnt = 0
t = min_val - 2
while t < max_val:
  t += 2
  divs = []
  for b in xrange(2, 11):
    z = to_base(t, b)
    found = False
    for p in primes:
      if (z % p) == 0:
        divs += [p]
        found = True
        break
    if not found:
      break
  if found:
    R = toStr(t)
    for d in divs:
      R += " %d" % d
    print R
    cnt += 1   
    if cnt == J:
      break
