import os
import math

def get_prime_divider(number, primes):
  for p in primes:
    if p > int(math.sqrt(number)):
      break
    if number % p == 0:
      return p
  return 0

def get_all_primes(max_number):
  primes = [2]
  for i in xrange(3, max_number):
    pd = get_prime_divider(i, primes)
    if not pd:
      primes.append(i)

  print primes
  return primes

def get_actual_number(number, base):
  digits = []
  origin = number
  while number > 0:
    digits.append(number % 2)
    number /= 2

  current_base = 1
  actual_number = 0
  for d in digits:
    actual_number += current_base * d
    current_base *= base

  print digits, base, actual_number
  return actual_number

def is_jamcoin(number, primes):
  prime_dividers = []
  for base in xrange(2, 11):
    actual_number = get_actual_number(number, base)
    pd = get_prime_divider(actual_number, primes)
    if not pd:
      print 'Fail', number, actual_number, pd
      return False, []
    else:
      prime_dividers.append(pd)
  return True, prime_dividers

def solve(n, j):
  # max_prime_number = int(math.pow(2, 28))
  max_prime_number = int(math.pow(2, 20))
  primes = get_all_primes(max_prime_number)
  jamcoins = []

  start_number = int(math.pow(2, n-1)) + 1
  end_number = int(math.pow(2, n))
  for number in xrange(start_number, end_number, 2):
    jamcoin, prime_dividers = is_jamcoin(number, primes)
    if jamcoin:
      actual_number = get_actual_number(number, 10)
      jamcoins.append((actual_number, prime_dividers))
      if len(jamcoins) == j:
        break
  return jamcoins

fin = open('C.in', 'r')
fout = open('C.out', 'w')
for i, line in enumerate(fin):
  if i == 0:
    t = int(line)
    continue
  parts = line.strip().split()
  n = int(parts[0])
  j = int(parts[1])

  res = solve(n, j)

  out_str = 'Case #%d:\n' % i
  for ires in res:
    out_str += str(ires[0]) + ' ' + ' '.join([str(x) for x in ires[1]]) + '\n'
  print out_str
  fout.write(out_str)
fin.close()
fout.close()
