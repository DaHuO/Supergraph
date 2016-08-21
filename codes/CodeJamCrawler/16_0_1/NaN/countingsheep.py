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
        Nstart = int(lineText.strip())
        if Nstart == 0:
            output = "INSOMNIA"
        else:
            Ncurr = Nstart
            digitsSeen = set()
            while True:
                digitsSeen = digitsSeen.union(set(str(Ncurr)))
                if len(digitsSeen) == 10:
                    output = str(Ncurr)
                    break
                else:
                    Ncurr += Nstart
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", output, end="", sep="")