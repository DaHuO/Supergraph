f = open('B-large.in', 'r')
t = int (f.readline())

for i in xrange(1, t + 1):
  count = 0
  cakes = f.readline().strip()
  prev = ''
  for currcake in cakes:
    if prev == '':
      prev = currcake
    else:
      if prev!=currcake:
        prev = currcake
        count+=1
  if cakes[0] == '-' and count%2==0:
    count+=1
  elif cakes[0] == '+' and count%2==1:
    count+=1

  print "Case #{}: {}".format(i, count)
