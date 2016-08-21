# START SETUP #
modeWanted = input("b/s\n")
if modeWanted.upper() == "B":
    mode = "Big"
else:
    mode = "Small"
# GET FILES #
inputFile = open("inputs\\fractiles" + mode + ".in").readlines()
outputFile = open("outputs\\fractiles" + mode + "Out.txt", "w")
# MAIN #
caseNumber = 0
for case in inputFile[1:]:
    caseNumber += 1
    outputString = ""
    for i in range(1, int(case.rstrip().split(" ")[-1]) + 1):
        outputString += str(i) + " "
    outputFile.write("Case #" + str(caseNumber) + ": " + outputString.rstrip() + "\n")