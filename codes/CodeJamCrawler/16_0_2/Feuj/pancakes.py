def read_int(): return int(raw_input())
def read_ints(): return map(int, raw_input().split())  

T = read_int()

for t in xrange(T):
  s = raw_input()[::-1]
  prev = "+"
  count = 0
  for c in s:
    if c != prev:
      count += 1
      prev = c

  print 'Case #%d: %s' % (t+1, count)