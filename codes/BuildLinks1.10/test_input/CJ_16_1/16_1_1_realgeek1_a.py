import sys

def solve(s):
  t = []
  for c in s:
    if len(t) == 0:
      t.append(c)
      continue
    if c >= t[0]:
      t = [c] + t
    else:
      t.append(c)
  return ''.join(t)

def f (i, s):
  print 'Case #' + str(i) + ': ' + solve(s)

i = 0
for line in sys.stdin:
  i += 1
  if i == 1:
    continue
  f(i-1, line[:-1])

