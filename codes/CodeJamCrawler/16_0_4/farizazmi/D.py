for tc in range(1, input() + 1):
  k, c, s = map(int, raw_input().split())
  res = ""
  if k == 1: 
    res = "1"
  elif c == 1 and s < k:
    res = "IMPOSSIBLE",
  elif c == 1 and s >= k:
    for i in range(1, k + 1):
      res += str(i) + " "
  elif k == 2:
    res = "2"
  elif k == 3:
    res = "2 3"
  else:
    for i in range(2, k - 1):
     res += str(i) + " "
    res += str(pow(k, c) - k)
  print "Case #" + str(tc) + ": " + res
