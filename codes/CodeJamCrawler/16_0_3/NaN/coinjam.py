import itertools
import math
import sys

if len(sys.argv) == 1:
    print("No input file provided.")
    sys.exit()
else:
    filename = sys.argv[1]
    try:
        fileobject = open(filename, 'r')
    except:
        print("Failed to open given file.")
        sys.exit()
    try:
        firstLine = fileobject.readline()
    except:
        print("Failed to read first line.")
        sys.exit()
    datasetSize = int(firstLine)
    if not datasetSize:
        print("Unable to parse dataset size.")
        sys.exit()
    lineNr = 1
    for i in range(datasetSize):
        lineNr = lineNr + 1
        try:
            lineText = fileobject.readline()
        except:
            print("Failed to read line ", lineNr)
            sys.exit()
        textToParse = lineText.strip()
        inputParams = textToParse.split(" ")
        N = int(inputParams[0]) # length of number
        J = int(inputParams[1]) # jam coins to create
        # Idea to find such numbers: All 1s must be part of symmetric blocks.
        # E.g. 10100101 = (n^(5+2) + n^5) + (n^(2+0) + n^0)
        #               = n^5 * (n^2 + 1) + (n^2 + 1)
        #               = (n^2 + 1) * (n^5 + 1)
        # So the sum of such symmetric block with lowest exponent as 0 is
        # non-trivial divisor.
        # Restrictions: First and last part of block must be a 1.
        # Let's check how we can satisfy our datasets:
        # Small: N = 16; J = 50: N/2 = 8; 8 - 2 = 6 (start and end 1), 2^6 = 64 > 50
        # Large: N = 32; J = 500: N/2 = 16; 16 - 2 = 14 (start and end 1),
        # 2^14 = 2^9 * 2^5 = 512 * 2^5 > 500
        # So it's sufficient to work with one group of symmetric blocks using
        # half of the sequence's length. For the example input, it wouldn't be
        # sufficient (3 solutions wanted, 2 found this way).
        L = N // 2 - 2 # length of the center part
        # Precalculate the expontential values and cache them.
        expValues = {}
        for n in range(2, 11):
            expValues[n] = []
            for j in range(N // 2 - 1, -1, -1):
                expValues[n].append(n**j)
        iter = itertools.product(range(2), repeat = L)
        print("Case #", i+1, ":", sep="")
        jamcoinsPrinted = 0
        for item in iter:
            sequence = [1]
            sequence.extend(list(item))
            sequence.append(1)
            divisors = []
            for n in range(2, 11):
                divisor = sum([b * v for b,v in zip(sequence, expValues[n])])
                divisors.append(divisor)
            sequenceHalf = "".join(map(str, sequence))
            sequenceFull = sequenceHalf + sequenceHalf
            print(sequenceFull, " ", " ".join(map(str, divisors)), sep="")
            jamcoinsPrinted += 1
            if jamcoinsPrinted == J:
                break
