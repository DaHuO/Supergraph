def solve_case(st, cn):
  st = list(st)
  cnt = 0
  while '-' in st:
    cnt += 1
    # eat all that are same
    i = 0
    t = st[i]
    while i < len(st) and st[i] == t:
      i += 1
    for j in range(i):
      if st[j] == "-":
        st[j] = "+"
      elif st[j] == "+":
        st[j] = "-"

  print "Case #%d:" % cn, cnt


T = int(raw_input())
for i in xrange(T):
  solve_case(raw_input(), i+1)

