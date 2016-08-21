import sys

def count_sheep(n):
  if 0 == n:
    return 'INSOMNIA'

  x = 0
  unmarked = set(range(10))
  while unmarked:
    x += n
    unmarked -= set([int(c) for c in str(x)])
  return str(x)


t = int(sys.stdin.readline())
for i in range(1, t + 1):
  print('Case #%d: %s' % (i, count_sheep(int(sys.stdin.readline()))))
