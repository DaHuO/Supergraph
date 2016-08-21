def sol(K, C, S):
  if (C == 1 and S < K) or (C > 1 and S < K - 1):
    return "IMPOSSIBLE"

  if C == 1:
    return " ".join(map(lambda x: str(x), range(1, K + 1)))

  if K > 1:
    return " ".join(map(lambda x: str(x), range(2, K + 1)))
  else:
    return "1"

t = long(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    K, C, S = map(lambda x: int(x), raw_input().split())
    print "Case #{}: {}".format(i, sol(K, C, S))
