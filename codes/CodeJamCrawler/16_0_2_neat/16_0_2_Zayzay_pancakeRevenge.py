import sys

def pancakeRevenge(input):
  with open(input) as f:
    next(f)
    outfile = open('output.txt', 'w')
    T = 1
    for line in f:
      pancakes = list(line.rstrip())
      numFlips = 0
      lastPancake = 0
      for i in range(len(pancakes)-1):
        if pancakes[lastPancake] != pancakes[i+1]:
          flip(pancakes, lastPancake)
          numFlips += 1
        lastPancake = i+1
      if pancakes[-1] == '-':
        flip(pancakes, len(pancakes)-1)
        numFlips += 1
      outfile.write('Case #%d: %d\n' % (T, numFlips))
      T += 1

def flip(pancakes, lastPancake):
  for i in range(lastPancake+1):
    if pancakes[i] == '+':
      pancakes[i] = '-'
    elif pancakes[i] == '-':
      pancakes[i] = '+'
      
if __name__ == "__main__":
  if len(sys.argv) == 2:
    pancakeRevenge(sys.argv[1])
  else:
    print 'please specify an input file'