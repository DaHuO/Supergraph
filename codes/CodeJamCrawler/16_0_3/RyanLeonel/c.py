def isqrt(n):
  x = n
  y = (x + 1) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def toStr(n,base):
  convertString = "0123456789"
  if n < base:
    return convertString[n]
  else:
    return toStr(n//base,base) + convertString[n%base]

n = 32
j = 500
j1 = 0
print "Case #1:"
i = (2**(n - 1)) + 1
while i < (2 ** n):
  x = toStr(i, 2)
  res = x
  xx = {}
  yy = {}
  zz = {}
  for i1 in range(2, 11):
    x2 = int(x, i1)
    y2 = 0
    if x2 % 2 == 0:
      y2 = 2
    z2 = (1000001 if isqrt(x2) > 1000000 else isqrt(x2) + 1)
    #z2 = isqrt(x2) + 1
    i2 = 3
    while i2 < z2:
      if x2 % i2 == 0:
        y2 = i2
        break
      i2 += 2
    xx[i1] = x2
    yy[i1] = y2
    zz[i1] = z2
    res += (" " + str(y2))
    if y2 == 0:
      break
  if y2 != 0:
    j1 += 1
    print res
  if j1 == j:
  	break
  i += 2
