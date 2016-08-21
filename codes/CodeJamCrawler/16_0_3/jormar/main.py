import math

def divisorGenerator(n):
    # print "   - divisorGenerator: {}".format(n)
    large_divisors = []
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  if r > 150000:
    r=150000
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True    


def getNext(n):
  middleValue = 0
  middleValueLength = n-2

  i = 0
  while True:
    yield '1{:0>{}}1'.format(format(middleValue, 'b'), middleValueLength)
    middleValue = middleValue+1
    i=i+1

def isJamcoin(jamcoin):
  for base in xrange(2,11):
    value = int(jamcoin, base)
    if isPrime(value):
      return False

  return True

def getNonTrivialDivisors(jamcoin):
  result = list()
  for base in xrange(2,11):
    value = int(jamcoin, base)
    result.append(divisorGenerator(value).next())

  return result
    


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for icase in xrange(1, t + 1):
  n, j = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  total = 0

  # print "   - Starting Case # {}".format(icase)

  print "Case #{}:".format(icase)

  for jamcoin in getNext(n):
    if isJamcoin(jamcoin):
      total = total+1
      divisors = getNonTrivialDivisors(jamcoin)
      print "{} {}".format(jamcoin, ' '.join( [ str(x) for x in divisors ] ))

      if total == j:
        break

      # j=0
      # for base in xrange(2,11):
      #   value = int(jamcoin, base)
      #   print "   - Base {}: {} % {} = {}".format(base, int(jamcoin, base), divisors[j], int(jamcoin, base) % divisors[j])
      #   j=j+1
  
  # check out .format's specification for more formatting options
