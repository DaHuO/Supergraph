def solve(s, target):
  if not s:
    return 0
  if s[-1] == target:
    return solve(s[:-1], target)
  else:
    return 1 + solve(s[:-1], s[-1])
  

T = int(input())
for i in range(T):
  s = input()
  print("Case #%d: %d" % (i+1,solve(s, '+')))
