primes = [2]
for i in range(3, 100000):
  sq = i ** 0.5
  for p in primes:
    if p >= sq:
      primes.append(i)
      break
    if i % p == 0:
      break


def getDivisor(n):
  for p in primes:
    if p ** 2 > n:
      return None
    if n % p == 0:
      return p
  return None


def solve(N, J):
  res = []
  n = int('1'+'0'*(N-2)+'1', 2)
  # primes = primesfrom2to((n * 2) ** 0.5)

  while len(res) < J:
    s = bin(n)[2:]
    divisors = []
    for i in xrange(2, 11):
      divisor = getDivisor(int(s, i))
      if divisor is None:
        break
      divisors.append(divisor)
    if len(divisors) == 9:
      res.append(s+' '+' '.join((str(x) for x in divisors)))
      print 'found one!', s, divisors
    n += 2
  return res

s = solve(32, 500)
with open('jamcoin.out', 'w') as out:
  out.write('Case #1:' + '\n')
  for i, x in enumerate(s):
    out.write(x + '\n')

