import math
import itertools

def construct_primes():
  # print 'constructing primes...'
  limit = 10000000
  is_prime = [True] * limit
  is_prime[0] = False
  is_prime[1] = False
  prime_list = []
  
  for i, isprime in enumerate(is_prime):
    if isprime:
      prime_list.append(i)
      if len(prime_list) > 500:
        break
      for x in xrange(i * i, limit, i):
        is_prime[x] = False
        
  # print 'done constructing primes...'
  return prime_list
  
def convert(i):
  binary = "{0:b}".format(i)
  return [int(binary, base) for base in xrange(2, 11)]

def find_divs(nums, prime_list):
  divs = [0] * 9
  for n, num in enumerate(nums):
    div_found = -1
    for prime in prime_list:
      if num % prime == 0:
        div_found = prime
        break
    if div_found != -1:
      divs[n] = div_found
    else:
      return None
  return [nums[-1]] + divs
  
  
def find_smallest_prime(num, prime_list):
  for i in prime_list:
    if num != i and num % i == 0:
      return i

def find_coin_jams(N, J):
  prime_list = construct_primes()
  
  start = (1 << (N - 1)) + 1
  stop = 1 << N
  count = 0
  for i in itertools.count(start, 2):
    if i >= stop or count == J:
      break
    
    divs = find_divs(convert(i), prime_list)
    if divs:
      count += 1
      print ' '.join([str(x) for x in divs])
  # print count

T = int(raw_input())
N, J = [int(x) for x in raw_input().strip().split()]
print 'Case #1:'
find_coin_jams(N, J)
