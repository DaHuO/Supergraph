def solve(N):
  seen = [False]*10
  for i in range(1,100000):
    v = N * i
    for c in str(v):
      seen[int(c)] = True

    nt = True 
    for s in seen:
      nt = nt and s

    if nt:
      return v
  return "INSOMNIA"
    

T = int(input())
for i in range(T):
  N = int(input())
  print("Case #%d: %s" % (i+1, solve(N)))
