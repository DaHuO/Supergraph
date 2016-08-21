#!/usr/bin/python
import sys
def raw_input(f=open(sys.argv[1])): return f.readline().rstrip()
n = int(raw_input())
for i in range(1, n+1):
   j = 1
   t = n = int(raw_input())
   digs = range(10)
   while len(digs):
      if j == 200:
         res ='INSOMNIA'
         break
      was_digs = list(digs)
      di = map(int, list(str(t)))
      for d in was_digs:
         if d in di:
            digs.remove(d)
      if not len(digs):
         res = str(t)
         break
      j += 1
      t = j * n
   print 'Case #%d: %s' % (i, res)

