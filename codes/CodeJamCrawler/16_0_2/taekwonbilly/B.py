def flip(s,i):
  t= "".join({'+':'-','-':'+'}[a] for a in s[i-1::-1]) + s[i:]
#  print ("V", s, i, t)
  return t

from Queue import Queue as Q

cases = int(raw_input())
for case in range(cases):
  dat = raw_input()
  q = Q()
  q.put((0,dat))
  res = None
  done = { dat }
  while res is None:
    c,val = q.get()
#    raw_input()
#    print (c,val)
    if val.count("-") == 0:
      res = c; break
    for i in range(1, len(dat)+1):
      fv = flip(val, i)
      if fv not in done:
        done.add(fv)
        q.put((c+1, fv))
  print "Case #%d: %d" %(case+1, res )
