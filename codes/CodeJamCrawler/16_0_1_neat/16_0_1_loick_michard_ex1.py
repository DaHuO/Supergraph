n=input()

def getSleep(n):
  initial = n
  if n == 0:
    return 'INSOMNIA'
  s = set()
  t = 0
  while True:
    for digit in str(n):
      s.add(digit)
    if len(s) > 9:
      break
    n += initial
    t += 1
  return n

for x in xrange(n):
  i=input()
  print 'Case #'+str(x+1)+':', getSleep(i)