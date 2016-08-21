import os

def check_finish(pancake):
  for c in pancake:
    if c != '+':
      return False
  return True

def flip_pancake(pancake, pos):
  new_pancakge = ''
  for i in xrange(pos):
    if pancake[pos-i-1] == '+':
      new_pancakge += '-'
    else:
      new_pancakge += '+'
  new_pancakge += pancake[pos:]
  return new_pancakge

def bfs(pancake):
  length = len(pancake)
  current_pancakes = [pancake]
  next_pancakes = []
  visited = set([pancake])
  step = 0
  while True:
    for p in current_pancakes:
      if check_finish(p):
        return step

    next_pancakes = []
    for p in current_pancakes:
      for i in xrange(1,length+1):
        next_p = flip_pancake(p, i)
        if next_p not in visited:
          visited.add(next_p)
          next_pancakes.append(next_p)
    current_pancakes = next_pancakes
    step += 1

  return step

fin = open('B-small-attempt0.in', 'r')
fout = open('B.out', 'w')
for i, line in enumerate(fin):
  if i == 0:
    t = int(line)
    continue

  pancake = line.strip()
  res = bfs(pancake)

  out_str = 'Case #%d: %s' % (i, res)
  print out_str
  fout.write(out_str + '\n')
fin.close()
fout.close()
