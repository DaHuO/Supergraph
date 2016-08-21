import sys

def getLines():
    return [line.rstrip('\n') for line in sys.stdin]

def party(index):
    return chr(65 + index)

def getMaxIndex(values, length, exclude=-1):
    maximum = 0
    maxIndex = -1
    for index in range(0, length):
        if index != exclude and maximum < values[index]:
            maximum = values[index]
            maxIndex = index
    return maxIndex

assert(getMaxIndex([1, 2, 3], 3) == 2)
assert(getMaxIndex([1, 2, 3], 3, 2) == 1)

def solve(parties, length):
    results = []
    total = 0
    for index in range(0, length):
        total += parties[index]
    while total > 0:
        value1, value2 = 0, 0
        index1 = getMaxIndex(parties, length)
        if index1 != -1:
            total -= 1
            value1 = parties[index1]
        index2 = getMaxIndex(parties, length, index1)
        if index2 != -1:
            total -= 1
            value2 = parties[index2]
        if total == 1:
            parties[index1] -= 1
            results.append(party(index1))
        elif value1 == value2:
            parties[index1] -= 1
            parties[index2] -= 1
            results.append(party(index1) + party(index2))
        elif value1 == 1:
            parties[index1] -= 1
            results.append(party(index1))
        else:
            parties[index1] -= 2
            results.append(party(index1) + party(index1))
    return results

lines = getLines()
nbCases = int(lines.pop(0))

for case in range(0, nbCases):
    nbParties = int(lines.pop(0).strip())
    parties = list(map(int, lines.pop(0).strip().split(' ')))
    answer = solve(parties, nbParties)
    print("Case #", (case + 1), ": ", " ".join(answer), sep="")
