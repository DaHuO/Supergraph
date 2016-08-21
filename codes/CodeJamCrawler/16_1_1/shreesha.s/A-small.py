t = int(raw_input())
for i in range(t):
  s = raw_input()
  new = s[0]
  leng = len(s)
  for j in range(1, leng):
    if s[j] >= new[0]:
      new = s[j] + new
    else:
      new = new + s[j]
  print "Case #%d:" %(i+1),
  print new.upper()
