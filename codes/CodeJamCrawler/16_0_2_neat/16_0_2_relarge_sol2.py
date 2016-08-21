def nor(side):
  if side == '+':
    return '-'
  else:
    return '+'

def sol(n, side = '+'):
  if len(n) == 1:
    return 0 if n == side else 1

  i = len(n) - 2
  while i >= 0:
    if n[i] != n[-1]:
      break
    i -= 1

  if i == -1:
    return 0 if n[-1] == side else 1
  else:
    return sol(n[: i + 1], side) if n[-1] == side else sol(n[: i + 1], nor(side)) + 1

t = long(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    n = raw_input()
    print "Case #{}: {}".format(i, sol(n))
