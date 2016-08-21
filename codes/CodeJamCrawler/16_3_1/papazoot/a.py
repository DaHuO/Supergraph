from Solve import *
from collections import Counter

asciA = 65

def evacuation(args):
    nParties = int(args[0])
    countsList = map(int, args[1].split())
    countsMap = {}
    for i in range(nParties):
        countsMap[i] = countsList[i]
    counts = Counter(countsMap)

    totalCount = sum(countsList)
    evacuationPlan = []
    while totalCount > 0:
        a, b = counts.most_common(2)
        if totalCount == 3:
            sub = {a[0]:1}
            counts.subtract(sub)
            totalCount -= 1
            evacuationPlan.append(toChar(a[0]))
        elif a[1] == b[1]:
            sub = {a[0]:1, b[0]:1}
            counts.subtract(sub)
            totalCount -= 2
            evacuationPlan.append(toChar(a[0]) + toChar(b[0]))
        else:
            if totalCount == 4:
                sub = {a[0]:2}
                counts.subtract(sub)
                totalCount -= 2
                evacuationPlan.append(toChar(a[0]) + toChar(a[0]))
            else:
                sub = {a[0]:1}
                counts.subtract(sub)
                totalCount -= 1
                evacuationPlan.append(toChar(a[0]))
        
    return " ".join(evacuationPlan)

def toChar(index):
    return str(unichr(index+asciA))
                
if __name__ == "__main__":
    solveF("A-large.in", evacuation, 2)
