def next(f):
    c = f.read(4)
    if c == "":
      return 0
    ans = 0
    for i in range(4):
      ans = ans + (ord(c[i]) << (8 * i))
    return ans

def load(f, A, B, base = 0, num = 1000):
  data = []
  while True:
    ans = next(f)
    if ans >= A and ans < B and (base == 0 or ans % base == 1):
      data.append(ans)
    elif ans == 0 or ans >= B or len(data) >= num:
      break
  return data

def find_next(f, i):
  while True:
    ans = next(f)
    if ans == 0 or ans > i:
      return False
    if ans == i:
      return True

# def find(L, bases):
#   for i in L:
#     for b in bases:
#       if i in b:
#         return False
#   return True

# def check(i, bases, top):
#   div = []
#   cands = []
#   for base in xrange(2, 11):
#     cands.append(int(str(i), base))
#   print cands
#   if find(cands, bases):
#     print i
#     for cand in cands:
#       for prime in top.iterkeys():
#         if cand % prime == 0:
#           div.append(prime)
#           break
#       else:
#         return False
#     print div
#     return True
#   return False

def list_p(L, top, div):
  rem = len(L)
  for i in xrange(rem):
    div.append(0)
  for p in top[0:1000]:
    if p ** 2 > L[-1]:
      break
    for i in xrange(len(L)):
      if L[i] == 0:
        continue
      if p ** 2 > L[-1]:
        return False
      if L[i] % p == 0:
        div[i + 1] = p
        L[i] = 0
        rem -= 1
    if rem == 0:
      break
  return rem == 0

def is_p(n, top):
  for p in top:
    if p ** 2 > n:
      return False
    if n % p == 0:
      return True

def next_cand(n):
  # n = 3
  b = int(str(n), 2)
  # b = (11)_2
  # b + 2 = (101)_2
  return int(bin(b+2)[2:], 10)

def sol(N, J):
  import math
  f = open("/Users/junli/Downloads/primes32/primes.32b", 'rb')
  top = load(f, 2, math.sqrt((10 ** 16 - 1) / 9), 0, 1000)
  top = [2] + top
  f.close()

  ans = []
  cand = 10 ** (N - 1) + 1
  while len(ans) < J:
    tb = map(lambda x: int(str(cand), x), range(2, 11))
    div = [cand]
    if not list_p(tb, top, div):
      cand = next_cand(cand)
      continue
    ans.append(div)
    cand = next_cand(cand)
  return ans

t = long(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
  N, J = map(lambda x: int(x), raw_input().split())
  if N == 16:
    sol16 = sol(N, J)
  else:
    sol16 = sol(N, J)
  print "Case #{}:".format(i)
  for div in sol16:
    print "{}".format(" ".join(map(lambda x: str(x), div)))
