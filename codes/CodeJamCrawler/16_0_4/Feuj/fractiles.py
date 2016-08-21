def read_int(): return int(raw_input())
def read_ints(): return map(int, raw_input().split())  

T = read_int()

for t in xrange(T):
  k, c, s = read_ints()

  answer = " ".join(map(str, range(1,s+1)))

  print 'Case #%d: %s' % (t+1, answer)