t = int(raw_input())
for i in range(t):
  val = []
  key = set([])
  ans = set([])
  n = int(raw_input())
  for j in range((2*n)-1):
    line = map(int, raw_input().split())
    for k in line:
      val.append(k)
      key.add(k)
  for j in key:
    if val.count(j) % 2 == 1:
      ans.add(j)
  ans = list(ans)
  ans.sort()
  print "Case #%d:" %(i+1),
  for j in ans:
    print j,
  print ""
