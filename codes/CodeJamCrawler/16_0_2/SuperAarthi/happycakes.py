def flip(cakes):
  flip = ''
  for i in range(len(cakes)):
    cake = cakes[len(cakes)-i-1]
    if cake == '+':
      flip += '-'
    elif cake == '-':
      flip += '+'
  return flip
  
def isPlain(cakes):
  for i in range(len(cakes)):
    if cakes[i] == '-':
      return True
  return False
  
def flipAt(cakes, place):
  full = flip(cakes[:place]) + cakes[place:]
  return full

f = open('B-large.in', 'r')
out = open('happycakesOutput.txt', 'w')

numLines = f.readline()

for i in range(int(numLines)):
  line = f.readline()
  cakes = ''.join(line.split())
  
  flips = 0
  
  while isPlain(cakes):
    x = len(cakes)-1
    while x >= 0:
      if cakes[x] == '-':
        boo = x
        break
      x -= 1
    if cakes[0] == '-':
      cakes = flipAt(cakes, boo+1)
      flips += 1
    else:
      y = 0
      while y <= boo:
        if cakes[y] == '-':
          aww = y
          break
        y += 1
      cakes = flipAt(cakes, aww)
      flips += 1
      cakes = flipAt(cakes, boo+1)
      flips += 1
  out.write('Case #%d: %s\n' % (i+1, flips))