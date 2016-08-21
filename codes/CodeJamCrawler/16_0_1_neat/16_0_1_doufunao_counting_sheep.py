import math
import os
import sys


tests = []

def read(lines):
  # todo: read the input, create a list of lines
  c = lines[0]
  for i in range(1,c):
    tests.append({lines[i]: None})
  return tests

def mark(n, m):
  if n < 0:
    return

  if n == 0:
    m[0] = 1
    return

  while n > 0:
    a = n % 10
    m[a] = 1
    n = n / 10

def check(n):
  o = n
  m = {}
  r = 0
  while len(m) < 10:
    mark(n, m) 
    if n + o <= n:
      return False, n, r
    n = n + o
    r = r + 1
    
  return True, n-o, r


dataset = [
-1,
0,
1,
2,
11,
1692,
999999
]
dataset[0] = len(dataset) - 1

read(dataset)

dataset = []
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
dataset = [t]
for i in xrange(1, t + 1):
  n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  dataset.extend(n)
  # check out .format's specification for more formatting options

for i in range(1, dataset[0]+1):
  n = dataset[i]
  yes, lastn, r = check(n)
  if yes:
    print 'Case #%d: %d' % (i, lastn)
  else:
    print 'Case #%d: INSOMNIA' % i

sys.exit(0)
maxr = 0
maxrn = 0
for n in range(0, 1000000):
  yes, lastn, r = check(n) 
  if maxr < r:
    maxr = r
    maxrn = n
  if yes:
    # print 'Case #%d: %d %d' % (n, lastn, r)
    pass
  else:
    print 'Case #%d: INSOMNIA %d' % (n, r)

print 'max r ', maxr, maxrn


