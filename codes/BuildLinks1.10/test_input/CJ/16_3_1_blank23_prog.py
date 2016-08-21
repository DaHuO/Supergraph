def sortTuplesByPos(tuples, pos):
    tuples = sorted(tuples, key=lambda x: x[pos])
    return tuples

def update(tuples):
    for x in xrange(len(tuples)-1, -1, -1):
        if tuples[x][1] == 0:
            tuples.pop(x)

f = open("A-small-attempt0.in", "r")
g = open("A-small-attempt0.out", "w")

cases = int(f.readline())
for h in xrange(cases):
    f.readline()
    parties = map(int, f.readline().split())
    
    result = []
    pTuples = []
    for i in xrange(len(parties)):
        tuple = [chr(i+65), parties[i]]
        pTuples.append(tuple)
    
    pTuples = sortTuplesByPos(pTuples, 1)
    pTuples.reverse()
    result.append(pTuples[0][0] + pTuples[1][0])
    pTuples[0][1], pTuples[1][1] = pTuples[0][1]-1, pTuples[1][1]-1
    update(pTuples)
    
    while len(pTuples) != 0:
        pTuples = sortTuplesByPos(pTuples, 1)
        pTuples.reverse()
        
        if len(pTuples) > 1:
            if pTuples[0][1] == pTuples[1][1]+1 or pTuples[0][1]+1 == pTuples[1][1] or pTuples[0][1] == pTuples[1][1]:
                result.append(pTuples[0][0] + pTuples[1][0])
                pTuples[0][1], pTuples[1][1] = pTuples[0][1]-1, pTuples[1][1]-1
            else:
                result.append(pTuples[0][0])
                pTuples[0][1] = pTuples[0][1]-1
        else:
            result.append(pTuples[0][0])
            pTuples[0][1] = pTuples[0][1]-1
             
        update(pTuples)
    
    result.reverse()
    strResult = (" ").join(result)
    g.write("Case #" + str(h+1) + ": " + strResult + "\n")