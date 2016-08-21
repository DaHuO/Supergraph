
x = int(raw_input())
strings = []
for i in range(0, x):
    strings.append(raw_input())


for j in range(0, len(strings)):
    letters = {}
    letters.clear()
    for k in range(0, len(strings[j])):
        if strings[j][k] in letters:
            letters[strings[j][k]] += 1
        else:
            letters[strings[j][k]] = 1
    zeroans = ""
    oneans = ""
    twoans = ""
    threeans = ""
    ans = ""
    while ("Z" in letters and letters["Z"] != 0) and ("E" in letters and letters["E"] != 0) and ("R" in letters and letters["R"] != 0) and ("O" in letters and letters["O"] != 0):
        zeroans += "0"
        for l in ["Z", "E", "R", "O"]:
            letters[l] -= 1
    while ("T" in letters and letters["T"] != 0) and ("W" in letters and letters["W"] != 0) and ("O" in letters and letters["O"] != 0):
        twoans += "2"
        for l in ["T", "W", "O"]:
            letters[l] -= 1
    while ("F" in letters and letters["F"] != 0) and ("O" in letters and letters["O"] != 0) and ("U" in letters and letters["U"] != 0) and ("R" in letters and letters["R"] != 0):
        ans += "4"
        for l in ["F", "O", "U", "R"]:
            letters[l] -= 1
    while ("F" in letters and letters["F"] != 0) and ("I" in letters and letters["I"] != 0) and ("V" in letters and letters["V"] != 0) and ("E" in letters and letters["E"] != 0):
        ans += "5"
        for l in ["F", "I", "V", "E"]:
            letters[l] -= 1
    while ("S" in letters and letters["S"] != 0) and ("I" in letters and letters["I"] != 0) and ("X" in letters and letters["X"] != 0):
        ans += "6"
        for l in ["S", "I", "X"]:
            letters[l] -= 1
    while ("S" in letters and letters["S"] != 0) and ("V" in letters and letters["V"] != 0) and ("N" in letters and letters["N"] != 0) and ("E" in letters and letters["E"] != 0 and letters["E"] != 1):
        ans += "7"
        for l in ["S", "V", "N"]:
            letters[l] -= 1
        letters["E"] -= 2
    while ("E" in letters and letters["E"] != 0) and ("I" in letters and letters["I"] != 0) and ("G" in letters and letters["G"] != 0) and ("H" in letters and letters["H"] != 0) and ("T" in letters and letters["T"] != 0):
        ans += "8"
        for l in ["E", "I", "G", "H", "T"]:
            letters[l] -= 1
    while ("I" in letters and letters["I"] != 0) and ("E" in letters and letters["E"] != 0) and ("N" in letters and letters["N"] != 0 and letters["N"] != 1):
        ans += "9"
        for l in ["I", "E"]:
            letters[l] -= 1
        letters["N"] -= 2
    while ("O" in letters and letters["O"] != 0) and ("N" in letters and letters["N"] != 0) and ("E" in letters and letters["E"] != 0):
        oneans += "1"
        for l in ["O", "N", "E"]:
            letters[l] -= 1
    while ("T" in letters and letters["T"] != 0) and ("H" in letters and letters["H"] != 0) and ("R" in letters and letters["R"] != 0) and ("E" in letters and letters["E"] != 0 and letters["E"] != 1):
        threeans += "3"
        for l in ["T", "H", "R"]:
            letters[l] -= 1
        letters["E"] -= 2
    print "Case #" + str(j+1) + ": " + zeroans + oneans + twoans + threeans + ans
