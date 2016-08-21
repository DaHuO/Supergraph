import sys
import itertools
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ N, K ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  ps = map(lambda x: float(x), sys.stdin.readline().strip().split(' '))

  res = 0.0

  sk = [ set(idxs) for idxs in itertools.combinations(range(K), K/2) ]

  for qs in itertools.combinations(ps, K):
    tmp = 0.0
    for idxs in sk:
      acc = 1.0
      for i in xrange(K):
        if i in idxs: acc *= qs[i]
        else: acc *= 1 - qs[i]
      tmp += acc
    res = max(res, tmp)

  print "Case #%d: %.12f" % (1+tmp_tc, res)

