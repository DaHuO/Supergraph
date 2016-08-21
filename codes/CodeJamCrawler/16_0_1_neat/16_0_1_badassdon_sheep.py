import sys 
import math

T = int(sys.stdin.readline())

for case in range(T):
  N = int(sys.stdin.readline())

  if N == 0:
    print "Case #%i: INSOMNIA" % (case+1)
    continue

  i = 1
  digits = { }
  while True:
    multiple = str(N*i)
    for ch in multiple:
      digits[ch] = True

    if len(digits) == 10:
      print "Case #%i: %s" % (case+1, multiple)
      break

    i = i + 1

