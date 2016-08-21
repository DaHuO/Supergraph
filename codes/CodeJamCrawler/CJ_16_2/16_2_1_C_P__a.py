# Google Code Jam 1B Round - Problem A
def getFiles(name):
    return open(name + '.in', 'r'), open(name + '.out', 'w')

name = 'example'
name = 'A-small-attempt0'
name = 'A-large'

inFile, outFile = getFiles(name)

# Converts character to appropriate index (0 - 25)
def getIndex(char):
    return ord(char) - 65

def getChar(index):
    return chr(index + 65)

def getValue(S):

    buckets = [0 for i in range(26)]

    numbers = [0 for i in range(10)]

    # increment buckets for each of the letters
    for c in S:
        index = getIndex(c)
        if index > -1:
            buckets[index] += 1

   # Z -> zero
   # W -> two
   # X -> six
   # G -> eight
   # U -> four
   # O -> one
   # S -> seven
   # V -> five
   # H -> three
   # E -> nine

    # Find all Z's and pull out zero
    z = buckets[getIndex('Z')]
    for i in range(z):
        buckets[getIndex('E')] -= 1
        buckets[getIndex('R')] -= 1
        buckets[getIndex('O')] -= 1
    numbers[0] = z
    buckets[getIndex('Z')] = 0

    # Find all W's and pull out two
    w = buckets[getIndex('W')]
    for i in range(w):
        buckets[getIndex('T')] -= 1
        buckets[getIndex('O')] -= 1
    numbers[2] = w
    buckets[getIndex('W')] = 0

    # Find all X's and pull out six
    x = buckets[getIndex('X')]
    for i in range(x):
        buckets[getIndex('S')] -= 1
        buckets[getIndex('I')] -= 1
    numbers[6] = x
    buckets[getIndex('X')] = 0

    # Find all G's and pull out eight
    g = buckets[getIndex('G')]
    for i in range(g):
        buckets[getIndex('E')] -= 1
        buckets[getIndex('I')] -= 1
        buckets[getIndex('H')] -= 1
        buckets[getIndex('T')] -= 1
    numbers[8] = g
    buckets[getIndex('G')] = 0

    # Find all U's and pull out four
    u = buckets[getIndex('U')]
    for i in range(u):
        buckets[getIndex('F')] -= 1
        buckets[getIndex('O')] -= 1
        buckets[getIndex('R')] -= 1
    numbers[4] = u
    buckets[getIndex('U')] = 0

    # Find all O's and pull out one
    o = buckets[getIndex('O')]
    for i in range(o):
        buckets[getIndex('N')] -= 1
        buckets[getIndex('E')] -= 1
    numbers[1] = o
    buckets[getIndex('O')] = 0

    # Find all S's and pull out seven
    s = buckets[getIndex('S')]
    for i in range(s):
        buckets[getIndex('E')] -= 1
        buckets[getIndex('V')] -= 1
        buckets[getIndex('E')] -= 1
        buckets[getIndex('N')] -= 1
    numbers[7] = s
    buckets[getIndex('S')] = 0

    # Find all V's and pull out five
    v = buckets[getIndex('V')]
    for i in range(v):
        buckets[getIndex('F')] -= 1
        buckets[getIndex('I')] -= 1
        buckets[getIndex('E')] -= 1
    numbers[5] = v
    buckets[getIndex('V')] = 0

    # Find all H's and pull out three
    h = buckets[getIndex('H')]
    for i in range(h):
        buckets[getIndex('T')] -= 1
        buckets[getIndex('R')] -= 1
        buckets[getIndex('E')] -= 2
    numbers[3] = h
    buckets[getIndex('H')] = 0

    # Find all E's and pull out nine
    e = buckets[getIndex('E')]
    for i in range(e):
        buckets[getIndex('N')] -= 2
        buckets[getIndex('I')] -= 1
    numbers[9] = e
    buckets[getIndex('E')] = 0

    retValue = ""
    for i in range(len(numbers)):
        for j in range(numbers[i]):
            retValue += str(i)

    print(retValue)

    return (retValue)


# Number of test cases
T = int(inFile.readline())

# Read in each row
for counter in range(T):
    line = inFile.readline()
    if line != '':
        outFile.write("Case #" + str(counter + 1) + ": " + getValue(line) + "\n")

inFile.close()
outFile.close()
