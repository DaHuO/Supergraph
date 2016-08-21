from time import sleep

answers = []

def jam(s):
    out = []
    while "Z" in s:
        out.append("0")
        for letter in "ZERO":
            s.remove(letter)
    while "W" in s:
        out.append("2")
        for letter in "TWO":
            s.remove(letter)
    while "X" in s:
        out.append("6")
        for letter in "SIX":
            s.remove(letter)
    while "S" in s:
        out.append("7")
        for letter in "SEVEN":
            s.remove(letter)
    while "V" in s:
        out.append("5")
        for letter in "FIVE":
            s.remove(letter)
    while "F" in s:
        out.append("4")
        for letter in "FOUR":
            s.remove(letter)
    while "G" in s:
        out.append("8")
        for letter in "EIGHT":
            s.remove(letter)
    while "H" in s:
        out.append("3")
        for letter in "THREE":
            s.remove(letter)
    while "I" in s:
        out.append("9")
        for letter in "NINE":
            s.remove(letter)
    while "N" in s:
        out.append("1")
        for letter in "ONE":
            s.remove(letter)
    return "".join(sorted(out))

with open("A-large.in") as f:
    lines = f.readlines()[1:]
    for i, string in enumerate(lines, 1):
        print ("trying ", string)
        answers.append("Case #{}: {}".format(i, jam(list(string.rstrip()))))

with open("answers.txt", "w") as f:
    f.write("\n".join(answers))
