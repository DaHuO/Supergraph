import sys

def analyze (a, s, last):
  if s == '':
    return a
  if last == '':
    a=[1]
    return analyze(a, s[1:], s[0])
  if last == s[0]:
    a[len(a) - 1] = a[len(a) - 1] + 1
    return analyze(a, s[1:], s[0])
  a.append(1)
  return analyze(a, s[1:], s[0])

def flip (l):
  r = []
  for e in l:
    r.append(1 - e)
  return r

def steps (ss, target):
  # print 'mod: ' + str(ss) + ', target: ' + str(target)
  if len(ss) == 0:
    return 0
  if ss[:-1] == target:
    ss = ss[:-1]
  if len(ss) == 0:
    return 0
  if len(ss) == 1:
    return 1
  split = len(ss) / 2
  return steps(ss[0:split], target) + steps(flip(ss[split:]), target)

def f (i, s):
  a = analyze([], s, '')
  if s[-1] == '+':
    a = a[:-1]
  ss = [1, 0] * (len(a) / 2)
  if len(a) % 2 == 1:
    ss = [0] + ss
  # print 'Case #' + str(i) + ': ' + s + ', ' + str(ss) + ', ' + str(steps(ss, 1))
  print 'Case #' + str(i) + ': ' + str(steps(ss, 1))

i = 0
for line in sys.stdin:
  i += 1
  if i == 1:
    continue
  f(i-1, line[:-1])

