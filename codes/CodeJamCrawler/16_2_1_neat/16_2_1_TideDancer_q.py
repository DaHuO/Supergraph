import numpy

t = int(raw_input())  # read a line with a single integer

for j in xrange(1, t + 1):
  S = [str(s) for s in raw_input().split(" ")] 
  S = S[0]

  c = {}

  for e in S:
    if e in c:
      c[e] = c[e] + 1
    else:
      c.update({e: 1})

  number = []

  if 'Z' in c:
    for i in range(c['Z']):
      number.append(0)
      c['Z'] = c['Z'] - 1
      c['E'] = c['E'] - 1
      c['R'] = c['R'] - 1
      c['O'] = c['O'] - 1
  if 'W' in c:
    for i in range(c['W']):
      number.append(2)
      c['T'] = c['T'] - 1
      c['W'] = c['W'] - 1
      c['O'] = c['O'] - 1
  if 'U' in c:
    for i in range(c['U']):
      number.append(4)
      c['F'] = c['F'] - 1
      c['U'] = c['U'] - 1
      c['R'] = c['R'] - 1
      c['O'] = c['O'] - 1
  if 'X' in c:
    for i in range(c['X']):
      number.append(6)
      c['S'] = c['S'] - 1
      c['I'] = c['I'] - 1
      c['X'] = c['X'] - 1
  if 'G' in c:
    for i in range(c['G']):
      number.append(8)
      c['E'] = c['E'] - 1
      c['I'] = c['I'] - 1
      c['G'] = c['G'] - 1
      c['H'] = c['H'] - 1
      c['T'] = c['T'] - 1

# after this
  if 'O' in c:
    for i in range(c['O']):
      number.append(1)
      c['O'] = c['O'] - 1
      c['N'] = c['N'] - 1
      c['E'] = c['E'] - 1
  if 'S' in c:
    for i in range(c['S']):
      number.append(7)
      c['S'] = c['S'] - 1
      c['E'] = c['E'] - 2
      c['V'] = c['V'] - 1
      c['N'] = c['N'] - 1
  if 'V' in c:
    for i in range(c['V']):
      number.append(5)
      c['F'] = c['F'] - 1
      c['I'] = c['I'] - 1
      c['V'] = c['V'] - 1
      c['E'] = c['E'] - 1
  if 'R' in c:
    for i in range(c['R']):
      number.append(3)
      c['T'] = c['T'] - 1
      c['H'] = c['H'] - 1
      c['E'] = c['E'] - 2
      c['R'] = c['R'] - 1
  
  if 'I' in c: 
    for i in range(c['I']):
      number.append(9)

  number.sort()

  print "Case #{}: {}".format(j, ''.join(str(x) for x in number))
