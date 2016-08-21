def solveCase(case):
  i = 0
  while case :
    case = case.rstrip('+')
    if case == "" :
      return i
      
    i = i + 1
    t = case[0]
    c = case.lstrip(t)
    l = len(case) - len(c)
    t = '+' if t == '-' else '-'
    case = t*l + c

with open("B-large.in") as f :
  t = f.readline()
  t = int(t)
  for i in range(t) :
    case = f.readline()
    case = case.strip()
    y = solveCase(case)

    print("Case #%d: %d" % (i + 1, y))
