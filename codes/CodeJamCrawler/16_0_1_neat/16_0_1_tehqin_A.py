def getNext(curN):
   if curN == 0:
      return 'INSOMNIA'
   seen = set(list(str(curN)))
   x = curN
   while len(seen) < 10:
      x += curN
      seen |= set(list(str(x)))
   return str(x)

T = int(raw_input())
for tc in range(1, T+1):
   print 'Case #{}: {}'.format(tc, getNext(int(raw_input())))
