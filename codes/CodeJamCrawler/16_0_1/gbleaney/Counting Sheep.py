input = open('./A-large.in', 'r')
output = open('./A-large.out', 'w')

def writeOut(i, out):
    output.write("Case #" + str(i) + ": " + str(out) + "\n")

tests = int(input.readline())

for i in range(1, tests+1):
    N = int(input.readline())
    if N == 0:
        writeOut(i, "INSOMNIA")
        continue

    seen = {}
    finalN = 0

    while not len(seen) == 10:
        finalN += N
        for char in str(finalN):
            seen[char] = True



    writeOut(i, finalN)

