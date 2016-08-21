import sys
sys.setrecursionlimit(100000)

fileIn = "B-small-attempt1.in"#""B-small-attempt0.in"# "sheep-test"
fileOut = fileIn + "-out"


def simplify(pile):
    for i, v in enumerate(reversed(pile)):
        if v == '-':
            return pile[0:len(pile)-i]
    return []


def turn_pile(pile, index):
    pile2 = pile[:]
    for i in range(index+1):
        if pile[i] == '-':
            pile2[index-i] = '+'
        else:
            pile2[index - i] = '-'

    return pile2


def solve_level(pile):
    if len(pile) == 0:
        return True
    return False


def contains(lines, pile):
    for p in lines:
        count = 0
        if len(p) != len(pile):
            continue

        for i,v in enumerate(p):
            if pile[i] == v:
                count += 1
        if count == len(p):
            return True

def solve(pile):
    print pile
    level = 0
    lines = [simplify(pile)]

    while True:
        # Solve a Line
        lines2 = []
        print len(lines)

        for p in lines:
            if solve_level(p):
                return level

            # Add all returning for this line
            for i in range(len(p)):
                nextPile = simplify(turn_pile(p, i))
                if not contains(lines2, nextPile):
                    lines2.append(nextPile)
        level += 1
        lines = lines2


# OutPut function
def writeLine(i, value):
    fileout.write("Case #" + str(i) + ": " + str(value) + "\n")
    print "return value : " + str(value)


# Read the Input
file = open(fileIn, "r")
fileout = open(fileOut, "w")
readIndex = 0
print "Starting the Algo"

for n in file.readlines():
    if readIndex == 0:
        count = n
        readIndex += 1

    else:
        liste = list(n)
        end = liste[len(liste)-1]
        if (end != '-') and (end != '+'):
            liste = liste[0:len(liste)-1]

        value = solve(liste)
        writeLine(readIndex, value)
        readIndex += 1

fileout.close();
file.close();


