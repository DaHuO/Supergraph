import string

inputFile = open('pancakes-large.in', 'r')
inputData = inputFile.read().strip()

numCases  = int(inputData.split('\n')[0])
cases     = inputData.split('\n')

def formatAnswer(index, answer):
  return "Case #" + str(index) + ": " + str(answer)

def computeAnswer(pancakeString):
  currentLetter = pancakeString[0]
  count         = 0
  for nextLetter in pancakeString[1:]:
    if currentLetter != nextLetter:
      count         += 1
      currentLetter  = nextLetter

  return count

for case in xrange(1,len(cases)):
  pancakeString = cases[case].strip() + "+"
  answer        = computeAnswer(pancakeString)

  print formatAnswer(case, answer)


