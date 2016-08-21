def unbalanced(parties):
    roomTotal = sum(parties.values())
    for party in parties:
        if ((float(parties[party]) / float(roomTotal)) > 0.5):
            return True
    return False

def getNextStep(parties):
    majorityParty = max(parties, key=parties.get)
    if sum(parties.values()) == 3:
        return majorityParty
    testStep = majorityParty * 2;
    testParties = parties.copy()
    testParties[majorityParty] -= 2
    if unbalanced(testParties):
        del testParties[majorityParty]
        secondParty = max(testParties, key=parties.get)
        return majorityParty + secondParty
    else:
        return testStep

def solve(parties):
    steps = ""
    while(sum(parties.values()) > 2):
        nextStep = getNextStep(parties)
        steps += nextStep + " ";
        for party in list(nextStep):
            parties[party] -= 1
    steps += "".join(list(filter(parties.get, parties)))
    return steps

t = int(input())
partyNames = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for i in range(1, t + 1):
  p = int(input())
  parties = {};
  sdfasd = input();
  partyCount = [int(x) for x in sdfasd.split(" ")];
  for j in range(0, p):
      parties[partyNames[j]] = partyCount[j]
  print("Case #{}: {}".format(i, solve(parties)))