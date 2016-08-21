FILE_NAME = "B-large";

def processAndGetResult(line):
    pancakes = []
    for p in line:
        if p == "+":
            pancakes.append(1)
        elif p == "-":
            pancakes.append(0)
    return str(getResult(pancakes))

def checkIfSideUp(pancakes):
    s = set(pancakes)
    if 0 in s:
        return False
    return True

def flip(pancakes, i):
    for j in xrange(0, i+1):
        if pancakes[j] == 1:
            pancakes[j] = 0
        else:
            pancakes[j] = 1
    return pancakes

def getResult(pancakes):
    count = 0
    if checkIfSideUp(pancakes):
        return count
    for i in xrange(len(pancakes) - 1, -1, -1):
        if pancakes[i] == 0:
            pancakes = flip(pancakes, i)
            count += 1
            if checkIfSideUp(pancakes):
                return count


def main():
    with open("./"+FILE_NAME+".in", "r") as f:
        with open("./"+FILE_NAME+".out", "w") as r:
            first = True
            j = 0
            for line in f:
                if first == True:
                    first = False
                    continue
                j += 1
                res = processAndGetResult(line)
                r.write("Case #"+ str(j) + ": " + res + "\n")


if __name__ == '__main__':
    main()
