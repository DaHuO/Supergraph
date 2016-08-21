#!/usr/local/bin/python

def r():
  with open('/Users/tony/Downloads/A-large.in.txt', 'r') as f:
    l = f.readlines()
    y = [x.rstrip('\n') for x in l[1:]]
    return [int(x) for x in y]
x = r()

def c(x):
  if x == 0:
    return 'INSOMNIA'

  i = 1
  n = x
  s = set(str(x))

  while True:
    y = i * n
    a = list(str(y))
    s = s.union(a)
    if len(s) == 10:
      return y
    i += 1
  
a = [c(y) for y in x]

def w(a):
  with open('a.out', 'w') as f:
    for i, x in enumerate(a):
      f.write('Case #' + str(i + 1) + ': ' + str(x) + '\n')

w(a)
