import sys
ctr = -1
with open(sys.argv[1]) as f:
  for line in f:
    ctr += 1
    if ctr == 0:
      continue
    line = line.strip()
    flips = 0
    #print "Case #%d: %d" %(ctr, nxt)
    if len(line) == 1:
      if line == "+":
        print "Case #%d: %d" %(ctr, 0)
        continue
      if line == "-":
        print "Case #%d: %d" %(ctr, 1)
        continue
    for idx in range(len(line)):
      if idx == 0:
        prev = line[idx]
        soFar = prev
        continue
      if line[idx] == soFar:
        continue
      if soFar == "+":
        flips += 1
        soFar = "-"
      else:
        flips += 1
        soFar = "+"
    if soFar == "-":
      flips += 1
    print "Case #%d: %d" %(ctr, flips)





