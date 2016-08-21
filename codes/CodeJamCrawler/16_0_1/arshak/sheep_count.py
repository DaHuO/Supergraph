#!/usr/bin/python

import sys;

# Extract all digits in a number.
def digs(n):
  if (n < 10):
    return [n];
  else:
    return [n % 10] + digs(n / 10);

small  = "A-small-attempt0.in"
large  = "A-large.in"
sample = "in.txt"

f = file(large);
n = int(f.next());

for i in range(n):
  k = int(f.next());
  b = [False] * 10;
  if (k == 0):
    print "Case #%d: INSOMNIA" % (i + 1);
  else:
    d = 0;
    t = k;
    while (d < 10):
      ds = digs(t);
      for x in ds:
        if (b[x] == False):
          if (d == (10 - 1)):
            d = 10;
            break;
          b[x] = True;
          d += 1;
      t += k;
    print "Case #%d: %d" % (i + 1, t - k);

