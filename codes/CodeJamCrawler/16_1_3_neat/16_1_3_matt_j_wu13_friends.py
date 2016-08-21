t = int(input())


def solve(kids):
    longestCycle = 0
    inCycle = []

    pairs = []

    chains = []
    
    for i in range(len(kids)):
        thisCycle = []
        thisCycle.append(i)
        currId = kids[i]
        while currId not in thisCycle:
            thisCycle.append(currId)
            currId = kids[currId]
        length = len(thisCycle) - thisCycle.index(currId)

        if length == 2:
            p1 = thisCycle[-2]
            p2 = thisCycle[-1]
            p1, p2 = min(p1, p2), max(p1, p2)
            if [p1, p2] not in pairs:
                pairs.append([p1, p2])

            if len(thisCycle) > 2:
                chains.append([thisCycle[-2], len(thisCycle) - 2])
        
        longestCycle = max(longestCycle, length)

    fromPairs = []
    
    for p in pairs:
        leftId = p[0]
        rightId = p[1]
        left = 0
        right = 0
        for c in chains:
            if c[0] == leftId:
                left = max(left, c[1])
            elif c[0] == rightId:
                right = max(right, c[1])
        fromPairs.append(left + right + 2)
    """
    for i in range(len(kids)):
        includedKids = []
        if i not in includedKids:
            bfid = kids[i]
            if kids[bfid] == i:
                includedKids.append(i)
                includedKids.append(bfid)
                groupByPairs += 2

                left = i
                right = bfid
                for k in range(len(kids)):
                    if k not in includedKids:
                        if kids[k] == left:
                            left = k
                            includedKids.append(k)
                            groupByPairs += 1
                        elif kids[k] == right:
                            right = k
                            includedKids.append(k)
                            groupByPairs += 1"""
                            
    return max(longestCycle, sum(fromPairs))

for i in range(1, t + 1):
    n = int(input())
    line = input()
    kids = line.split(" ")
    for j in range(len(kids)):
        kids[j] = (int(kids[j]) - 1)

    solution = solve(kids)
    
    print("Case #{}: {}".format(i, solution))
