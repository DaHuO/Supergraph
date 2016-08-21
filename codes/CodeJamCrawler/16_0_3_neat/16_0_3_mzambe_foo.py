#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Emmanouil Zampetakis 3/10/2015
#

import sys
import array

def main():
  T = input()
  s = raw_input().split(' ')
  N = int(s[0])
  J = int(s[1])
  cnt = 0

  print "Case #1:"

  m = int(2**(N - 1) + 1)
  while cnt < J:
    sm = "{0:b}".format(m)

    ff = True
    i = 2
    dv = []
    while (i < 11) & ff:
      mm = int(sm, i)
      f = False
        
      #print mm
      j = 2
      while (j < 10000) & (not f):
        if (mm % j == 0) :
          f = True
          dv.append(j)

        j = j + 1
    
      ff = ff & f

      i = i + 1

    if ff:
      print sm,

      for i in xrange(0, 8):
        print dv[i],
        
      print dv[8]
    
      cnt = cnt + 1

    m = m + 2
    


if __name__ == '__main__':
    main()
