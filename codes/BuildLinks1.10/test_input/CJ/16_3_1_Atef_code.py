
read_from = 2

if read_from == 2:
  inp = open("A-large.in")
elif read_from == 1:
  inp = open("A-small-attempt0.in")
else:
  inp = open("input.txt")
T = int(inp.readline().strip())

import operator

def get_max(h):
  hi = max(h.iteritems(), key=operator.itemgetter(1))[0]
  s = sum(h.values())
  h[hi] -= 1
  new_hi = max(h.iteritems(), key=operator.itemgetter(1))[0]
  if h[new_hi] * 2 > s - 1:
    h[new_hi] -= 1
    return [hi, new_hi]
  else:
    return [hi]

for kase in xrange(T):

  N = int(inp.readline().strip())
  P = map(int, inp.readline().strip().split(" "))
  rem = {}
  for i in range(N):
    rem[chr(ord('A') + i)] = P[i]
  ans = []
  while sum(rem.values()) > 0:
    #print rem
    hi = ''.join(get_max(rem))
    ans.append(hi)

  print "Case #%d: %s" % (kase + 1, ' '.join(ans))

