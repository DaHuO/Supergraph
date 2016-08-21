ti = 0
tn = input()
while ti < tn:

  n = input()
  o = 'INSOMNIA'
  a = [True] * 10
  c = 0

  if n > 0:
    i = 1
    while c < 10:
      x = str(n * i)
      for j in range(10):
        if a[j] and str(j) in x:
          a[j] = False
          c += 1
      i += 1
    o = (i - 1) * n

  print 'Case #%s: %s' % (ti + 1, o)
  ti += 1
