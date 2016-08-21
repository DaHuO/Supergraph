n=input()

dic = {}

def compute(c, j, idx, turn, poss):
  diff = 0
  if idx >= len(c):
    vc = int(''.join(c))
    vj = int(''.join(j))
    poss.append((abs(vc-vj),vc,vj,''.join(c),''.join(j)))
    return

  if turn == 0:
    if c[idx] != '?':
      return compute(c, j, idx, 1, poss)
    for i in xrange(10):
      c2 = c[::]
      c2[idx] = str(i)
      compute(c2, j, idx, 1, poss)

  if turn == 1:
    if j[idx] != '?':
      return compute(c, j, idx+1, 0, poss)
    for i in xrange(10):
      j2 = j[::]
      j2[idx] = str(i)
      compute(c, j2, idx+1, 0, poss)

for x in xrange(n):
  c, j = raw_input().split(' ')
  #print c, j
  print 'Case #'+str(x+1)+':',
  p = []
  compute(list(c), list(j), 0, 0, p)
  print sorted(p)[0][3],sorted(p)[0][4]