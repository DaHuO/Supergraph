# START SETUP #
modewanted = input("b/s\n")
if modewanted.upper() == "B":
    mode = "Big"
else:
    mode = "Small"
# GET FILES #
inputFile = open("inputs\\getTheDigits" + mode + ".in").readlines()
outputFile = open("outputs\\getTheDigits" + mode + "Out.txt", "w")
# MAIN #
caseNumber = 0
for case in inputFile[1:]:
    caseNumber += 1
    totalLetterDict = {"A":0,
                       "B":0,
                       "C":0,
                       "D":0,
                       "E":0,
                       "F":0,
                       "G":0,
                       "H":0,
                       "I":0,
                       "J":0,
                       "K":0,
                       "L":0,
                       "M":0,
                       "N":0,
                       "O":0,
                       "P":0,
                       "Q":0,
                       "R":0,
                       "S":0,
                       "T":0,
                       "U":0,
                       "V":0,
                       "W":0,
                       "X":0,
                       "Y":0,
                       "Z":0}
    stringList = list(case.rstrip())
    for letter in stringList:
        totalLetterDict[letter] += 1
    # GET NUMBERS THAT HAVE UNIQUE CHARACTERS #
    no0s = totalLetterDict["Z"]
    no2s = totalLetterDict["W"]
    no4s = totalLetterDict["U"]
    no6s = totalLetterDict["X"]
    no8s = totalLetterDict["G"]
    # REMOVE ZEROS #
    totalLetterDict["Z"] -= no0s
    totalLetterDict["E"] -= no0s
    totalLetterDict["R"] -= no0s
    totalLetterDict["O"] -= no0s
    # REMOVE TWOS #
    totalLetterDict["T"] -= no2s
    totalLetterDict["W"] -= no2s
    totalLetterDict["O"] -= no2s
    # REMOVE FOURS #
    totalLetterDict["F"] -= no4s
    totalLetterDict["O"] -= no4s
    totalLetterDict["U"] -= no4s
    totalLetterDict["R"] -= no4s
    # REMOVE SIXS #
    totalLetterDict["S"] -= no6s
    totalLetterDict["I"] -= no6s
    totalLetterDict["X"] -= no6s
    # REMOVE EIGHTS #
    totalLetterDict["E"] -= no8s
    totalLetterDict["I"] -= no8s
    totalLetterDict["G"] -= no8s
    totalLetterDict["H"] -= no8s
    totalLetterDict["T"] -= no8s
    # GET NUMBERS THAT HAVE UNIQUE CHARACTERS #
    no1s = totalLetterDict["O"]
    no3s = totalLetterDict["R"]
    no5s = totalLetterDict["F"]
    no7s = totalLetterDict["S"]
    # REMOVE ONES #
    totalLetterDict["O"] -= no1s
    totalLetterDict["N"] -= no1s
    totalLetterDict["E"] -= no1s
    # REMOVE THREES #
    totalLetterDict["T"] -= no3s
    totalLetterDict["H"] -= no3s
    totalLetterDict["R"] -= no3s
    totalLetterDict["E"] -= no3s
    totalLetterDict["E"] -= no3s
    # REMOVE FIVES #
    totalLetterDict["F"] -= no5s
    totalLetterDict["I"] -= no5s
    totalLetterDict["V"] -= no5s
    totalLetterDict["E"] -= no5s
    # REMOVE SEVENS #
    totalLetterDict["S"] -= no7s
    totalLetterDict["E"] -= no7s
    totalLetterDict["V"] -= no7s
    totalLetterDict["E"] -= no7s
    totalLetterDict["N"] -= no7s
    # GET NUMBER OF NINES #
    no9s = totalLetterDict["I"]
    # GET PHONE NUMBER #
    phoneNumber = ""
    for i in range(no0s):
        phoneNumber += "0"
    for i in range(no1s):
        phoneNumber += "1"
    for i in range(no2s):
        phoneNumber += "2"
    for i in range(no3s):
        phoneNumber += "3"
    for i in range(no4s):
        phoneNumber += "4"
    for i in range(no5s):
        phoneNumber += "5"
    for i in range(no6s):
        phoneNumber += "6"
    for i in range(no7s):
        phoneNumber += "7"
    for i in range(no8s):
        phoneNumber += "8"
    for i in range(no9s):
        phoneNumber += "9"
    outputFile.write("Case #" + str(caseNumber) + ": " + phoneNumber + "\n")