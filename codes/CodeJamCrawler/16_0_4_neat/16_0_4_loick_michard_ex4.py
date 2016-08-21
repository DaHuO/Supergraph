n=input()

def tails(k, c, s):
  if c * s < k:
    return 'IMPOSSIBLE'
  res = []
  pos = 0
  while len(res) * c < k:
    toCheck = 0
    for i in xrange(c):
      if pos + i < k:
        toCheck += (pos + i) * (k ** (c - i - 1))
    pos += c
    res.append(toCheck + 1)
  return ' '.join(map(str, res))

for x in xrange(n):
  k, c, s = map(int, raw_input().split())
  print 'Case #'+str(x+1)+':', tails(k,c,s)