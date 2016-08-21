
mincs = {
  0: 'ZERO',
  1: 'ONE',
  2: 'TWO',
  3: 'THREE',
  4: 'FOUR',
  5: 'FIVE',
  6: 'SIX',
  7: 'SEVEN',
  8: 'EIGHT',
  9: 'NINE'
}

minc = {}

for d in range(10):
  s = mincs[d]
  newd = {}
  for c in s: newd[c] = newd.get(c, 0) + 1
  minc[d] = newd
    

def has(ch, dd):
  for k in dd:
    if ch.get(k, 0) < dd.get(k, 0): return False
  return True

def sol(ch, nc):
  global mincs, minc
  if nc == 0: return True, ''
  for d in range(10):
    dd = minc[d]
    if has(ch, dd):
      for k in dd: ch[k] -= dd[k]
      hassol, solved = sol(ch, nc - len(mincs[d]))
      if hassol: return True, str(d) + solved      
      for k in dd: ch[k] += dd[k]
  return False, ''

def solve(N):
  print N
  ch = {}
  nc = len(N)
  for c in N: ch[c] = ch.get(c, 0) + 1
  hassol, solved = sol(ch, nc)
  return solved

f = open('A-small-attempt0.in')
fo = open('output_A_small.out', 'w')

NT = int(f.readline())
for t in xrange(NT):
  N = f.readline().strip()
  fo.write('Case #' + str(t+1) + ': ' + str(solve(N)) + '\n')
  

f.close()
fo.close()