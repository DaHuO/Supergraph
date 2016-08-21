f = open('input', 'r');
N = int(f.readline())

for i in range(N):
 k, c, s = map(lambda x: int(x), f.readline().split())
 if (k>c*s): print 'Case #%d: IMPOSSIBLE' %(i+1)
 else:
  print 'Case #%d:' %(i+1),
  li = [x for x in range(k)] + [0 for x in range(c*k+1)]
  for j in range((k+c-1)/c):
   temp = 0;
   for l in range(c): temp += (li[c*j+l])*(k**(c-l-1))
   print '%d' %(temp+1),
  print '\n',
