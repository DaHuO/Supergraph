__author__ = 'rutger'

def goodCycle(c, f):
    for i in range(len(c)):
        next = c[(i + 1) % len(c)]
        prev = c[i - 1]
        curr = c[i]
        bff = f[curr] - 1
        if next != bff and prev != bff:
            return False
    return True


problemName = "bff.txt"
f = open(problemName, 'w')


def getLength(idx, friends):
    seen = [False] * len(friends)

    current = friends[idx]
    while not seen[current - 1]:
        seen[current - 1] = True
        current = friends[current - 1]

    cycle = []
    for i in range(len(seen)):
        if seen[i]:
            cycle.append(i)

    return cycle



def findCycle(idx, friends):
    seen = [False] * len(friends)
    seen[idx] = True

    c = [idx]

    current = friends[idx] - 1
    while not seen[current]:
        c.append(current)
        seen[current] = True
        current = friends[current] - 1
    if idx == current:
        return True, c
    else:
        return False, []

def getLongestAlt(cycle, length, friends):
    partOfCycle = [False] * length
    for el in cycle:
        partOfCycle[el] = True

    if sum(partOfCycle) > 2:
        return sum(partOfCycle)


    pathToA = 0
    pathToB = 0
    a = cycle[0]
    b = cycle[1]
    for i in range(length):
        if i != a and i != b:
            seen2 = [False] * length
            seen2[i] = True
            current = friends[i] - 1
            while not seen2[current]:
                if current == a:
                    pathToA = max(sum(seen2), pathToA)
                    break
                elif current == b:
                    pathToB = max(sum(seen2), pathToB)
                    break
                else:
                    seen2[current] = True
                    current = friends[current] - 1
    return max(pathToB, pathToA) + sum(partOfCycle)


def getLongest(cycle, length, friends):
    partOfCycle = [False] * length
    for el in cycle:
        partOfCycle[el] = True

    if sum(partOfCycle) > 2:
        return sum(partOfCycle)


    pathToA = 0
    pathToB = 0
    a = cycle[0]
    b = cycle[1]
    for i in range(length):
        if i != a and i != b:
            seen2 = [False] * length
            seen2[i] = True
            current = friends[i] - 1
            while not seen2[current]:
                if current == a:
                    pathToA = max(sum(seen2), pathToA)
                    break
                elif current == b:
                    pathToB = max(sum(seen2), pathToB)
                    break
                else:
                    seen2[current] = True
                    current = friends[current] - 1
    return pathToA + pathToB + sum(partOfCycle)


def solve(friends):
    partOfCycle = [False] * len(friends)
    cycles = []
    for i in range(len(friends)):
        if partOfCycle[i]:
            continue
        isCycle, cycle = findCycle(i, friends)
        if isCycle:
            cycles.append(cycle)
            for el in cycle:
                partOfCycle[el] = True

    maxLength = 0
    for cycle in cycles:
        l = getLongest(cycle, len(friends), friends)
        maxLength = max(l, maxLength)

    sumOfAllCycles = 0
    maxPaths = [0,0]
    for cycle in cycles:
        if len(cycle) == 2:
            sumOfAllCycles += len(cycle)
            l = getLongest(cycle, len(friends), friends)
            maxPaths.append(l)

    maxPaths = sorted(maxPaths, reverse=True)

    return max(maxLength, sum(maxPaths))

T = int(input())
for t in range(T):
    nbKids = int(input())
    friends = list(map(int, input().split()))

    result = solve(friends)
    f.write("Case #%d: %d\n" % (t+1, result))
    print("Case #%d: %d" % (t+1, result))


f.close()