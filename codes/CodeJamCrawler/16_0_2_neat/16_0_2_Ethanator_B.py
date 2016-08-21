#!/usr/bin/python -tt
import itertools
import sys

def flip(s):
  res = ""
  for i in xrange(len(s)):
    a = s[i]
    if a == "+":
      res = "-" + res
    elif a == "-":
      res = "+" + res
  return res

def pan(s):
  if len(s) == 0: return 0
  if s == "+": return 0
  if s == "-": return 1
  r_plus = len(s)
  while r_plus > 0 and s[r_plus - 1] == "+":
    r_plus -= 1
  if r_plus < len(s):
    return pan(s[:r_plus])
  l_minus = -1
  while l_minus < len(s) - 1 and s[l_minus + 1] == "-":
    l_minus += 1
  if l_minus > -1:
    return 1 + pan(flip(s))
  l_plus = -1
  while l_plus < len(s) - 1 and s[l_plus + 1] == "+":
    l_plus += 1
  return 1 + pan(flip(s[:l_plus+1])+s[l_plus+1:])

n = int(raw_input())
for i in xrange(n):
  s = raw_input().rstrip()
  print "Case #" + str(i+1) + ": " + str(pan(s))
