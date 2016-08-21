def solve(P):
  res = []
  R = P[:]
  cnt = 0
  while sum(P) > 0:
    nonzeros = [i for i, x in enumerate(P) if x > 0]
    if len(nonzeros) == 2 and P[nonzeros[0]] == P[nonzeros[1]]:
      res.append(chr(nonzeros[0] + ord('A')) \
        + chr(nonzeros[1] + ord('A')))
      cnt += 2
      P[nonzeros[0]] -= 1
      P[nonzeros[1]] -= 1
    else:
      i = P.index(max(P))
      P[i] -= 1
      res.append(chr(i + ord('A')))
      cnt += 1
    if max(P) > sum(P) / 2:
      print 'majority', P

  if sum(R) != cnt:
    print 'count', R
  return " ".join(res)

t = int(raw_input())
for i in xrange(1, t + 1):
  N = int(raw_input())
  P = [int(s) for s in raw_input().split(" ")]  
  print "Case #{}: {}".format(i, solve(P))