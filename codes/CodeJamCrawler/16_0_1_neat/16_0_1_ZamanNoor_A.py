t = int(raw_input())  
s = set()
for i in xrange(1, t + 1):
  digit = int(raw_input())
  j=1
  if digit == 0:
      print "Case #{}: {}".format(i, 'INSOMNIA')
  else:
      while True:
          digitMul = digit*j
          last = digitMul
          while digitMul>0:
              mod = digitMul%10
              s.add(mod)
              digitMul = digitMul/10
          if len(s)==10:
              print "Case #{}: {}".format(i,last)
              break
          j+=1
  s.clear()
  