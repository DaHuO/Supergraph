T = input()
for t in range(1, T + 1):
  N = input()
  s = set()
  for i in range(1, 101):
    for j in str(i * N):
      s.add(j)
    if len(s) == 10:
      print('Case #%d: %d' % (t, i * N))
      break
  if len(s) != 10:
    print('Case #%d: INSOMNIA' % t)
