# START SETUP #
modeWanted = input("b/s\n")
if modeWanted.upper() == "B":
    mode = "Big"
else:
    mode = "Small"
# GET FILES #
inputFile = open("inputs\\countingSheep" + mode + ".in").readlines()
outputFile = open("outputs\\countingSheep" + mode + "Out.txt", "w")
# MAIN #
caseNumber = 0
overText = "INSOMNIA"
for case in inputFile[1:]:
    caseNumber += 1
    if int(case) != 0:
        numberDict = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"0":0}
        maxItteration = 10**int(len(str(int(case))) + 1)
        i = 1
        while sum(numberDict.values()) != 10:
            bigNum = i * int(case)
            # PRINT OUT #
            print(int(case), "*", i, "=", bigNum)
            # GET NUMBERS FROM BIGNUM #
            for number in str(bigNum):
                numberDict[number] = 1
            # INCREACE ITTERATOR #
            i += 1
        over = False
    else:
        over = True
    if over:
        outputFile.write("Case #" + str(caseNumber) + ": " + overText + "\n")
    else:
        outputFile.write("Case #" + str(caseNumber) + ": " + str(bigNum) + "\n")