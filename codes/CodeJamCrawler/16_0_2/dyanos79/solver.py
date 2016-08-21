#!/usr/bin/env python
import os,sys,string

def flip(v):
  newone = ''
  for ch in v:
    if ch == '0' or ch == '-':
      newone += '1'
    elif ch == '1' or ch == '+':
      newone += '0'
  return newone

problem = open(sys.argv[1], 'rt').readlines()
T = int(problem[0])
for i in range(0, T):
  backup = problem[i+1].strip()
  newone = backup.replace('+', '1').replace('-', '0')
  if int(newone, 2) == 2**len(newone)-1:
    print "Case #%d: 0" % (i + 1)
    continue

  # reversing
  backup, cnt = newone[::-1], 0
  for j in range(0, len(backup)):
    ch = backup[j]
    if ch == '1':
      continue

    last = 0
    for k in range(-1, -len(backup), -1):
      if backup[k] == '1':
        last = k
      else:
        break

    if last != 0:
      backup = backup[:last] + flip(backup[last:])
      cnt += 1

    backup = backup[:j] + flip(backup[j:][::-1])
    cnt += 1

  print "Case #%d: %d" % (i + 1, cnt)
