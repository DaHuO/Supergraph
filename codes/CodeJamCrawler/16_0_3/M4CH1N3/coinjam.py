from itertools import product

def prime_sieve(N):
  """
  Compute all prime to N
  initial condition: N > 1
  O(n log log n)
  """
  primes = [True]*(N+1)
  primes[0] = primes[1] = False

  for i in range(2, int(N**0.5)+1):
    if primes[i]:
      for j in range(i*i, N+1, i):
        primes[j] = False

  return primes

def divisor(num):
  """
  Return lowest divisor of number
  """
  for x in range(2,int(num**0.5)+1):
    if num%x == 0:
      return x
  return num

def jamcoin(digits):
  for binary in product(('0','1'),repeat=digits-2):
    coin = ''.join(('1',) + binary + ('1',))
   
    if not any(divisor(int(coin,base))==int(coin,base) for base in range(2,11)):
      print('Coin found: {}'.format(coin))
      yield coin


fh = open('output_large.txt','w')

T = int(input().strip())
for i in range(T):
  N, J = [int(x) for x in input().strip().split()]

  print('Case #{}:'.format(i+1),file=fh)

  coins = 0

  # Find Jam Coin
  for i in jamcoin(N):
    coins += 1

    # Find divisors
    div = []
    for base in range(2,11):
      div.append(divisor(int(i,base)))

    print('{} {}'.format(i,' '.join(map(str,div))),file=fh)
    if coins >= J: break
