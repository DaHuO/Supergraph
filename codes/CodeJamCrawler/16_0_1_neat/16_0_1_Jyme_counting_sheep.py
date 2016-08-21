case = 1
with open('input') as f:
  next(f)
  for line in f:
    pool = set()
    n = 1
    line = line.strip()
    out = line
    while True:
      if int(out) == 0:
        out = "INSOMNIA"
        break
      pool |= set(map(int,str(out)))
      if len(pool) == 10:
        break
      else:
        n = n+1
        out = int(line) * n
      
    print "Case #"+str(case)+": "+str(out)
    case += 1
    
