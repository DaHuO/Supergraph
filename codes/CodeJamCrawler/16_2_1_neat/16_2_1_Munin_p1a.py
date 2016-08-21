#!/usr/bin/env python
import os
import sys
import time

tStart = time.time()

#---------------------------------------------------------------------

ifilename = 'input.in'
ofilename = 'results.out'

args = sys.argv
if len(args) > 1:
  ifilename = args[1]
if len(args) > 2:
  ofilename = args[2]

#---------------------------------------------------------------------
 
ifile = open(ifilename,'r')
data  = ifile.read()
ifile.close()
lines = data.splitlines()
ofile = open(ofilename, 'w')

#---------------------------------------------------------------------
# Functions

numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def get_number(text):

  if len(text) == 0:
    return []

  for k,num in enumerate(numbers):
    text_tmp = text[:]
    ok = 1
    for c in num:
      if c in text_tmp:
        text_tmp.remove(c)
      else:
        ok = 0
        break
    if ok == 1:
      nn = get_number(text_tmp)
      if nn != 0:
        return [k]+nn
  return 0

#---------------------------------------------------------------------
# Main
ncases = int(lines[0])
lines  = lines[1:]
for ncase in xrange(ncases):
  text  = lines[0]
  lines = lines[1:]

  solution = ''
  for n in get_number([c for c in text]):
    solution = solution + str(n)

  # -------------------------------------------------
  res = 'Case #%d: %s'%(ncase+1, solution)
  ofile.write('%s\n'%(res))
  print res

#---------------------------------------------------------------------

ofile.close()

print '\n Run time = ' + str((time.time() - tStart))     
