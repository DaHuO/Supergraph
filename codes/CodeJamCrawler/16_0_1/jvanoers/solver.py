import os, sys

if not len(sys.argv) > 1:
    print("Enter input")
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print("File not found")
    sys.exit(1)

numberOfLines = 0
data = []
with open(sys.argv[1], 'r') as f:
    z = 0
    for i, line in enumerate(f):
        if i == 0:
            numberOfLines = int(line)
        else:
            data.append(int(line))
            if z > numberOfLines:
                print("WARN: More tests than specified: {0} instead of {1}".format(z, numberOfLines))

    z += 1


def calculate(value, debug=False):
    seenNos = []
    maxIter = 100000
    originalValue = value

    i = 1
    cur = value
    while i < maxIter:
        nos = getList(cur)
        for x in nos:
            if x not in seenNos:
                if debug:
                    print("Seen new no. {0} with result {1}".format(x, cur))
                seenNos.append(x)

        if canSleep(seenNos, debug):
            return cur
        else:
            i += 1
            cur = originalValue * i
            if debug:
                print("New value {0}".format(cur))

    return "INSOMNIA"


def canSleep(seenNos, debug):
    if debug:
        print("Testing...")
        print(seenNos)
    return all(x in seenNos for x in [0,1,2,3,4,5,6,7,8,9])

def getList(number):
    ret = []
    for char in str(number):
        ret.append(int(char))
    return ret


outArray = []
i = 1
for test in data:
    value = calculate(test)
    out = "Case #{0}: {1}".format(i, value)
    outArray.append(out)
    print(out)
    i += 1

with open('output.txt', 'w') as o:
    o.write('\n'.join(outArray))
