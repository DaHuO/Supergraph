for t in range(1, input() + 1):
  cur = raw_input()
  res = cur[0]
  for elm in cur[1:]:
    if (elm >= res[0]): res = elm + res
    else: res = res + elm
  print "Case #" + str(t) + ": " + str(res)