import sys, math

letters = [["Z", "E", "R", "O"],
           ["O", "N", "E"],
           ["T", "W", "O"],
           ["T", "H", "R", "E", "E"],
           ["F", "O", "U", "R"],
           ["F", "I", "V", "E"],
           ["S", "I", "X"],
           ["S", "E", "V", "E", "N"],
           ["E", "I", "G", "H", "T"],
           ["N", "I", "N", "E"]]
uniq_letters = [["O"],
           ["T", "H", "R"],
           ["F"],
           ["S"],
           []]

stdin = sys.stdin.readlines()
cases = int(stdin.pop(0))

for case in xrange(cases):
    s = list(stdin.pop(0).strip())
    letter_counts = {"F": 0, "G": 0, "H": 0, "I": 0, "O": 0, "S": 0, "U": 0, "W": 0, "X": 0, "Z": 0}
    for let in s:
        try:
            letter_counts[let] += 1
        except KeyError:
            letter_counts[let] = 1
    digits = [0] * 10
    while letter_counts["Z"]:
        digits[0] += 1
        letter_counts["Z"] -= 1
        letter_counts["E"] -= 1
        letter_counts["R"] -= 1
        letter_counts["O"] -= 1
    while letter_counts["W"]:
        digits[2] += 1
        letter_counts["T"] -= 1
        letter_counts["W"] -= 1
        letter_counts["O"] -= 1
    while letter_counts["U"]:
        digits[4] += 1
        letter_counts["F"] -= 1
        letter_counts["O"] -= 1
        letter_counts["U"] -= 1
        letter_counts["R"] -= 1
    while letter_counts["X"]:
        digits[6] += 1
        letter_counts["S"] -= 1
        letter_counts["I"] -= 1
        letter_counts["X"] -= 1
    while letter_counts["G"]:
        digits[8] += 1
        letter_counts["E"] -= 1
        letter_counts["I"] -= 1
        letter_counts["G"] -= 1
        letter_counts["H"] -= 1
        letter_counts["T"] -= 1
    while letter_counts["O"]:
        digits[1] += 1
        letter_counts["O"] -= 1
        letter_counts["N"] -= 1
        letter_counts["E"] -= 1
    while letter_counts["H"]:
        digits[3] += 1
        letter_counts["T"] -= 1
        letter_counts["H"] -= 1
        letter_counts["R"] -= 1
        letter_counts["E"] -= 2
    while letter_counts["F"]:
        digits[5] += 1
        letter_counts["F"] -= 1
        letter_counts["I"] -= 1
        letter_counts["V"] -= 1
        letter_counts["E"] -= 1
    while letter_counts["S"]:
        digits[7] += 1
        letter_counts["S"] -= 1
        letter_counts["E"] -= 2
        letter_counts["V"] -= 1
        letter_counts["N"] -= 1
    while letter_counts["I"]:
        digits[9] += 1
        letter_counts["N"] -= 2
        letter_counts["I"] -= 1
        letter_counts["E"] -= 1
    res = ""
    for i in range(10):
        res += str(i) * digits[i]
    print("Case #" + str(case+1) + ": " + res)
