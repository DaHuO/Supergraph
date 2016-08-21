#!/usr/bin/env python
# -*- coding: utf8 -*-

from string import ascii_uppercase as up

inputfile = 'A-large.in'
# inputfile = 'input.in'
outputfile = 'large-output.op'

def rem(data):
  tup = []
  while (len(tup) <= 1):
    majority = max(data)
    idx = data.index(majority)
    tup.append(idx)
    data[idx]-=1
    if sum(data) == 0 or sum(data) == 2: break
  return data, tup

def solve(N, data):
  lst = []
  while ( sum(data) != 0 ):
    data, tup = rem(data)
    lst.append(''.join(up[i] for i in tup))
  return ' '.join(lst)

if __name__ == '__main__':
  inputdata = open(inputfile, 'rb').readlines()
  cases = int(inputdata[0])
  inputdata.pop(0)
  with open(outputfile, 'wb') as out:
    for case in range(cases):
      N = int(inputdata[0])
      data = map(int, inputdata[1].split())
      out.write('Case #%d: %s\n' % (case+1, solve(N, data)))
      inputdata = inputdata[2:]