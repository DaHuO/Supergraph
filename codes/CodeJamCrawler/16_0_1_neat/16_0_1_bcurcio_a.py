def solve(n):
  if n == 0:
    return 'INSOMNIA'
      
  m,s = 0,set([])
  while(len(s)<10):
    m+=n
    map(lambda x: s.add(x),str(m))
  return m

t = int(raw_input())
for x in xrange(1,t+1):
  n = int(raw_input())
  print 'Case #%d: %s'%(x,solve(n))
