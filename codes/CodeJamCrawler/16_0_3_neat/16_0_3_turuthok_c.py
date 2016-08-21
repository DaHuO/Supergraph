import random

p = []
f = [0] * 65536
for i in xrange(2, 65536):
  if f[i] == 0:
    p.append(i)
    for j in xrange(i+i, 65536, i):
      f[j] = 1

def get_random(n):
  s = '1'
  for i in xrange(n-2):
    s += `random.randint(0, 1)`
  s += '1'
  return s

def jamcoin(s):
  global p
  res = [-1] * 9
  for i in xrange(9):
    v = int(s, i+2)
    for pp in p:
      if pp*pp > v: return [-1]
      if v % pp == 0:
        res[i] = pp
        break
    if res[i] < 0: return [-1]
  return res

raw_input()
n, j = map(int, raw_input().split())
all = set([])
print "Case #1:"
random.seed(34943)
while j > 0:
  s = get_random(n)
  if s not in all:
    d = jamcoin(s)
    if len(d) == 9:
      j -= 1
      all.add(s)
      print s, ' '.join(map(str, d))

