input = open("B-large.in")
i = 0
for l in input:
  l = l.strip()
  if i == 0:
    i += 1
    continue
  curr = ""
  num = 0
  for j in range(len(l)):
    if j == 0:
      curr = l[j]
    else:
      if not curr == l[j]:
        curr = l[j]
        num += 1
  if l[len(l) - 1] == '-':
    num += 1
  print "Case #" + str(i) + ": " + str(num)
  i += 1
