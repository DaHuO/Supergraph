import sys

file = sys.stdin
def getStr():
    return (file.readline())
def getInts():
    vals = list()
    for s in file.readline().split():
        vals.append(s)
    return vals

cases = int(getStr())
for i in range(cases):
    word = getStr()
    #print(word)
    possibilties = set()
    possibilties.add(word[0])
    for c in range(1, len(word)):
        backup = set()
        if word[c] != '\n':
            for j in possibilties:
                backup.add(word[c] + j)
                backup.add(j + word[c])
            backup = sorted(backup)
            possibilties = set()
            possibilties.add(backup[-1])
    final = sorted(possibilties)
    print("Case #" + str(i + 1) + ": " + final[-1])
