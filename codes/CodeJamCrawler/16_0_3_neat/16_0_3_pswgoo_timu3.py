
#primes = [int(i) for i in open('prime.txt').read().split('\n') if i.strip()]
primes = []
#from math import sqrt
import math
from random import randint
def xn_mod_p(x, n, p):
  if n == 0:
    return 1
  res = xn_mod_p((x*x)%p, n>>1, p)
  if n&1 != 0:
    res = (res*x)%p
  return res
def xn_mod_p2(x, n, p):
  res = 1
  n_bin = bin(n)[2:]
  for i in range(0, len(n_bin)):
    res = res**2 % p
    if n_bin[i] == '1':
      res = res * x % p
  return res

def miller_rabin_witness(a, p):
  if p == 1:
    return False
  if p == 2:
    return True
  #p-1 = u*2^t 求解 u, t
  n = p - 1
  t = int(math.floor(math.log(n, 2)))
  u = 1
  while t > 0:
    u = n // 2**t
    if n % 2**t == 0 and u % 2 == 1:
      break
    t = t - 1
  b1 = b2 = xn_mod_p2(a, u, p)
  for i in range(1, t + 1):
    b2 = b1**2 % p
    if b2 == 1 and b1 != 1 and b1 != (p - 1):
      return False
    b1 = b2
  if b1 != 1:
    return False
  return True
def prime_test_miller_rabin(p, k):
  while k > 0:
    a = randint(1, p - 1)
    if not miller_rabin_witness(a, p):
      return False
    k = k - 1
  return True

def be_prime(x):
    for p in primes:
        if x % p == 0:
            return False
        if x < p:
            break
    return True
def be_prime_new(x):
    if x == 2:
        return True
    i = 2
    step = 1
    
    if x % 2 == 1:
        step = 2
        i = 3
    
    while i * i <= x:
        if x % i == 0:
            return False
        i += step
    return True
def interpret(s, base):
    s_list = [int(i) for i in s]
    s_len = len(s)
    ans = 0
    for i, k in enumerate(s_list):
        ans += base ** (s_len - i - 1) * k
    return ans

def generate_middle(n, L):
    bin_n = bin(n)
    len_bin = len(bin_n) - 2
    return '0' * (L - len_bin) + bin_n[2:]

def get_div(data):
    i = 2
    while i * i <= data:
        if data % i == 0:
            return i
        i += 1

def cal_n(n, j):
    middle_len = n - 2
    i = 0
    k = 0
    max_middle = 2 ** middle_len
    while i < max_middle:
        data = '1' + generate_middle(i, middle_len) + '1'
        tag = True
        yinzi = [data]
        for base in range(2, 11):
            interbase = interpret(data, base)
            '''
            if prime_test_miller_rabin(interbase, 50) == True:
                tag = False
                break
            '''
            if be_prime_new(interbase) == True:
                tag = False
                break
            yinzi.append(str(get_div(interbase)))
            
        if tag:
            k += 1
            print (' '.join(yinzi))
            if k >= j:
                break
        i += 1

inp = [i for i in open('test').read().split('\n')]
for i in range(int(inp[0])):
    n, j = inp[i+1].split()
    n, j = int(n), int(j)
    print ('Case #%d:' % (i+1))
    cal_n(n, j)
