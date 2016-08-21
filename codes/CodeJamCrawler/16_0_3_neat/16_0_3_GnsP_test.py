def isSqr(x):
  return int(x**0.5)**2 == x

def fermatFactor(n):
  if n%2==0:
    return 2
  a = int(n**0.5)
  if a**2 < n:
    a += 1
  b2 = a**2 - n
  while not isSqr(b2):
    a += 1
    b2 = a**2 - n
  return a-int(b2**0.5)


def modPow(b, e, m): 
  if m==1:
    return 0
  r = 1
  b = b%m
  while e>0:
    if e%2==1:
      r = (r*b)%m
    e /= 2
    b = (b*b)%m
  return r


def fastPrime(p):
  if p==2:
    return True
  return modPow(2, p-1, p)==1


def isComposite(n):
  if not fastPrime(n):
    #return fermatFactor(n)
    for i in range(2,10000):
      if n%i==0:
        return i
  return 0

def check(n, digs):
  s = bin(n)[2:]
  if len(s) < digs:
    s = '0'*(digs-len(s))+s
  m = [int(x) for x in s][::-1]
  m = [1] + m + [1]
  factors = []
  for b in range(2, 11):
    num = 0
    p = 0
    for i in m:
      num += i*(b**p)
      p += 1
    ret = isComposite(num)
    if ret != 0:
      factors.append(ret)
    else:
      return False
  return (''.join([str(x) for x in m[::-1]]),factors)

def solve(n, c):
  res = []
  count = 0
  for i in range(2**(n-2)):
    ret = check(i, n-2)
    if ret != False:
      res.append(ret)
      count += 1
    if count == c:
      break
  return res

for tc in range(int(input())):
  n, c = [int(x) for x in input().split()]
  print('Case #{_tc}:'.format(_tc=tc+1))
  ret = solve(n,c)
  for r in ret:
    #print(r)
    print(r[0]+' '+' '.join([str(x) for x in r[1]]))

#print(len(solve(int(input()))))
