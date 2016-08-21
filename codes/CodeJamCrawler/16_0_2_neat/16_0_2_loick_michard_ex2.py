n=input()

h = {True: '-', False: '+'}

def pancakes(ps, inv=False):
  if (ps.count(h[inv]) == len(ps)):
    return 0
  if ps[-1] == h[inv]:
    return pancakes(ps[:-1], inv)
  return 1 + pancakes(ps[:-1], not inv)

for x in xrange(n):
  ps = raw_input()
  print 'Case #'+str(x+1)+':', pancakes(ps)