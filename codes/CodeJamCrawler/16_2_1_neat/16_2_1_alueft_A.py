t = int(raw_input())

for T in xrange(t):
  s = raw_input()
  d, a = {}, []
  for i in s:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
  if d.get('G'):
    a.extend(["8"]*d['G'])
    d['E'] -= d['G']
    d['I'] -= d['G']
    d['H'] -= d['G']
    d['T'] -= d['G']
    d['G'] -= d['G']
  if d.get('Z'):
    a.extend(["0"]*d['Z'])
    d['E'] -= d['Z']
    d['R'] -= d['Z']
    d['O'] -= d['Z']
    d['Z'] -= d['Z']
  if d.get('X'):
    a.extend(["6"]*d['X'])
    d['S'] -= d['X']
    d['I'] -= d['X']
    d['X'] -= d['X']
  if d.get('W'):
    a.extend(["2"]*d['W'])
    d['T'] -= d['W']
    d['O'] -= d['W']
    d['W'] -= d['W']
  if d.get('U'):
    a.extend(["4"]*d['U'])
    d['F'] -= d['U']
    d['O'] -= d['U']
    d['R'] -= d['U']
    d['U'] -= d['U']
  if d.get('R'):
    a.extend(["3"]*d['R'])
    d['T'] -= d['R']
    d['H'] -= d['R']
    d['E'] -= d['R']
    d['E'] -= d['R']
    d['R'] -= d['R']
  if d.get('S'):
    a.extend(["7"]*d['S'])
    d['E'] -= d['S']
    d['V'] -= d['S']
    d['E'] -= d['S']
    d['N'] -= d['S']
    d['S'] -= d['S']
  if d.get('V'):
    a.extend(["5"]*d['V'])
    d['F'] -= d['V']
    d['I'] -= d['V']
    d['E'] -= d['V']
    d['V'] -= d['V']
  if d.get('I'):
    a.extend(["9"]*d['I'])
    d['N'] -= d['I']
    d['N'] -= d['I']
    d['E'] -= d['I']
    d['I'] -= d['I']
  if d.get('E'):
    a.extend(["1"]*d['E'])
    d['O'] -= d['E']
    d['N'] -= d['E']
    d['E'] -= d['E']
  print "Case #{0}: {1}".format(T+1,"".join(sorted(a)))
