from bitarray import bitarray
limit=(1<<20)-1
is_prime = bitarray(limit+1)
is_prime.setall(1)
is_prime[0]=0
is_prime[1]=0

def primes_upto(limit):
    global is_prime
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False


import math

def get_divisors(n):
    large_divisors = []
    #div_limit=0
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if is_prime[i] and n % i == 0:
            large_divisors.append(i)
            #div_limit+=1
            if i*i != n:
              large_divisors.append(n / i)
              #div_limit+=1
        #if div_limit>=10:
        #    break
    return large_divisors

def dec_to_bin(x):
    return bin(x)[2:]

primes_upto(limit)
f = open('C-small-attempt0.in', 'r')
t = int (f.readline())

for i in xrange(1, t + 1):
  print("Case #{}:".format(i))
  n,m = [int(s) for s in f.readline().strip().split(" ")]  # read a list of integers, 2 in this case
  min = (1<<(n-1))+1
  max = (1<<n)-1
  cnt=0
  while min<=max:
    out = ''
    div_cnt = 0
    if not is_prime[min]:
      divisors = get_divisors(min)
      divisors.sort()
      binnum = dec_to_bin(min)
      if len(divisors) == 0:
        min+=2
        continue
      div_cnt = 1
      out = binnum+ " " + str(divisors[0])
      divisors = [ dec_to_bin(s) for s in divisors] 
      for baseind in xrange(3,11):
        num = int(binnum, baseind)
        for divisor in divisors:
          div_conv = int(divisor, baseind)
          if num%div_conv==0:
            out += " " + str(div_conv)
            div_cnt+=1
            break
      if div_cnt!=9:
        min+=2
        continue
      print out
      cnt+=1
      if cnt == m:
        break
    min+=2


