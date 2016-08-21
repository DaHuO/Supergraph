
def ExtractDigits(s):
    #priority
    # ZERO - Z
    # SIX - X
    # TWO - W
    # FOUR - U
    # THREE - R
    # EIGHT - G
    # FIVE - F
    # SEVEN - V
    # ONE - O
    # NINE - N

    digits = []
    s = s.upper()

    while s != "":
        if "Z" in s:
            digits.append(0)
            s = s.replace("Z", '', 1)
            s = s.replace("E", '', 1)
            s = s.replace("R", '', 1)
            s = s.replace("O", '', 1)
        elif 'X' in s:
            digits.append(6)
            s = s.replace('S', '', 1)
            s = s.replace('I', '', 1)
            s = s.replace('X', '', 1)
        elif 'W' in s:
            digits.append(2)
            s = s.replace('T', '', 1)
            s = s.replace('W', '', 1)
            s = s.replace('O', '', 1)
        elif 'U' in s:
            digits.append(4)
            s = s.replace('F', '', 1)
            s = s.replace('O', '', 1)
            s = s.replace('U', '', 1)
            s = s.replace('R', '', 1)
        elif 'R' in s:
            digits.append(3)
            s = s.replace('T', '', 1)
            s = s.replace('H', '', 1)
            s = s.replace('R', '', 1)
            s = s.replace('E', '', 2)
        elif 'G' in s:
            digits.append(8)
            s = s.replace('E', '', 1)
            s = s.replace('I', '', 1)
            s = s.replace('G', '', 1)
            s = s.replace('H', '', 1)
            s = s.replace('T', '', 1)
        elif 'F' in s:
            digits.append(5)
            s = s.replace('F', '', 1)
            s = s.replace('I', '', 1)
            s = s.replace('V', '', 1)
            s = s.replace('E', '', 1)
        elif 'V' in s:
            digits.append(7)
            s = s.replace('S', '', 1)
            s = s.replace('E', '', 2)
            s = s.replace('V', '', 1)
            s = s.replace('N', '', 1)
        elif 'O' in s:
            digits.append(1)
            s = s.replace('O', '', 1)
            s = s.replace('N', '', 1)
            s = s.replace('E', '', 1)
        elif 'N' in s:
            digits.append(9)
            s = s.replace('N', '', 2)
            s = s.replace('I', '', 1)
            s = s.replace('E', '', 1)

    digits.sort()
    return digits

def main():
    f = open("phone.in", "r")
    numCases = int(f.readline())

    for i in range(1, numCases+1):
        s = f.readline().strip()
        digits = ExtractDigits(s)
        print("Case #", i, ": ", "".join(str(i) for i in digits), sep='')

main()
