numbrid = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
o = open("digitsinput.txt")
ridu = int(o.readline())
c = open("digitsoutput.txt", "w")
for x in range(1, ridu+1):
    string = o.readline()
    t2hed = []
    telefon = []
    for i in range(len(string)):
        t2hed.append(string[i])

    while "Z" in t2hed:
        telefon.append("0")
        t2hed.remove("Z")
        t2hed.remove("E")
        t2hed.remove("R")
        t2hed.remove("O")
    while "W" in t2hed:
        telefon.append("2")
        t2hed.remove("T")
        t2hed.remove("W")
        t2hed.remove("O")
    while "U" in t2hed:
        telefon.append("4")
        t2hed.remove("F")
        t2hed.remove("O")
        t2hed.remove("U")
        t2hed.remove("R")
    while "X" in t2hed:
        telefon.append("6")
        t2hed.remove("S")
        t2hed.remove("I")
        t2hed.remove("X")
    while "G" in t2hed:
        telefon.append("8")
        t2hed.remove("E")
        t2hed.remove("I")
        t2hed.remove("G")
        t2hed.remove("H")
        t2hed.remove("T")
        
    while "F" in t2hed:
        telefon.append("5")
        t2hed.remove("F")
        t2hed.remove("I")
        t2hed.remove("V")
        t2hed.remove("E")
    while "H" in t2hed:
        telefon.append("3")
        t2hed.remove("T")
        t2hed.remove("H")
        t2hed.remove("R")
        t2hed.remove("E")
        t2hed.remove("E")

    while "V" in t2hed:
        telefon.append("7")
        t2hed.remove("S")
        t2hed.remove("E")
        t2hed.remove("V")
        t2hed.remove("E")
        t2hed.remove("N")

    while "O" in t2hed:
        telefon.append("1")
        t2hed.remove("O")
        t2hed.remove("N")
        t2hed.remove("E")

    while "I" in t2hed:
        telefon.append("9")
        t2hed.remove("N")
        t2hed.remove("I")
        t2hed.remove("N")
        t2hed.remove("E")

    telefon.sort()
    c.write("Case #" + str(x) + ": " + "".join(telefon) + "\n")
    print("Case #" + str(x) + ": " + "".join(telefon))

o.close()
c.close()
