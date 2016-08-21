for t in range(input()):
  n = input()
  f = [0] * 2505
  for i in range(2 * n - 1):
    x = map(int, raw_input().split())
    for j in x:
      f[j] = (f[j] + 1) % 2
  res = ""
  for i in range(2501):
    if (f[i] == 1):
      res += " " + str(i)
  print "Case #" + str(t + 1) + ":" + res
