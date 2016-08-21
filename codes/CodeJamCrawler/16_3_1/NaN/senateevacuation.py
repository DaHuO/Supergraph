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
        textToParse = lineText[0:-1]
        inputParams = textToParse.split(" ")
        N = int(textToParse) # number of parties
        lineNr = lineNr + 1
        try:
            lineText = fileobject.readline()
        except:
            print("Failed to read line ", lineNr)
            sys.exit()
        textToParse = lineText.strip()
        partyMembers = list(map(int, textToParse.split(" ")))
        parties = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        leaveSequence = []
        while sum(partyMembers) > 0:
            leaveStep = []
            maxParty = None
            for partyPos in range(len(partyMembers)):
                if maxParty is None:
                    maxParty = partyPos
                elif partyMembers[maxParty] < partyMembers[partyPos]:
                    maxParty = partyPos
            leaveStep.append(parties[maxParty])
            partyMembers[maxParty] -= 1
            maxParty = None
            for partyPos in range(len(partyMembers)):
                if maxParty is None:
                    maxParty = partyPos
                elif partyMembers[maxParty] < partyMembers[partyPos]:
                    maxParty = partyPos
            # Check if removing the second member grants an absolute majority to a party.
            maxPartyPotential = None
            for partyPos in range(len(partyMembers)):
                if partyPos == maxPartyPotential:
                    members = partyMembers[partyPos] - 1
                else:
                    members = partyMembers[partyPos]
                if maxPartyPotential is None:
                    maxPartyPotential = partyPos
                    maxPartyCount = members
                elif partyMembers[maxPartyPotential] < members:
                    maxPartyPotential = partyPos
                    maxPartyCount = members
            otherParties = 0
            for partyPos in range(len(partyMembers)):
                if partyPos == maxPartyPotential:
                    continue
                otherParties += partyMembers[partyPos]
            # Only one party with one member left?
            oneSenator = (1 == sum(partyMembers) - 1)
            if otherParties >= maxPartyCount - 1 and partyMembers[maxParty] > 0 and not oneSenator:
                leaveStep.append(parties[maxParty])
                partyMembers[maxParty] -= 1
            leaveSequence.append("".join(leaveStep))
        output = " ".join(leaveSequence)
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", output, end="", sep="")