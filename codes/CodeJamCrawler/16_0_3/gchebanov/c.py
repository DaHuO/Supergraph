import random

T = int(input())

def get_dv(x):
  i = 2
  while i * i <= x:
    if x % i == 0:
      return i
    i += 1
  return x

def gen(j):
  s = '1' + ''.join([random.choice('01') for i in range(j-2)]) + '1' 
  proof = []
  for b in range(2, 11):
    x = 0
    for c in s:
      x *= b
      if c == '1':
        x += 1
    dv = get_dv(x)
    if dv == x:
      return None
    proof.append(dv)
  return s, proof

def solve(n, j):
  S = set()
  res = []
  while len(res) < n:
    while True:
      tmp = gen(j)
      if tmp:
        x, proof = tmp
        break
    if x in S:
      continue
    S.add(x)
    res.append((x, proof))
  return res

for t in range(T):
  j, n = map(int, input().split())
  print('Case #{}:'.format(t+1))
  for a, l in solve(n, j):
    print(a + ' ' + ' '.join(map(str, l)))

