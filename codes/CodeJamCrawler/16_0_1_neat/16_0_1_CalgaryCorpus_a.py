import sys
 
def solve(nr):
   copianr = nr
   seen = set()
   seendigits = set()
   while not (copianr in seen):
      seen.add(copianr)
      seendigits = seendigits | set(list(str(copianr)))
      if len(seendigits) == 10: return str(copianr)
      copianr += nr
#      print "otra vuelta ", copianr
   return None
 
# main()
 
# read 1 number, use it to control the loop
for tc in xrange(1, int(sys.stdin.readline())+1):
    # read 2 numbers
    A = int(sys.stdin.readline())
    # read several floats, keep the result in a list
 
    best = solve(A)
    if best is None: best = 'INSOMNIA'
    print 'Case #%d: %s' % (tc, best)
