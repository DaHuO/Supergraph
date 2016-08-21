from collections import defaultdict
import sys
import fileinput

class TestCase(object):
  def findMissing(self):
    table = defaultdict(lambda: 0)
    for l in self.numList:
      for x in l:
        table[int(x)] = table[int(x)] ^ 1
    missingList = []
    keys = table.keys()
    keys.sort()
    for x in keys:
      if table[x] == 1:
        missingList.append(x)
    return missingList

  def __init__(self, numList):
    self.numList = numList
    self.missingList = self.findMissing()
    print self.missingList

def solve(t):

  return ' '.join(str(item) for item in t.missingList)

start = True
i = 0
numberOfT = 0
testCases = []

with open(sys.argv[1]) as f:
  if start:
    numberOfT = int(f.readline())
    start = False
  count = 0

  while count < numberOfT:
    gridN = int(f.readline())
    totalLines = 2 * gridN - 1
    lineCount = 0
    dataList = []
    while lineCount < totalLines:
      data = [x for x in f.readline().split()]
      dataList.append(data)
      lineCount = lineCount + 1
    t = TestCase(dataList)
    testCases.append(t)
    count = count + 1

i = 1
f = open('answer', 'w')
for t in testCases:
  answer = solve(t)
  f.write("Case #" + str(i) + ": " + str(answer) + "\n")
  i = i + 1


