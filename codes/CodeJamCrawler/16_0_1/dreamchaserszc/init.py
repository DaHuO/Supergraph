import fileinput

class TestCase(object):
  def __init__(self, num):
    self.num = num

def solve(t):

  failed = 'INSOMNIA'

  if t.num == 0:
    return failed 

  list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  
  lastNum = t.num

  count = 1
  while (len(list1) != 0):
    lastNum = t.num * count
    print "numStr is " + str(lastNum)
    numStrList = list(str(lastNum))
    rmList = []
    for x in list1:
      print "x in list1 is " + str(x)

      #print "numStrList is " + str(numStrList)
      if (str(x) in numStrList):
        print "found in numStrList"
        rmList.append(x)
      
    for x in rmList:
      list1.remove(x)
    count = count + 1
  return lastNum

start = True
i = 0
numberOfT = 0
testCases = []

for line in fileinput.input():
  if start:
    numberOfT = int(line)
    start = False
    continue
    
  t = TestCase(int(int(line)))
  testCases.append(t)

i = 1
f = open('answer', 'w')
for t in testCases:
  answer = solve(t)
  f.write("Case #" + str(i) + ": " + str(answer) + "\n")
  i = i + 1


