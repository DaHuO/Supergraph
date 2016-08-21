import collections

def getPhoneNumber(phoneNum):

  occurNum = dict([(i, 0) for i in range (0, 10)])
  twoNum, sixNum, zeroNum, fourNum, heightNum = 0, 0, 0, 0, 0
  charNum = collections.defaultdict(int)
  for i in phoneNum:
    charNum[i] += 1
  
  countExpNum = collections.defaultdict(int)
  for i in phoneNum:
    if i == "W":
      occurNum[2] += 1
      for l in "TWO":
        countExpNum[l] += 1
    elif i == "X":
      occurNum[6] += 1
      for l in "SIX":
        countExpNum[l] += 1
    elif i == "Z":
      occurNum[0] += 1
      for l in "ZERO":
        countExpNum[l] += 1
    elif i == "U":
      occurNum[4] += 1
      for l in "FOUR":
        countExpNum[l] += 1
    elif i == "G":
      occurNum[8] += 1
      for l in "EIGHT":
        countExpNum[l] += 1
  
  restLetter = []
  for l, charCount in charNum.iteritems():
    if countExpNum[l] < charCount:
      for _ in xrange(charCount - countExpNum[l]):
        restLetter.append(l)
    elif countExpNum[l] > charCount:
      raise "ISSUE"
  
  countThree, countSeven = 0, 0
  for i in restLetter:
    if i == "H":
      occurNum[3] += 1
      for l in "THREE":
        countExpNum[l] += 1
    if i == 'S':
      occurNum[7] += 1
      for l in "SEVEN":
        countExpNum[l] += 1
    if i == 'O':
      occurNum[1] += 1
      for l in "ONE":
        countExpNum[l] += 1
    if i == 'F':
      occurNum[5] += 1
      for l in "FIVE":
        countExpNum[l] += 1
  
  restLetter = []
  for l, charCount in charNum.iteritems():
    if countExpNum[l] < charCount:
      for _ in xrange(charCount - countExpNum[l]):
        restLetter.append(l)
    elif countExpNum[l] > charCount:
      raise "ISSUE"
  
  occurNum[9] = len(restLetter) / 4
  res = []
  for i in range(10):
    for _ in range(occurNum[i]):
      res.append(str(i))
  return "".join(res)
  
inputPath = r'C:\Users\Nelson\Downloads\A-large.in'
outputPath = r'C:\Users\Nelson\Downloads\A_large.out'
fct = getPhoneNumber
caseNb = None
outputFile = open(outputPath, 'w')
for i, line in enumerate(open(inputPath, 'r')):
  if not caseNb:
    caseNb = int(line)
    continue
  outputFile.write('Case #%s: %s\n' % (i, fct(line.strip())))
outputFile.close()

