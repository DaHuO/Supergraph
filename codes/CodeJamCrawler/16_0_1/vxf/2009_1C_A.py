def solveCase(n):
  if n == 0 :
    return "INSOMNIA"
    
  seen = set()
  i = 1
  while len(seen) < 10 :
    x = str(i*n)
    seen.update(set(x))
    i = i + 1
    
  return x

with open("A-large.in") as f :
  t = f.readline()
  t = int(t)
  for i in range(t) :
    n = f.readline()
    n = int(n)
    y = solveCase(n)

    print("Case #%d: %s" % (i + 1, y))
