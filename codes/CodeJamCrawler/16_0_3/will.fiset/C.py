
import functools
import random

# isprime - Rabin_Miller. Fail rate is: (1/2)^certainty
def isprime(p, certainty = 15 ):
    if(p<2): return False
    if(p!=2 and (p&1)==0): return False
    s=p-1
    while((s&1)==0): s>>=1
    for _ in range(certainty):
        a=random.randrange(p-1)+1
        temp=s
        mod=pow(a,temp,p)
        while(temp!=p-1 and mod!=1 and mod!=p-1):
            mod=(mod*mod)%p
            temp<<=1
        if(mod!=p-1 and  (temp&1)==0): return False
    return True

def getFactor(n):
  for i in range(2, n):
    if n % i == 0:
      return i

def isJamCoin(coin):
  
  if len(coin) < 2: return False
  if coin[-1] == "0": return False

  b2  = int(coin, 2); b3  = int(coin, 3)
  b4  = int(coin, 4); b5  = int(coin, 5)
  b6  = int(coin, 6); b7  = int(coin, 7)
  b8  = int(coin, 8); b9  = int(coin, 9)
  b10 = int(coin, 10)
  
  bases = [b2,b3,b4,b5,b6,b7,b8,b9,b10]
  are_primes = list(map(isprime, bases))
  are_all_prime = functools.reduce(lambda x, y: x or y, are_primes)
  
  if are_all_prime == False:
    return bases
  return False

def jamCoinGen(start, max_len):

  num = int(start, 2)
  
  while( True ):
    
    coin = bin(num)[2:]
    
    if (len(coin) > N):
      yield None
    
    bases = isJamCoin(coin)
    if bases != False: 
      yield [coin] + list(map(getFactor, bases))
    
    num += 1

  # Bases are all not prime, let's find those divisors

T = int(input())

for _case in range(1, T+1):
    
    print("Case #{:d}:".format(_case))
    N, J = map(int, input().split(" "))
    # print(N, J)
    start = "1" + "0"*(N-2) + "1"
    gen = jamCoinGen(start, N)
    count = 0
    
    while count != J:
      v = next(gen)
      if v == None: break
      print("{:} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d}".format(*v))
      count += 1 














