#!/usr/bin/env python
# -*- coding: utf8 -*-

from string import digits

inputfile = 'A-large.in'
outputfile = 'large-output.op'

def solve(data):
  d = list(digits)
  dx = str(data)
  x=1
  while(len(d)>0):
    dx = str(data*x)
    for i in dx:
      if i in d: d.remove(i)
    x+=1
  return dx


if __name__ == '__main__':
  inputdata = open(inputfile, 'rb').readlines()
  cases = int(inputdata[0])
  inputdata.pop(0)
  with open(outputfile, 'wb') as out:
    for case in range(cases):
      n = inputdata[0].strip()
      if n=='0': result = 'INSOMNIA'
      else: result = solve(int(n))
      sol = 'Case #%d: %s\n' %(case+1, str(result))
      out.write(sol)
      inputdata = inputdata[1:]