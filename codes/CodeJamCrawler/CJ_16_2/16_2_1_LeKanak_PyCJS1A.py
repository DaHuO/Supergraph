
import collections

class PyCJS1A(object):

  letter = ["ZERO", # If Z
            "ONE", ## if O
            "TWO", # if W
            "THREE", ## If H
            "FOUR", # if U
            "FIVE",
            "SIX", # if X
            "SEVEN", ## If S
            "EIGHT", # if G
            "NINE"
            ]

  def execute(self, data):

    countOccur = dict([(i, 0) for i in range (0, 10)])
    countTwo, countSix, countZero, countFour, countHuit = 0, 0, 0, 0, 0
    countPerLetter = collections.defaultdict(int)
    for i in data:
      countPerLetter[i] += 1

    countExpLetter = collections.defaultdict(int)
    for i in data:
      if i == "W":
        countOccur[2] += 1
        for l in "TWO":
          countExpLetter[l] += 1
      elif i == "X":
        countOccur[6] += 1
        for l in "SIX":
          countExpLetter[l] += 1
      elif i == "Z":
        countOccur[0] += 1
        for l in "ZERO":
          countExpLetter[l] += 1
      elif i == "U":
        countOccur[4] += 1
        for l in "FOUR":
          countExpLetter[l] += 1
      elif i == "G":
        countOccur[8] += 1
        for l in "EIGHT":
          countExpLetter[l] += 1

    restLetter = []
    for l, countL in countPerLetter.iteritems():
      if countExpLetter[l] < countL:
        for _ in xrange(countL - countExpLetter[l]):
          restLetter.append(l)
      elif countExpLetter[l] > countL:
        raise "ISSUE"

    countThree, countSeven = 0, 0
    for i in restLetter:
      if i == "H":
        countOccur[3] += 1
        for l in "THREE":
          countExpLetter[l] += 1
      if i == 'S':
        countOccur[7] += 1
        for l in "SEVEN":
          countExpLetter[l] += 1
      if i == 'O':
        countOccur[1] += 1
        for l in "ONE":
          countExpLetter[l] += 1
      if i == 'F':
        countOccur[5] += 1
        for l in "FIVE":
          countExpLetter[l] += 1

    restLetter = []
    for l, countL in countPerLetter.iteritems():
      if countExpLetter[l] < countL:
        for _ in xrange(countL - countExpLetter[l]):
          restLetter.append(l)
      elif countExpLetter[l] > countL:
        raise "ISSUE"

    countOccur[9] = len(restLetter) / 4
    res = []
    for i in range(10):
      for _ in range(countOccur[i]):
        res.append(str(i))
    return "".join(res)

if __name__ == '__main__':

  print PyCJS1A().execute("ETHER")


