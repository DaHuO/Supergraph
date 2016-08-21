#!/usr/bin/env python
# -*- coding: utf8 -*-

inputfile = 'B-large.in'
outputfile = 'large-output.op'

def solve(data):
  pat = ['-', '+']
  if data[-1]==pat[0]: count=1
  else: count=0
  for i in range(len(data)-1):
    if data[i] != data[i+1]:
      count+=1
  return count

if __name__ == '__main__':
  inputdata = open(inputfile, 'rb').readlines()
  cases = int(inputdata[0])
  inputdata.pop(0)
  with open(outputfile, 'wb') as out:
    for case in range(cases):
      data = inputdata[0].strip()
      result = solve(data)
      sol = 'Case #%d: %d\n'%(case+1, result)
      out.write(sol)
      inputdata = inputdata[1:]