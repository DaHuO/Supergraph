#https://code.google.com/codejam/contest/6254486/dashboard#s=p2
import time

path = 'C-large'
path_input = path + '.in'
path_output = path + '.out'

def readfile(path):
  with open(path, 'r') as f:
    data_raw = f.readlines()
  f.closed
  return data_raw

def writefile(path, outputs):
  f = open(path, 'w')
  s = []
  for i in range(len(outputs)):
      s.append('Case #' + str(i+1) + ':')
      for j in range(len(outputs[i])):
        s.append(' '.join(map(str, outputs[i][j])))
  f.write('\n'.join(s))
  f.close()

def genPrimesList(n):
  sieve = [True] * (n + 1);
  i = 1
  sieve[0] = False
  sieve[1] = False
  primes = []
  while i < n:
    i += 1
    if not sieve[i]:
      continue
    primes.append(i)
    i2 = 2 * i
    while i2 < n:
      sieve[i2] = False
      i2 += i
  return primes
  
  
primes = genPrimesList(pow(2, 20))  

def solve(problem):
  N, J = problem
  global primes
  output = []
  n = 2 ** (N - 1) - 1
  while len(output) < J:
    divisors = []
    n += 2
    ns = '{0:b}'.format(n)
    for base in xrange(2, 11):
      found = False
      x = int(ns, base)
      for p in primes:
        if p >= x:
          break
        if x % p == 0:
          divisors.append(p)
          found = True
          break
      if not found:
        break
    else:  
      output.append([ns] + divisors)

  return output
  
  
 
starttime = time.time()
data_raw = readfile(path_input)
del data_raw[0]
problems = []
i = False
for line in data_raw:
  problems.append(map(int, line.strip().split(' ')));
  
outputs = map(solve, problems)
writefile(path_output, outputs)
  
print 'running time: ', time.time() - starttime  