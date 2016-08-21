#!/usr/bin/env python

import sys

if __name__ == '__main__':
  T = int(sys.stdin.readline())
  for i in xrange(T):
    K, C, S = (int(c) for c in sys.stdin.readline().split(" "))
    A = " ".join(str(1 + x * K**(C-1)) for x in xrange(K))
    print "Case #%d: %s" % (i + 1, A)
