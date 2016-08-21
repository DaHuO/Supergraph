from solver import solve

t = int(input())
for i in range(1, t + 1):
  s = input()
  print("Case #{}: {}".format(i, solve(s)))