import random

N = 32
J = 500

def isPrime2(a):
  if a < 10:
    return a in [2, 3, 5, 7]
 
  for k in xrange(2, min(a - 1, 1000)):
    if a % k == 0:
      return k
  return -1

def isJamCoin(s):
  for k in xrange(len(s)):
    if s[k] != '0' and s[k] != '1':
      return False
  if len(s) <= 1:
    return False
  if s[0] != '1' or s[-1] != '1':
    return False

  divisors = []

  for base in xrange(2, 11):
    k = 0
    for i in xrange(len(s)):
      k = k * base + ord(s[i]) - ord('0')
    divisor = isPrime2(k)
    if divisor != -1:
      divisors.append(divisor)
    else:
      return False, None

  return True, divisors

#print isJamCoin('100011')
#print isJamCoin('111111')
#print isJamCoin('111001')

found = {}

while True:
  s = '1'
  for i in xrange(N-2):
    if random.randint(0, 1) == 0:
      s += '0'
    else:
      s += '1'
  s += '1'
  
  jamCoin, divisors = isJamCoin(s)
  if jamCoin:
    found[s] = divisors

  if len(found) == J:
    break

print "Case #1:"
for s in found:
  print s + " " + " ".join([str(x) for x in found[s]])
  






