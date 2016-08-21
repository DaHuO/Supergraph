def delete_char(s, i):
    return s[:i] + s[(i + 1):]

def delete_digit(s, digit):
    for c in digit:
        i = s.find(c)
        s = delete_char(s, i)
    return s

def decode(s):
    digits = []
    if 'Z' in s:
        s = delete_digit(s, "ZERO")
        digits = decode(s)
        digits.append(0)
        return digits
    if 'W' in s:
        s = delete_digit(s, "TWO")
        digits = decode(s)
        digits.append(2)
        return digits
    if 'U' in s:
        s = delete_digit(s, "FOUR")
        digits = decode(s)
        digits.append(4)
        return digits
    if 'X' in s:
        s = delete_digit(s, "SIX")
        digits = decode(s)
        digits.append(6)
        return digits
    if 'G' in s:
        s = delete_digit(s, "EIGHT")
        digits = decode(s)
        digits.append(8)
        return digits
    if 'H' in s:
        s = delete_digit(s, "THREE")
        digits = decode(s)
        digits.append(3)
        return digits
    if 'F' in s:
        s = delete_digit(s, "FIVE")
        digits = decode(s)
        digits.append(5)
        return digits
    if 'V' in s:
        s = delete_digit(s, "SEVEN")
        digits = decode(s)
        digits.append(7)
        return digits
    if 'O' in s:
        s = delete_digit(s, "ONE")
        digits = decode(s)
        digits.append(1)
        return digits
    if 'N' in s:
        s = delete_digit(s, "NINE")
        digits = decode(s)
        digits.append(9)
        return digits
    return digits


fin = open("in.in", "r")
fout = open("out.out", "w")

n = int(fin.readline())

i = 1

for line in fin:
    res = decode(line.rstrip())
    res.sort()
    fout.write("Case #" + str(i) + ": " + ''.join(map(str, res)) +"\n")
    i += 1

fin.close()
fout.close()

dictionary = {"ZERO": 0, "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9}


