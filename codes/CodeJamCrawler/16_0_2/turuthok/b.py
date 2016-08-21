def f(x):
  return (len(x)//2) * 2 if x[0] == '+' else ((len(x)-1)//2)*2 + 1

t = int(raw_input())
for tt in xrange(1, t+1):
  s = raw_input()
  x = s[0]
  for i in xrange(1, len(s)):
    if s[i] != x[len(x)-1]:
      x += s[i]
  print "Case #" + `tt` + ":", f(x)

