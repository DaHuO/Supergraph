import string

inputFile = open('sheep.in', 'r')
inputData = inputFile.read().strip()

numCases  = int(inputData.split('\n')[0])
cases     = inputData.split('\n')

def formatAnswer(index, answer):
  return "Case #" + str(index) + ": " + str(answer)

def computeAnswer(number):
  if number == 0:
    return "INSOMNIA"

  digitSet = set([])
  for i in xrange(1,100):
    digitSet = digitSet.union(set([ dig for dig in str(i * number)]))
    if len(digitSet) == 10:
      return i * number
  else:
    print digitSet
    print "Error on:", number
    return "INSOMNIA"


for i in xrange(1,len(cases)):
  number = int(cases[i])

  answer = computeAnswer(number)
  print formatAnswer(i, answer)


