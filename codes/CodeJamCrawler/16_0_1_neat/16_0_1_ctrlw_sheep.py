#!/usr/bin/python3
import sys, math, re

MAX = 1000000 * 1000000
ALL_DIGITS = 1023
INSOMNIA = "INSOMNIA"
cache = {0: INSOMNIA}

def int2mask(x):
  if x == 0:
    return 1
  
  result = 0
  while x > 0:
    [x, rest] = divmod(x, 10)
    result |= (1 << rest)
  return result

def count_cycles(n):
  #check cache
  if n in cache:
    return cache[n]
  
  digits = 0
  current = 0
  result = INSOMNIA
  while current < MAX and digits != ALL_DIGITS:
    current += n
    digits |= int2mask(current)
  if digits == ALL_DIGITS:
    result = str(current)
    
  #put into cache
  cache[n] = result
  return result


T = int(sys.stdin.readline())
for t in range(T):
  N = int(sys.stdin.readline())
  result = count_cycles(N)

  print("Case #%d: %s" % (t + 1, result))
