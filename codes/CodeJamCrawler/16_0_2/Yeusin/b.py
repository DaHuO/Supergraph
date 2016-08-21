#!/bin/python
case = 0
q = []
history = {}
fcount = 99999999999999


def flip(x, a):
  rn = reversed(x)
  nn = ""
  for item in rn:
    nn += '-' if item == '+' else '+'
  if nn not in history or history[nn] > a:
    history[nn] = a
    q.append((nn, a))
    # print q

  for i in range(1, len(x)):
    rn = reversed(x[:i])
    nn = ""
    for item in rn:
      nn += '-' if item == '+' else '+'

    n = nn + x[i:]
    if n not in history or history[n] > a:
      history[n] = a
      q.append((n, a))
      # print q


def run():
  global fcount
  while len(q) > 0:
    for item in q:
      if '-' not in item[0]:
        if fcount > item[1]:
          fcount = item[1]

    x, a = q.pop()
    if a + 1 < fcount:
      flip(x, a + 1)


t = input()
for i in range(1, t + 1):
  n = raw_input()
  q = []
  history = {}
  fcount = 999999999999999
  case = i
  history[n] = 0
  q.append((n, 0))
  run()
  print "Case #{}: {}".format(case, fcount)
