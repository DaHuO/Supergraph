def f(n):
  if n == 0: return "INSOMNIA"
  curr, l = 0, 10
  f = [False] * 10
  while True:
    curr += n
    c = curr
    while c > 0:
      d = c % 10
      if not f[d]:
        f[d] = True
        l -= 1
      c //= 10
    if l == 0: return curr

t = int(raw_input())
for tt in xrange(1, t+1):
  n = int(raw_input())
  print "Case #" + `tt` + ":", f(n)

