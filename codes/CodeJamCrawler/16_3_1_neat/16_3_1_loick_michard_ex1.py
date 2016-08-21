n=input()

def compute(p, ss):
  while True:
    maxi = -1
    maxis = []
    total = 0
    idx = 0
    for s in ss:
      total += s
      if s > maxi:
        maxi = s
        maxis = [idx]
      elif s == maxi:
        maxis.append(idx)
      idx += 1
    if total == 0:
      return
    if len(maxis) % 2 == 0:
      print 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[maxis[0]] + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[maxis[1]],
      ss[maxis[0]] -= 1
      ss[maxis[1]] -= 1
    else:
      print 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[maxis[0]],
      ss[maxis[0]] -= 1



for x in xrange(n):
  p = input()
  s = map(int, raw_input().split(' '))
  print 'Case #'+str(x+1)+':',
  compute(p, s)
  print