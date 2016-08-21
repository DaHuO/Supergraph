def sol(n):
  if n == 0:
    return "INSOMNIA"
  else:
    i = n
    digit = {}
    while True:
      for c in str(i):
        if c not in digit:
          digit[c] = 1
      if len(digit) == 10:
        return i
      else:
        i += n

t = long(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, sol(n))
