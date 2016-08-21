t = int(raw_input())  # read a line with a single integer
for x in xrange(1, t + 1):
    N = int(raw_input())
    digits = ['\r']
    i = 0;

    while True:
      if N == 0:
        print "Case #%d: %s" % (x, "INSOMNIA")        
        break
      i = i + 1
      n = N * i
      for s in str(n):
          if s not in digits:
              digits.append(s)
      if len(digits) == 11:
          print "Case #%d: %d" % (x, n)
          break
