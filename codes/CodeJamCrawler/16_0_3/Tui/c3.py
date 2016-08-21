import gc;
from math import sqrt;
from itertools import count, islice;
import numpy;
from fractions import gcd;

def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n/2, dtype=numpy.bool)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

# def isPrime(n,prime):
#   if n in prime:
#     return True
#   return False

def isPrime(n):
  if n < 2: return False
  for number in islice(count(2), int(sqrt(n)-1)):
      if not n%number:
          return False
  return True

def get_all(number_str):
  s = []
  for i in range(2,11):
    v = int(number_str,i)
    if isPrime(v) == False:
      s.append(v)

  if len(s) != 9:
    s = []
  return s

def factors(n):
  i = 2
  factors = []
  while i * i <= n:
    if n % i:
      i += 1
    else:
      n //= i
      factors.append(i)
  if n > 1:
    factors.append(n)
  return factors

def findMinus(n):
  return n[len(n)-1]
  sum_a = 1
  for item in n[0:len(n)-1]:
    sum_a = sum_a * item

  return sum_a

def all_possible(leng):
  sa = []
  m = "1" * leng
  m = int(m,2)
  
  for i2 in range(0,m):
    t = bin(i2)
    n = str(t).replace("0b", "")
    if len(n) == leng and n[-1:] == "1":
      sa.append(n)

  sa.append("1" * leng)
  return sa


def main():
  f = open('c3.in', 'r')

  # Clear Output
  fclear = open('c3.out', 'w')
  fclear.write("")
  fclear.close()

  fw = open('c3.out', 'a')

  n = int(f.readline())
  c = 1
  for x in range(0, n):
    m = str(f.readline()).replace("\n", "").split(' ')
    s = all_possible(int(m[0]))
    max_z = int(m[1])
    z = 1
    fw.write("Case #" + str(c) + ":\n")

    # prime = primesfrom3to(int("1" * int(m[0]),10))
    for k in s:
      all_base = get_all(k)
      if len(all_base) == 0:
        continue
      print k
      temp = []
      for item in all_base:
        temp.append(findMinus(factors(item)))
        gc.collect()

      fw.write(k + ' ' + ' '.join(map(str, temp)) + "\n")

      if z >= max_z:
        break
      z = z + 1

main()