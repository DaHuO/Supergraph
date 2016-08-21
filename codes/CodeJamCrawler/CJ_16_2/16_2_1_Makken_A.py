def solve(number):
    nr=[]

    while len(number) != 0:
        if 'Z' in number:
            nr.append(0)
            number.remove("Z")
            number.remove("E")
            number.remove("R")
            number.remove("O")
            continue
        elif 'G' in number:
            nr.append(8)
            number.remove("E")
            number.remove("I")
            number.remove("G")
            number.remove("T")
            number.remove("H")
            continue
        elif 'W' in number:
            nr.append(2)
            number.remove("T")
            number.remove("W")
            number.remove("O")
            continue
        elif 'X' in number:
            nr.append(6)
            number.remove("S")
            number.remove("I")
            number.remove("X")
            continue
        elif 'U' in number:
            nr.append(4)
            number.remove("F")
            number.remove("O")
            number.remove("U")
            number.remove("R")
            continue
        elif 'S' in number:
            nr.append(7)
            number.remove("S")
            number.remove("E")
            number.remove("V")
            number.remove("E")
            number.remove("N")
            continue
        elif 'O' in number:
            nr.append(1)
            number.remove("O")
            number.remove("N")
            number.remove("E")
            continue
        elif 'H' in number:
            nr.append(3)
            number.remove("T")
            number.remove("H")
            number.remove("R")
            number.remove("E")
            number.remove("E")
            continue
        elif 'V' in number:
            nr.append(5)
            number.remove("F")
            number.remove("I")
            number.remove("V")
            number.remove("E")
            continue
        elif 'N' in number:
            nr.append(9)
            number.remove("N")
            number.remove("I")
            number.remove("N")
            number.remove("E")
            continue
    return "".join(sorted([str(x) for x in nr]))

for item in range(1, int(input()) + 1):
    current = sorted(list(input()))
    print("Case #{}: {}".format(item, solve(current)))
