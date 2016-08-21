inputFile = open("B-large.in")
outputFile = open("B-large.out", "w")



def getDeepestBlank(sequence):
    sequence = sequence[::-1]
    for index, char in enumerate(sequence):
        if char == "-":
            return len(sequence) - index

def getDeepestContinuousSmile(sequence):
    for index, char in enumerate(sequence):
        if char == "-":
            return index

def performFlip(sequence, index):
    first = list(sequence[0:index])
    second = sequence[index:]

    first = first[::-1]

    for index, char in enumerate(first):
        if char == "-":
            first[index] = "+"
        else:
            first[index] = "-"

    return "".join(first) + second

testcases = int(inputFile.readline())

for testCase in range(testcases):
    seq = inputFile.readline()

    allSmiles = True

    for char in seq:
        if char == "-":
            allSmiles = False
            break

    if allSmiles:
        print("Took", 0, "flips")
        outputFile.write("Case #" + str(testCase+1) + ": 0\n")

    else:
        for i in range(10000):
            if seq[0] == "+":
                seq = performFlip(seq, getDeepestContinuousSmile(seq))
            else:
                seq = performFlip(seq, getDeepestBlank(seq))

            allSmiles = True

            for char in seq:
                if char == "-":
                    allSmiles = False
                    break

            if allSmiles:
                print("Took", i + 1, "flips")
                outputFile.write("Case #" + str(testCase+1) + ": " + str(i+1) + "\n")
                break

inputFile.close()
outputFile.close()
