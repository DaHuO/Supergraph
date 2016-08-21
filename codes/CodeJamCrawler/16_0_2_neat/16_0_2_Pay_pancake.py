ti = 0
tn = input()

while ti < tn:

  s = raw_input()
  c = 0
  x = s[0]
  for i in range(1, len(s)):
    if s[i] != x: c += 1
    x = s[i]
  if s[-1] == '-': c += 1

  print 'Case #%s: %s' % (ti + 1, c)
  ti += 1
