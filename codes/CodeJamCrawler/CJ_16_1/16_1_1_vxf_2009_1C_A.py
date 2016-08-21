def solveCase(S):
  x = S[0]
  for c in S[1:] :
    if c < x[0] : x = x + c
    else : x = c + x
    
  return x

with open("A-large.in") as f :
  t = f.readline()
  t = int(t)
  for i in range(t) :
    S = f.readline().strip()
    y = solveCase(S)

    print("Case #%d: %s" % (i + 1, y))
