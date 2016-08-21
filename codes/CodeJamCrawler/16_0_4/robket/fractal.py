t = int(raw_input())
for tc in range(1, t+1):
  k, c, s = [int(x) for x in raw_input().split()]
  positions = []
  k_to_check = 0
  while k_to_check < k:
    position = 0
    for i in xrange(c):
      position = k * position
      position += min(k_to_check, k-1)
      k_to_check += 1
    positions.append(position)
  if len(positions) > s:
    print("Case #%d: IMPOSSIBLE" % (tc))
  else:
    print("Case #%d: %s" % (tc, " ".join([str(pos+1) for pos in positions])))


