import sys

def getStr(line):
    return line.strip().split()

def getInt(line):
    return [int(i) for i in getStr(line)]

################################################################################

def checkMajority(partyPairs, people):
    if len(partyPairs) > 0:
        return partyPairs[0][0] > people / 2
    return False

def solve(partyPairs, people):
    steps = []
    start = 0
    first = None
    while people > 0:
        for p1 in range(start, len(partyPairs)-1):
            p2 = p1+1
            if partyPairs[p1][0] > partyPairs[p2][0]:
                party = partyPairs[p1][1]

                people -= 1
                start = max(0, p1-1)
                partyPairs[p1][0] -= 1

                if first:
                    if checkMajority(partyPairs, people):
                        steps.append(first)
                        first = party
                    else:
                        steps.append(first+party)
                        first = None
                else:
                    first = party
                break
        else:
            party = partyPairs[-1][1]

            people -= 1
            start = max(0, len(partyPairs)-2)

            if partyPairs[-1][0] > 1:
                partyPairs[-1][0] -= 1
            else:
                partyPairs.pop()

            if first:
                if checkMajority(partyPairs, people):
                    steps.append(first)
                    first = party
                else:
                    steps.append(first+party)
                    first = None
            else:
                first = party
    return " ".join(steps)

################################################################################

lines = sys.stdin.readlines()
L = 0
cases, = getInt(lines[L])
L += 1
for case in range(1, cases+1):
    N, = getInt(lines[L])
    L += 1
    P = getInt(lines[L])
    L += 1

    people = 0
    partyPairs = []
    for p, members in enumerate(P):
        party = chr(ord("A")+p)
        partyPairs.append([members, party])
        people += members

    partyPairs.sort()
    partyPairs.reverse()

    result = solve(partyPairs, people)
    print("Case #{}: {}".format(case, result))
