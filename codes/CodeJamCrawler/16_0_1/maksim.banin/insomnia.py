def last_num(n):
  if n == 0:
    return "INSOMNIA"
  seen = set()
  x = n
  for c in str(x):
    seen.add(c)
  while True:
    x += n
    for c in str(x):
      seen.add(c)
    if len(seen) == 10:
        return x


t = int(raw_input())
for tc in range(t):
  n = int(raw_input())
  print 'Case #%d: %s'%(tc+1, last_num(n))
