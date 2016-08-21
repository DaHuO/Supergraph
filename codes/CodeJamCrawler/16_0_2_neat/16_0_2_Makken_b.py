
def handlePancakes(pancakes):
    if allOfSame(pancakes, '+'):
        return 0
    elif allOfSame(pancakes, '-'):
        return 1

    if pancakes[-1] == '-':
        return 1 + handlePancakes(invertPancakes(pancakes))
    else:
        return handlePancakes(pancakes[0:-1])

def invertPancakes(pancakes):
    ret = []
    for item in pancakes:
        if item is '+':
            ret.append('-')
        else:
            ret.append('+')
    return "".join(ret)

def allOfSame(pancakes, sign):
    return pancakes.count(sign) == len(pancakes)

def isDone(pancakes):
    return pancakes.count('+') == len(pancakes)

def isAlternating(pancakes):
    everySecondElem = pancakes[0::2]
    everySecondElemOffs = pancakes[1::2]

    return everySecondElem.count(everySecondElem[0]) == len(everySecondElem) and everySecondElemOffs.count(everySecondElemOffs[0]) == len(everySecondElemOffs)

f = open("dataset.txt", "r")
o = open("output.txt", "w")

numberOfCases = int(f.readline())

for item in range(0,numberOfCases):
    current = f.readline().replace("\n","")
    string = "Case #{}: {}\n".format(item + 1,handlePancakes(current))
    o.writelines(string)


