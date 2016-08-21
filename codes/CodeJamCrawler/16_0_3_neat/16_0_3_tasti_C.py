import math, random

NOT_PRIME = {}

def is_factor(n, m):
  return n % m == 0

def is_not_prime_helper(n):
  if n < 2:
    return 0

  if n == 2 or n == 3:
    return 0
  
  if is_factor(n, 2):
    return 2

  if is_factor(n, 3):
    return 3
  
  # for i in xrange(5, int(math.sqrt(n)) + 1, 6):
  for i in xrange(5, 100, 6): # CRAZY optimization
    if is_factor(n, i):
      return i

    if is_factor(n, i + 2):
      return i + 2
  
  return 0

def is_not_prime(n):
  if n not in NOT_PRIME:
    NOT_PRIME[n] = is_not_prime_helper(n)

  return NOT_PRIME[n]

def is_jamcoin(jamcoin):
  # return all(map(lambda x: not is_prime(int(jamcoin, x)), range(2, 11)))
  divisors = []
  for i in xrange(2, 11):
    negated_primality = is_not_prime(int(jamcoin, i))
    if negated_primality:
      divisors.append(negated_primality)
    else:
      return False

  return divisors

def random_jamcoin(N):
  return ['1'] + map(lambda x: str(random.getrandbits(1)), range(N-2)) + ['1']

def jamcoins_and_divisors(N, J):
  jads = {}
  while len(jads) < J:
    jamcoin = ''.join(random_jamcoin(N))
    divisors = is_jamcoin(jamcoin)
    if divisors:
      jads[jamcoin] = divisors

  return jads

filename = 'C-large'
f = open(filename + '.in', 'r')
o = open(filename + '.out', 'w')

T = int(f.readline())

for t in range(T):
  N, J = map(int, f.readline().split(' '))
  o.write('Case #%d:\n' % (t + 1))
  jads = jamcoins_and_divisors(N, J)
  for jamcoin, divisors in jads.iteritems():
    o.write('%s' % (jamcoin))
    for divisor in divisors:
      o.write(' %d' % (divisor))
    o.write('\n')
