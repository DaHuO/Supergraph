from solver import solve

t = int(input())
for i in range(1, t + 1):
  n = int(input())
  print("Case #{}: {}".format(i, solve(n)))