from solver import solve

t = int(input())
for i in range(1, t + 1):
  n, j = [int(s) for s in input().split(" ")]
  results = solve(n, j)
  print("Case #{}:".format(i))
  for result in results:
    print("{}".format(result))