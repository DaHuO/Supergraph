__author__ = 'rutger'
problemName = "senate.txt"
f = open(problemName, 'w')

T = int(input())

def threeOrMoreParties(parties):
    c = 0
    for p in parties:
        if p > 0:
            c += 1
        if c > 2:
            return True
    return c > 2


def getMaxIndex(parties):
    idx = 0
    maxVal = -1
    for i in range(len(parties)):
        if parties[i] > maxVal:
            maxVal = parties[i]
            idx = i
    return idx


def twoAreEqual(parties):
    partyCopy = sorted(parties.copy(), reverse=True)
    return partyCopy[0] == partyCopy[1]


def solve(parties):
    steps = []

    while sum(parties) > 0:

        if threeOrMoreParties(parties):
            idx = getMaxIndex(parties)
            parties[idx] -= 1
            steps.append((1, idx))
        else:
            if twoAreEqual(parties):
                #keep adding
                idx1 = getMaxIndex(parties)
                nbSenators = parties[idx1]
                parties[idx1] -= 1
                idx2 = getMaxIndex(parties)
                for i in range(nbSenators):
                    steps.append((2, idx1, idx2))
                return steps
            else:
                #make them equal
                idx1 = getMaxIndex(parties)
                parties[idx1] -= 1
                steps.append((1, idx1))


def toLetter(n):
    return chr(ord("A") + n)


def prettyResult(r):
    s = ""
    for re in r:
        if re[0] == 1:
            s += " " + toLetter(re[1])
        else:
            s += " " + toLetter(re[1]) + toLetter(re[2])
    return s

for t in range(T):
    # do input
    nbParties = int(input())
    parties = list(map(int, input().split()))

    # solve input
    r = solve(parties)

    # print result
    result = prettyResult(r)
    f.write("Case #%d:%s\n" % (t+1, result))



f.close()