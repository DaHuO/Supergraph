#! /usr/bin/env python

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
      return (False, 1)
    # 2 is the only even prime number
    if n == 2: 
      return (True, 1)
    # all other even numbers are not primes
    if not n & 1: 
      return (False, 2)
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    x = 3
    while x < int(n**0.5)+1:
      if n % x == 0:
          return (False, x)
      x += 2
    return (True, 1)

o = open('output.txt', "w")
o.close()
with open('C-small.in', 'r') as f:
  for i, line in enumerate(f.readlines()):
    if i == 0:
      print '%d test cases' % int(line)
      continue

    length = int(line.split(' ')[0])
    count  = int(line.split(' ')[1])
    lower = int('1' + '0' * (length - 2) + '1', 2)
    upper = int('1' * length, 2)
    print lower
    print upper
    jamcoins = []
    while lower < upper:
      coin = lower
      factors = []
      for base in range(2, 11):
        string = bin(coin)[2:]
        number = int(string, base)
        result = isprime(number)
        if result[0]:
          break
        else:
          factors.append(result[1])
      if len(factors) == 9:
        jamcoins.append((coin, factors))
      if len(jamcoins) == count:
        break
      lower += 2

    o = open('output-large.txt', "a")
    o.write('Case #%d:' % i)
    o.write('\n')
    for coin in jamcoins:
      o.write('%s %s' % (bin(coin[0])[2:], ' '.join(map(str,coin[1]))))
      o.write('\n')
    o.close()
