import string

inputFile = open('phone-large.in', 'r')
inputData = inputFile.read().strip()

numCases  = int(inputData.split('\n')[0])
cases     = inputData.split('\n')

def formatAnswer(index, answer):
  return "Case #" + str(index) + ": " + str(answer)

def getLetterDict(letterDigits):
  letterDict = dict()
  for letter in letterDigits:
    try:
      letterDict[letter] += 1
    except:
      letterDict[letter] = 1
  return letterDict


def removeForNumber(letterDict, definingLetter, letters):
  if definingLetter not in letterDict or letterDict[definingLetter] == 0:
    return 0
  count = letterDict[definingLetter]
  for letter in letters:
    letterDict[letter] -= count
  return count


def computeAnswer(letterDigits):
  letterDict = getLetterDict(letterDigits)
  answer     = ''
  for (number, definingLetter, letters) in [ ('0', 'Z', 'ZERO'), ('8', 'G', 'EIGHT'), ('4', 'U', 'FOUR'), ('5', 'F', 'FIVE'), ('7', 'V', 'SEVEN'), ('2', 'W', 'TWO'), ('6', 'X', 'SIX'), ('1', 'O', 'ONE'), ('9', 'I', 'NINE'), ('3', 'T', 'THREE')]:
    answer += number * removeForNumber(letterDict, definingLetter, letters)

  return string.join(sorted(answer), '')

for case in xrange(1, numCases+1):
  letterDigits = cases[case]

  answer = computeAnswer(letterDigits)
  print formatAnswer(case, answer)


'ZERO','ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'

"""
'ZERO','ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'


Z -> ZERO
G -> EIGHT
U -> FOUR
F -> FIVE
V -> SEVEN
W -> TWO
X -> SIX
O -> ONE
N -> NINE
Rest -> THREE




"""
