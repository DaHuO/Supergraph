#!/usr/bin/env python

t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
  #n = [int(s) for s in raw_input().split(" ")]
  n = int(raw_input())

  limit = 100

  result = range(0, 10)
  m = n
  to_break = False

  for l in xrange(1, limit+1):
    num_str = str(n*l)
    #print "current number is {}".format(num_str)
    for c in num_str:
        #print "digit is {}".format(int(c))
        #print "leftover digits are {}".format(result)
        if int(c) in result:
          result.remove(int(c))
          if len(result) is 0:
            m = num_str
            to_break = True
            break

    if to_break:
      break

  if not to_break:
    m = "INSOMNIA"


  print "Case #{}: {}".format(i, m)

