T = input ()
for t in xrange (1, T + 1):
  d = {}
  n = input ()
  for i in range(2 * n - 1):
    a = map(int, raw_input().split())
    for j in a:
      if j not in d:
        d[j] = 0
      d[j] += 1
  ans = []
  for i in d:
    if d[i] % 2 != 0:
      ans.append(i)
  ans.sort()
  ans = map(str, ans)
  print("Case #%i: %s" % (t, " ".join(ans)))