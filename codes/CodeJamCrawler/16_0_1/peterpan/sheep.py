#!/usr/bin/python

T = input()
for tcase in range(1,T+1):
  N = input()
  if N==0:
    print('Case #%d: INSOMNIA' % tcase)
    continue
  said = set([])
  n = 0
  while True:
    n += N
    said = said.union(set(str(n)))
    if len(said) >= 10:
      print('Case #%d: %d' % (tcase,n))
      break
