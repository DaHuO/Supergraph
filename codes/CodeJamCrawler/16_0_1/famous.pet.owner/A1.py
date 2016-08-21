
def sleeploop(original_number,factor):
  if original_number*(factor+1) == original_number:
    return "INSOMNIA"
  elif digits == [1]*10:
    return int(original_number*(factor-1))
  else:
    for f in str(original_number*factor):
      digits[int(f)] = 1
#    print digits
#    print original_number*factor
    return sleeploop(original_number,factor+1)

t = int(raw_input())
for i in xrange(1,t+1):
  n = [int(s) for s in raw_input().split(" ")]
  
  digits = [0]*10
  print "Case #{}: {}".format(i,sleeploop(n[0],1))
