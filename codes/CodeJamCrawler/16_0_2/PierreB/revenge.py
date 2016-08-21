def switch(s):
  if s == '+': return '-'
  else: return '+'

def flip(line, num):
  s = [switch(l) for l in reversed(line[:num])]
  return ''.join(s)+line[num:]

def find_minus(line):
  for i in xrange(len(line)-1,-1,-1):
    if line[i] == '-': return i
  return -1

def all_plusses(slist, line):
  plusses = ''.join(['+' for i in range(len(line))])
  for l in slist:
    if l == plusses: return True
  return False

def solve(line):
  line = line.rstrip()
  slist = [line]
  j = 0
  while not all_plusses(slist, line):
    nlist = set([flip(l, i) for i in range(len(line)+1) for l in slist])
    slist = nlist
    j += 1

  return j


case = 1
with open('b.in') as f:
  next(f)
  for line in f:
    print "Case #"+str(case)+":", solve(line)
    case += 1

