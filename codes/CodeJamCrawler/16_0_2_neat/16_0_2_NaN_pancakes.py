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
        # Reduce the sequence by representing it as alternating blocks.
        # Flipping a part of a block would never be an advantage over
        # flipping the whole block because it potential adds a new alternation
        # while flipping the whole block never does.
        sequenceReduced = []
        for letter in textToParse:
            if len(sequenceReduced) == 0:
                sequenceReduced.append(letter)
            if sequenceReduced[-1] != letter:
                sequenceReduced.append(letter)
        # If the last (bottom) part of the reduced sequence is '+', it doesn't
        # need to be flipped. If there is a second last part, it's always '-'.
        # If the first part of the reduced sequence is '-', flipping all
        # pancakes up to (including) the last '-', the pancakes of the first
        # '-' will become '+', reducing the length of the sequence which is
        # still unordered by 1.
        # If the first part of the reduced sequence is '+', flipping only the
        # first block of the reduced sequence will turn them to '-' and they
        # will be followed by the second block of the reduced sequence which
        # already are '-'. Now flipping all pancakes up to (including) the
        # last '-', the pancakes of the former first two blocks of the
        # reduced sentence become '+', reducing the length of the sequence
        # which is still unordered by 2 in 2 steps.
        if sequenceReduced[-1] == "+":
            output = len(sequenceReduced) - 1
        else:
            output = len(sequenceReduced)
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", output, end="", sep="")