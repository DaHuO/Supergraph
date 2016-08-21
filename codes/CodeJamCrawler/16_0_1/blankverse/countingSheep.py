def solve(x):
  if(x == 0):
    return "INSOMNIA"
  N = 0
  s = set()
  while len(s) < 10:
    N += x
    num = N
    while num > 0:
      s.add(num % 10)
      num /= 10
  return str(N)

T = int(input())
for i in range(T):
  x = int(input())
  print "Case #%d: %s" % (i+1, solve(x))
