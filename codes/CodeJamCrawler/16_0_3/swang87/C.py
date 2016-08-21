def allstrings(N):
  c = [[1]]
  for i in range(N):
    c = [[x]+y for x in [0,1] for y in c]
  return [[1]+y for y in c]

def nextString(n):
  res = n
  n_len = len(n)
  for k in xrange(n_len-1, -1, -1):
    if n[k] == 0:
      res[k] = 1
      if k != n_len - 2:
        res[k+1 : n_len-1] = [0]* (n_len-2-k)
      return res

def digToBase(digits, b):
  n = 0
  for d in digits:
      n = b * n + d
  return n

def gen_primes():
  D = {}  
  q = 2  
  while True:
    if q not in D:
      yield q        
      D[q * q] = [q]
    else:
      for p in D[q]:
          D.setdefault(p + q, []).append(p)
      del D[q]
    q += 1

# get list of primes smaller than upper
def getPrimes(upper):
  p_gen = gen_primes()
  primes = [p_gen.next()]
  while primes[-1] < upper:
      primes.append(p_gen.next())
  return primes[:-1]

# maximum
primes = getPrimes(100000)

def checkPrime(k):
  if k in primes:
    return ''
  kstr = str(k)
  if kstr[-1] in set(['0', '2', '4', '6', '8']):
    return 2
  elif kstr[-1] == '5':
    return 5
  elif sum([int(i) for i in kstr]) % 3 == 0:
    return 3
  else:
    for p in primes:
      if k % p == 0:
        return p
  return ''


# def checkIfJam(val):
#   ret = []
#   for base in xrange(2, 11):
#     num = digToBase(val, base)
#     if num in set(primes):
#       return ''
#     else:
#       for p in primes:
#         if num % p == 0:
#           ret += [p]
#           break
#         if p == primes[-1]:
#           return ''
#   return ret

def checkIfJam(val):
  ret = []
  for base in xrange(2, 11):
    num = digToBase(val, base)
    a = checkPrime(num)
    if a == '':
      return ''
    else:
      ret += [a]
  return ret

# s = ' '.join([str(digToBase([1,0,0,1],i)) for i in xrange(2,11)])


N = 32
J = []
reqJ = 500
thisj = 0
i = [1]+[0]*(N-2)+[1]
last = [1]*N
while i != last:
  a = checkIfJam(i)
  if a != '':
    J += [[int(''.join([str(j) for j in i]))]+a]
    thisj += 1
    print thisj
  if thisj == reqJ:
    print 'done'
    break
  i = nextString(i)

out = open('C-large.out', 'w')
# for i in allstrings(N-2):
#   s = ' '.join([str(digToBase(i,b)) for b in xrange(2,10)])
#   out.write(''.join([str(j) for j in i])+s+"\n")

out.write("Case #1:\n")
for n in J:
  out.write(' '.join([str(j) for j in n])+"\n")

out.close()
