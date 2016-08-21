import collections

class PyCJS13A(object):

  alphabet = ['A', 'B', 'C', 'D']

  def getBiggestPartie(self, countParties):
    maxPartie, res = 1, []
    for partie, countPartie in countParties.iteritems():
      if countPartie > maxPartie:
        res = [partie]
        maxPartie = countPartie
      elif countPartie == maxPartie:
        res.append(partie)
    return res

  def execute(self, data):
    """
    """

    parties = int(data[0])
    subSetofParties = []
    for i in xrange(int(data[0])):
      subSetofParties.append(chr(65 + i))
    vals, countParties = collections.defaultdict(list), collections.defaultdict(int)
    for i, num in enumerate(data[1].split(" ")):
      for j in range(int(num)):
        vals[subSetofParties[i]].append(subSetofParties[i])
        countParties[subSetofParties[i]] += 1

    biggestParties = self.getBiggestPartie(countParties)
    grpParties = []
    while biggestParties:
      if len(biggestParties) % 2 == 1:
        grpParties.append(biggestParties[0])
        countParties[biggestParties[0]] -= 1
        del biggestParties[0]
      for i in range(len(biggestParties)/2):
        grpParties.append("%s%s" % (biggestParties[i], biggestParties[i + len(biggestParties)/2]))
        countParties[biggestParties[i]] -= 1
        countParties[biggestParties[i + len(biggestParties)/2]] -= 1

      biggestParties = self.getBiggestPartie(countParties)

    return " ".join(grpParties)

if __name__ == '__main__':
  """ """
  #print PyCJS13A().execute(data)