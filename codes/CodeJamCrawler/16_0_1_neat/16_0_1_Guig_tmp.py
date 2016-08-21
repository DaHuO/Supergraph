# yield a parsed input for every test case
def readInput(filePath):
  with open(filePath) as f:
    f.readline()
    for l in f:
      yield {'data': [int(x) for x in l.split()]}

def add(seen, n):
  for i in [int(c) for c in str(n)]:
    seen.add(i)

def solveOne(n):
  n = n[0]
  if n == 0:
    return 'INSOMNIA'

  seen = set([])
  k = 1
  while len(seen) < 10:
    add(seen, n * k)
    k += 1
  return n * k - n



def solve(inputFilePath, outputFilePath):
  with open(outputFilePath, 'w') as out:
    for i, x in enumerate(readInput(inputFilePath)):
      print 'solving case', i+1, 'for', x['data'][0]
      out.write('Case #' + str(i+1) + ': ' + str(solveOne(x['data'])) + '\n')

solve('A-large.in', 'A-small-practice.out')
