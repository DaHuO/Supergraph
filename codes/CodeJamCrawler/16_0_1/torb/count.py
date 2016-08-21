from sys import stdin

def solve(N):
  seen = [0] * 10
  if N == 0:
    return "INSOMNIA"
  i = 0
  while 0 in seen:
    i += 1
    x = N * i
    while x > 0:
      seen[x % 10] = 1
      x /= 10
  return str(i * N)
  
T = int(stdin.readline())

for tc in range(1, T+1):
  N = int(stdin.readline())
  print "Case #%d: %s" % (tc, solve(N))
