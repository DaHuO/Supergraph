import sys
cin = sys.stdin.readline
def readlist():
  return map(int, cin().split())
INF = sys.maxsize
NINF = -sys.maxsize - 1
#----------------------------------------------------------------------
from collections import defaultdict, Counter
import operator

T = int(cin())
for _t in xrange(T):
  S = cin().strip()
  ans = []
  for s in S:
    if ans and ord(s) >= ord(ans[0]):
      ans.insert(0, s)
    else:
      ans.append(s)
  print "Case #{}: {}".format(_t + 1, ''.join(ans))
