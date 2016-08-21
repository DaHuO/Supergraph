# START SETUP #
modeWanted = input("b/s\n")
if modeWanted.upper() == "B":
    mode = "Big"
else:
    mode = "Small"
# GET FILES #
inputFile = open("inputs\\senateEvacuation" + mode + ".in").readlines()
outputFile = open("outputs\\senateEvacuation" + mode + "Out.txt", "w")
# MAIN #
caseNumber = 0
line1 = True
for case in inputFile[1:]:

    if line1:
        line1 = False
    else:
        caseNumber += 1
        line1 = True
        outputLine = ""
        # CONSTRUCT SENETOR DICT #
        partyDict = {}
        senetors = case.split()
        character = 65
        for party in senetors:
            partyDict[chr(character)] = int(party)
            character += 1
        totalSenators = 0
        for party in partyDict.keys():
            totalSenators += int(partyDict[party])
        while totalSenators != 0:
            # MAIN LOGIC #
            longestParty = []
            longestNum = 0
            for party in partyDict.keys():
                if int(partyDict[party]) > longestNum:
                    longestNum = int(partyDict[party])
                    longestParty = list(party)
                elif int(partyDict[party]) == longestNum:
                    longestParty.append(party)
            # CONSTRUCT OUTPUT LINE #
            if len(longestParty) > 1 and longestNum > 1:
                outputLine += str(longestParty[0]) + str(longestParty[1]) + " "
                partyDict[longestParty[0]] -= 1
                partyDict[longestParty[1]] -= 1
            elif len(longestParty) > 1 and longestNum == 1:
                if len(partyDict) != 3:
                    outputLine += str(longestParty[0]) + str(longestParty[1]) + " "
                    partyDict[longestParty[0]] -= 1
                    partyDict[longestParty[1]] -= 1
                else:
                    outputLine += str(longestParty[0]) + " "
                    partyDict[longestParty[0]] -= 1
            # COMPLICTED BIT (ONLY ONE LONGER) #
            else:
                if longestNum > 2 or len(partyDict) > 2:
                    outputLine += str(longestParty[0]) + str(longestParty[0]) + " "
                    partyDict[longestParty[0]] -= 2
                else:
                    outputLine += str(longestParty[0]) + " "
                    partyDict[longestParty[0]] -= 1
            # FIND TOTAL SENATORS LEFT #
            totalSenators = 0
            delList = []
            for party in partyDict.keys():
                totalSenators += int(partyDict[party])
                # SCRUB OUT EMPTY PARTIES #
                if partyDict[party] == 0:
                    delList.append(party)
            # SCRUB #
            for key in delList:
                del partyDict[key]
        print(outputLine.rstrip())
        outputFile.write("Case #" + str(caseNumber) + ": " + outputLine.rstrip() + "\n")