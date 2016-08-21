#!/usr/bin/python

import sys

def flip(s, n):
  top = s[:n]
  bottom = s[n:]
  ftop = ""
  for c in top:
    if c == '-':
      nc = '+'
    else:
      nc = '-'
    ftop = nc + ftop
  return ftop + bottom

def tailhappy(s):
  ls = len(s)
  for i in range(ls):
    c = s[ls-i-1]
    if c == '-':
      return i
  return ls

def headsad(s):
  ls = len(s)
  for i in range(ls):
    c = s[i]
    if c == '+':
      return i
  return ls

def headhappy(s):
  ls = len(s)
  for i in range(ls):
    c = s[i]
    if c == '-':
      return i
  return ls

T = int(sys.stdin.readline())
for test in range(T):
  print >> sys.stderr, "Test: %d" % (test+1)

  S = sys.stdin.readline().strip()
  lS = len(S)
  sol = "+" * lS
  # print >> sys.stderr, S, sol
  cache = { S:0 }

  queue = [S]
  while len(queue) > 0:
    s = queue.pop(0)
    n = cache[s]
    th = tailhappy(s)
    hs = headsad(s)
    hh = headhappy(s)
    # print >> sys.stderr, s, n, th, hs, hh
    if th >= lS:
      break

    if hs > 0:
      f = [ hs ]
    else:
      # f = range(1, 1 + lS - th)
      f = [ hh ]
    for i in f:
    # for i in reversed(range(1, 1 + lS - th)):
      ns = flip(s, i)
      if ns not in cache or cache[ns] > (n+1):
        cache[ns] = n + 1
        queue.append(ns)
        # print >> sys.stderr, cache

  print "Case #%d: %d" % (test+1, cache[sol])

