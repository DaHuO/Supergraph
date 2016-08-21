from itertools import cycle
T = int(raw_input())

for t in xrange(T):
    K, C, S = (int(c) for c in raw_input().split(' '))
    if S * C < K:
      out = 'IMPOSSIBLE'
    else:
      pos = range(K)
      out = ' '.join(
        str(sum(x * (K ** j) for j, x in enumerate(pos[i:i+C])) + 1)
        for i in xrange(0, len(pos), C)
      )
    print 'Case #' + str(t + 1) + ': ' + out
