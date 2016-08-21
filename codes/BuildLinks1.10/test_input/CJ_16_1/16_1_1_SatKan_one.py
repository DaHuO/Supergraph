import sys

fp = open(sys.argv[1], "r")
output = open(sys.argv[2], "w")

total = int(fp.readline())

case = 0

alphabet = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}


for string in fp:
    case = case + 1
    final = ""

    for letter in string:
        # print("final:", final)
        if letter == "\n":
            continue

        if len(final) == 0:
            final = final + letter
            continue

        if alphabet[letter] < alphabet[final[0]]:
            final = final + letter
            continue
        else:
            final = letter + final

    out = "Case #{}: {}".format(case, final)
    print(out)
    output.write(out + "\n")

fp.close()
output.close()
