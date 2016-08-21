# Google Code Jam Qualification Round - Problem A
def getFiles(name):
    return open(name + '.in', 'r'), open(name + '.out', 'w')

name = 'example'
name = 'A-small-attempt0'
name = 'A-large'

inFile, outFile = getFiles(name)

def getValue(N):
    # The only time she won't encounter every number is if she sees a 0
    if N == 0:
        return "INSOMNIA"
    else:
        multiplier = 1
        # Keep track of which digits have been seen
        digitSeen = [False for _ in range(10)]

        while digitSeen.count(False) > 0:
            value = N * multiplier
            multiplier += 1

            for i in str(value):
                digitSeen[int(i)] = True

        return str(value)

# Number of test cases
T = int(inFile.readline())

# Read in each row
for counter in range(T):
    line = inFile.readline()
    if line != '':
        N = int(line)
        outFile.write("Case #" + str(counter + 1) + ": " + getValue(N) + "\n")

inFile.close()
outFile.close()
