def read_int(): return int(raw_input())
def read_ints(): return map(int, raw_input().split())  


def find(N):
  if N==0:
    return 'INSOMNIA'

  n = N
  seen = [False for _ in range(10)]
  count = 0
  while True:
    for d in map(int, str(n)):
      if not seen[d]:
        seen[d] = True
        count += 1
        if count == 10:
          return n
    n += N

T = read_int()

for t in xrange(T):
  print 'Case #%d: %s' % (t+1, find(read_int()))