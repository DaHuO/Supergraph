import sys
ctr = -1
with open(sys.argv[1]) as f:
  for line in f:
    seen = {}
    ctr += 1
    if ctr == 0:
      continue
    line = line.strip()
    num = int(line)
    idx = 0
    while(1):
      idx += 1
      nxt = num * idx
      if idx != 1 and nxt == num:
        print "Case #%d: %s" %(ctr, "INSOMNIA")
        break
      for d in str(nxt):
        if d not in seen:
          seen[d] = 1
      if len(seen) == 10:
        print "Case #%d: %d" %(ctr, nxt)
        break



