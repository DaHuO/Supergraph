# yield a parsed input for every test case
def readInput(filePath):
  with open(filePath) as f:
    f.readline()
    for l in f:
      yield {'data': [x for x in l.strip()]}

def solveOne(n):
  splits = sum((n[i-1] != n[i] for i in range(1, len(n))))
  if n[-1] == '+':
    return splits
  return splits + 1


def solve(inputFilePath, outputFilePath):
  with open(outputFilePath, 'w') as out:
    for i, x in enumerate(readInput(inputFilePath)):
      out.write('Case #' + str(i+1) + ': ' + str(solveOne(x['data'])) + '\n')

solve('B-large.in', 'A-small-practice.out')
