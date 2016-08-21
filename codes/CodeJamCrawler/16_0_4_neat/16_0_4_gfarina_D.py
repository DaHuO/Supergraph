def solve():
  K, C, S = map(int, raw_input().split())
  return ' '.join(map(str, xrange(1, K + 1)))

T = input()
for t in xrange(T):
    print 'Case #%d:' % (t + 1,), solve()
