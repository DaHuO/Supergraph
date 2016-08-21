import fileinput

class TestCase(object):
  def __init__(self, pan):
    self.pan = pan

def solve(t):

  happy = "+"
  sad = "-"
  
  count = 0
  seenHappy = False
  seenSad = False
  for x in list(t.pan):
    if (x == happy):
      if (seenSad):
        print "seen sad then happy"
        count = count + 1
        seenSad = False
        if (seenHappy):
          count = count + 1
      seenHappy = True
      continue

    if (x != sad):
      continue

    seenSad = True
    
  if (seenSad):
    print "sad 2 ? " + str(seenSad)
    count = count + 1
    print "seen sad at the end"
    if (seenHappy):
      count = count + 1
      print "seen sad then happy at the end"

  print "done"
  
  return count


start = True
i = 0
numberOfT = 0
testCases = []

for line in fileinput.input():
  if start:
    numberOfT = int(line)
    start = False
    continue
    
  t = TestCase(str(line))
  testCases.append(t)

i = 1
f = open('answer', 'w')
for t in testCases:
  answer = solve(t)
  f.write("Case #" + str(i) + ": " + str(answer) + "\n")
  i = i + 1


