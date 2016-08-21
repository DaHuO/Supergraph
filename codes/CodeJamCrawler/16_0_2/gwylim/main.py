t = int(raw_input())

for i in xrange(t):
  s = ''.join(reversed(raw_input()))
  j = 0
  while j < len(s) and s[j] == '+':
    j += 1
  flips = 0
  while j < len(s):
    if j == 0 or s[j-1] != s[j]:
      flips += 1
    j += 1
  print "Case #%d: %d" % (i+1, flips)
