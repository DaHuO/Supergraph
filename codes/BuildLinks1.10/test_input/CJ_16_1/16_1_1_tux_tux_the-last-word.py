#!/usr/bin/env python
# -*- coding: utf8 -*-

from string import ascii_lowercase as al

inputfile = 'A-large.in'
outputfile = 'large-output.op'

if __name__ == '__main__':
  inputdata = open(inputfile, 'rb').readlines()
  cases = int(inputdata[0])
  inputdata.pop(0)
  with open(outputfile, 'wb') as out:
    for case in range(cases):
      S = inputdata[0].strip().lower()
      s = S[0]
      for i in S[1:]:
        idx = al.index(i)
        if idx >= al.index(s[0]):
          s = i+s
        else: s+=i
      out.write('Case #%d: %s\n'%(case+1, s.upper()))
      inputdata = inputdata[1:]